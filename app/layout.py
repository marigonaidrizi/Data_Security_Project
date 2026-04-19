
from __future__ import annotations

from typing import Callable

import customtkinter as ctk

from .styles import COLORS, FONTS, PAD, SIDEBAR_WIDTH
from .widgets import (
    ActionButton,
    LabeledEntry,
    Panel,
    SidebarButton,
    StatusPanel,
    TextArea,
)


class Sidebar(ctk.CTkFrame):
    """Fixed left column: cipher tabs and status only (no brand header)."""

    def __init__(self, master, on_select: Callable[[str], None]):
        super().__init__(
            master,
            width=SIDEBAR_WIDTH,
            fg_color=COLORS["bg_alt"],
            corner_radius=0,
        )
        self.grid_propagate(False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self._on_select = on_select
        self._buttons: dict[str, SidebarButton] = {}

        self._build_tabs()
        self.status = StatusPanel(self)
        self.status.grid(
            row=2,
            column=0,
            sticky="ews",
            padx=PAD["md"],
            pady=(PAD["sm"], PAD["md"]),
        )

    def _build_tabs(self) -> None:
        container = ctk.CTkFrame(self, fg_color="transparent")
        container.grid(
            row=0,
            column=0,
            sticky="new",
            padx=PAD["md"],
            pady=(PAD["md"], PAD["sm"]),
        )
        container.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            container,
            text="CIPHERS",
            font=FONTS["label_sm"],
            text_color=COLORS["text_muted"],
            anchor="w",
        ).grid(row=0, column=0, sticky="ew", pady=(0, PAD["xs"]))

        for i, (key, label) in enumerate(
            (
                ("running_key", "Running Key Cipher"),
                ("double_transposition", "Double Transposition"),
            ),
            start=1,
        ):
            btn = SidebarButton(
                container,
                text=label,
                command=lambda k=key: self._on_select(k),
            )
            btn.grid(row=i, column=0, sticky="ew", pady=(0, PAD["xs"]))
            self._buttons[key] = btn

    def set_active(self, key: str) -> None:
        for k, btn in self._buttons.items():
            btn.set_active(k == key)


class ContentArea(ctk.CTkFrame):
    """Right pane: fixed-height chrome, then input/output share remaining height.

    No outer scroll — rows use weights so a typical laptop viewport fits.
    """

    def __init__(self, master):
        super().__init__(master, fg_color=COLORS["bg"], corner_radius=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=2)

        self._build_key_panel()
        self._build_actions_panel()
        self._build_input_panel()
        self._build_output_panel()

    def _build_key_panel(self) -> None:
        panel = Panel(self, title="Key", accent=True)
        panel.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=PAD["lg"],
            pady=(PAD["md"], PAD["xs"]),
        )

        body = panel.body()
        body.grid_columnconfigure(0, weight=1)

        self.key_input = LabeledEntry(
            body,
            label="Cipher key",
            placeholder="Enter key...",
        )
        self.key_input.grid(row=0, column=0, sticky="ew")

        self.key_helper_var = ctk.StringVar(value="")
        ctk.CTkLabel(
            body,
            textvariable=self.key_helper_var,
            font=FONTS["label_sm"],
            text_color=COLORS["text_muted"],
            anchor="w",
            justify="left",
            wraplength=780,
        ).grid(row=1, column=0, sticky="ew", pady=(PAD["xs"], 0))

    def _build_actions_panel(self) -> None:
        panel = Panel(self, title="Actions", accent=True)
        panel.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=PAD["lg"],
            pady=(PAD["xs"], PAD["xs"]),
        )

        body = panel.body()
        for col in range(4):
            body.grid_columnconfigure(col, weight=1, uniform="actions")

        self.encrypt_btn = ActionButton(
            body, "Encrypt", command=lambda: None, variant="primary"
        )
        self.decrypt_btn = ActionButton(
            body, "Decrypt", command=lambda: None, variant="secondary"
        )
        self.swap_btn = ActionButton(body, "Swap", command=lambda: None, variant="ghost")
        self.clear_btn = ActionButton(body, "Clear", command=lambda: None, variant="ghost")

        self.encrypt_btn.grid(row=0, column=0, sticky="ew", padx=(0, PAD["xs"]))
        self.decrypt_btn.grid(row=0, column=1, sticky="ew", padx=PAD["xs"])
        self.swap_btn.grid(row=0, column=2, sticky="ew", padx=PAD["xs"])
        self.clear_btn.grid(row=0, column=3, sticky="ew", padx=(PAD["xs"], 0))

    def _build_input_panel(self) -> None:
        panel = Panel(self, title="Input Text", accent=True)
        panel.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=PAD["lg"],
            pady=(PAD["xs"], PAD["xs"]),
        )

        body = panel.body()
        body.grid_columnconfigure(0, weight=1)
        body.grid_rowconfigure(0, weight=1)

        self.input_area = TextArea(
            body,
            "Plaintext / Ciphertext",
            height=96,
            expand_height=True,
        )
        self.input_area.grid(row=0, column=0, sticky="nsew")

    def _build_output_panel(self) -> None:
        panel = Panel(self, title="Output Text", accent=True)
        panel.grid(
            row=3,
            column=0,
            sticky="nsew",
            padx=PAD["lg"],
            pady=(PAD["xs"], PAD["md"]),
        )

        body = panel.body()
        body.grid_columnconfigure(0, weight=1)
        body.grid_rowconfigure(1, weight=1)

        toolbar = ctk.CTkFrame(body, fg_color="transparent")
        toolbar.grid(row=0, column=0, sticky="ew", pady=(0, PAD["xs"]))
        toolbar.grid_columnconfigure(0, weight=1)

        self.output_meta_var = ctk.StringVar(value="0 chars")
        ctk.CTkLabel(
            toolbar,
            textvariable=self.output_meta_var,
            font=FONTS["label_sm"],
            text_color=COLORS["text_muted"],
            anchor="w",
        ).grid(row=0, column=0, sticky="w")

        self.copy_btn = ActionButton(
            toolbar,
            "Copy Text",
            command=lambda: None,
            variant="secondary",
            width=120,
        )
        self.copy_btn.grid(row=0, column=1, sticky="e")

        self.output_area = TextArea(
            body,
            "Result",
            height=120,
            expand_height=True,
        )
        self.output_area.grid(row=1, column=0, sticky="nsew")
