
from __future__ import annotations

import customtkinter as ctk

from ciphers import (
    double_transposition_decrypt,
    double_transposition_encrypt,
    running_key_decrypt,
    running_key_encrypt,
)
from ciphers.running_key import CipherError
from utils.text_utils import normalize_alpha
from utils.validators import validate_double_transposition, validate_running_key

from .layout import ContentArea, Sidebar
from .styles import (
    APP_TITLE,
    COLORS,
    WINDOW_DEFAULT_SIZE,
    WINDOW_MIN_SIZE,
)


CIPHERS = {
    "running_key": {
        "label": "Running Key Cipher",
        "key_help": (
            "Key must be at least as long as the text (letters only; spaces ignored)."
        ),
        "encrypt": running_key_encrypt,
        "decrypt": running_key_decrypt,
        "validate": validate_running_key,
    },
    "double_transposition": {
        "label": "Double Transposition",
        "key_help": "Key sets column count and read order. Padding: X.",
        "encrypt": double_transposition_encrypt,
        "decrypt": double_transposition_decrypt,
        "validate": validate_double_transposition,
    },
}


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(APP_TITLE)
        self.geometry(f"{WINDOW_DEFAULT_SIZE[0]}x{WINDOW_DEFAULT_SIZE[1]}")
        self.minsize(*WINDOW_MIN_SIZE)
        self.configure(fg_color=COLORS["bg"])

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = Sidebar(self, on_select=self.select_cipher)
        self.sidebar.grid(row=0, column=0, sticky="nsw")

        self.content = ContentArea(self)
        self.content.grid(row=0, column=1, sticky="nsew")

        self._wire_actions()

        self._active_key = "running_key"
        self.select_cipher(self._active_key)
        self.sidebar.status.set("Ready.", "muted")

    def _wire_actions(self) -> None:
        self.content.encrypt_btn.configure(command=self._on_encrypt)
        self.content.decrypt_btn.configure(command=self._on_decrypt)
        self.content.swap_btn.configure(command=self._on_swap)
        self.content.clear_btn.configure(command=self._on_clear)
        self.content.copy_btn.configure(command=self._on_copy)

        self.content.output_area.textbox.bind(
            "<<Modified>>", self._refresh_output_meta
        )

    def select_cipher(self, key: str) -> None:
        if key not in CIPHERS:
            return
        self._active_key = key
        cfg = CIPHERS[key]

        self.sidebar.set_active(key)
        self.sidebar.status.set_cipher(cfg["label"])
        self.sidebar.status.set(f"Selected: {cfg['label']}.", "info")

        self.content.key_helper_var.set(cfg["key_help"])

    def _current(self):
        return CIPHERS[self._active_key]

    def _on_encrypt(self) -> None:
        cfg = self._current()
        text = self.content.input_area.get()
        key = self.content.key_input.get()

        error = cfg["validate"](text, key)
        if error:
            self.sidebar.status.set(error, "error")
            return

        try:
            result = cfg["encrypt"](text, key)
        except CipherError as exc:
            self.sidebar.status.set(str(exc), "error")
            return
        except Exception as exc:
            self.sidebar.status.set(f"Unexpected error: {exc}", "error")
            return

        self.content.output_area.set(result)
        self._refresh_output_meta()
        self.sidebar.status.set(
            f"Encrypted with {cfg['label']} ({len(result)} chars).", "success"
        )

    def _on_decrypt(self) -> None:
        cfg = self._current()
        text = self.content.input_area.get()
        key = self.content.key_input.get()

        if not normalize_alpha(text):
            self.sidebar.status.set("Input is empty.", "error")
            return
        if not normalize_alpha(key):
            self.sidebar.status.set("Key is empty.", "error")
            return

        if self._active_key == "running_key":
            t_len = len(normalize_alpha(text))
            k_len = len(normalize_alpha(key))
            if k_len < t_len:
                self.sidebar.status.set(
                    f"Key too short: need >= {t_len} letters, got {k_len}.",
                    "error",
                )
                return

        try:
            result = cfg["decrypt"](text, key)
        except CipherError as exc:
            self.sidebar.status.set(str(exc), "error")
            return
        except Exception as exc:
            self.sidebar.status.set(f"Unexpected error: {exc}", "error")
            return

        self.content.output_area.set(result)
        self._refresh_output_meta()
        self.sidebar.status.set(
            f"Decrypted with {cfg['label']} ({len(result)} chars).", "success"
        )

    def _on_swap(self) -> None:
        a = self.content.input_area.get()
        b = self.content.output_area.get()
        self.content.input_area.set(b)
        self.content.output_area.set(a)
        self._refresh_output_meta()
        self.sidebar.status.set("Swapped input and output.", "info")

    def _on_clear(self) -> None:
        self.content.key_input.set("")
        self.content.input_area.clear()
        self.content.output_area.clear()
        self._refresh_output_meta()
        self.sidebar.status.set("Cleared all fields.", "muted")

    def _on_copy(self) -> None:
        text = self.content.output_area.get()
        if not text:
            self.sidebar.status.set("Nothing to copy.", "warn")
            return
        try:
            self.clipboard_clear()
            self.clipboard_append(text)
            self.update()
        except Exception as exc:
            self.sidebar.status.set(f"Clipboard error: {exc}", "error")
            return
        self.sidebar.status.set(f"Copied {len(text)} chars to clipboard.", "success")

    def _refresh_output_meta(self, _event=None) -> None:
        text = self.content.output_area.get()
        self.content.output_meta_var.set(f"{len(text)} chars")
        try:
            self.content.output_area.textbox.edit_modified(False)
        except Exception:
            pass
