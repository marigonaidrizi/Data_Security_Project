

from __future__ import annotations

import customtkinter as ctk

from .styles import COLORS, CORNER, FONTS, PAD


class Panel(ctk.CTkFrame):
    """A rounded card with an optional header and accent strip."""

    def __init__(self, master, title: str | None = None, *, accent: bool = False, **kwargs):
        super().__init__(
            master,
            fg_color=COLORS["panel"],
            border_color=COLORS["border"],
            border_width=1,
            corner_radius=CORNER["panel"],
            **kwargs,
        )
        self.grid_columnconfigure(0, weight=1)
        self._next_row = 0

        if title is not None:
            header = ctk.CTkFrame(self, fg_color="transparent")
            header.grid(row=0, column=0, sticky="ew",
                        padx=PAD["md"], pady=(PAD["sm"], 0))
            header.grid_columnconfigure(1, weight=1)

            if accent:
                strip = ctk.CTkFrame(
                    header,
                    width=3,
                    height=14,
                    fg_color=COLORS["accent"],
                    corner_radius=2,
                )
                strip.grid(row=0, column=0, padx=(0, PAD["sm"]), pady=2)

            label = ctk.CTkLabel(
                header,
                text=title.upper(),
                font=FONTS["h2"],
                text_color=COLORS["text"],
                anchor="w",
            )
            label.grid(row=0, column=1, sticky="w")
            self.title_label = label
            self.header = header
            self._next_row = 1

    def body(self) -> ctk.CTkFrame:
        """Return a transparent body frame ready for content."""
        frame = ctk.CTkFrame(self, fg_color="transparent")
        frame.grid(
            row=self._next_row,
            column=0,
            sticky="nsew",
            padx=PAD["md"],
            pady=(PAD["sm"], PAD["md"]),
        )
        frame.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(self._next_row, weight=1)
        self._next_row += 1
        return frame


class SidebarButton(ctk.CTkButton):
    """Left-aligned tab button used in the sidebar cipher list."""

    def __init__(self, master, text: str, command, **kwargs):
        super().__init__(
            master,
            text="  " + text,
            command=command,
            anchor="w",
            height=42,
            corner_radius=CORNER["tab"],
            border_width=1,
            border_color=COLORS["border_soft"],
            fg_color=COLORS["panel"],
            hover_color=COLORS["panel_hi"],
            text_color=COLORS["text_dim"],
            font=FONTS["tab"],
            **kwargs,
        )
        self._active = False

    def set_active(self, active: bool) -> None:
        self._active = active
        if active:
            self.configure(
                fg_color=COLORS["accent_soft"],
                border_color=COLORS["accent"],
                text_color=COLORS["accent"],
            )
        else:
            self.configure(
                fg_color=COLORS["panel"],
                border_color=COLORS["border_soft"],
                text_color=COLORS["text_dim"],
            )


class ActionButton(ctk.CTkButton):
    """Standard action button (Encrypt, Decrypt, Swap, Clear, ...)."""

    VARIANTS = {
        "primary": {
            "fg_color": COLORS["accent"],
            "hover_color": COLORS["accent_hover"],
            "text_color": "#001712",
            "border_color": COLORS["accent_press"],
        },
        "secondary": {
            "fg_color": COLORS["panel_hi"],
            "hover_color": COLORS["border"],
            "text_color": COLORS["text"],
            "border_color": COLORS["border"],
        },
        "ghost": {
            "fg_color": "transparent",
            "hover_color": COLORS["panel_hi"],
            "text_color": COLORS["text_dim"],
            "border_color": COLORS["border"],
        },
    }

    def __init__(self, master, text: str, command, *, variant: str = "secondary", **kwargs):
        style = self.VARIANTS.get(variant, self.VARIANTS["secondary"])
        super().__init__(
            master,
            text=text,
            command=command,
            height=36,
            corner_radius=CORNER["button"],
            border_width=1,
            font=FONTS["button"],
            **style,
            **kwargs,
        )


class LabeledEntry(ctk.CTkFrame):
    """Single-line entry with a small label above it."""

    def __init__(self, master, label: str, *, placeholder: str = "", **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self._label_var = ctk.StringVar(value=label)
        ctk.CTkLabel(
            self,
            textvariable=self._label_var,
            font=FONTS["label_sm"],
            text_color=COLORS["text_muted"],
            anchor="w",
        ).grid(row=0, column=0, sticky="ew")

        self.entry = ctk.CTkEntry(
            self,
            placeholder_text=placeholder,
            height=34,
            corner_radius=CORNER["input"],
            border_width=1,
            border_color=COLORS["border"],
            fg_color=COLORS["bg_alt"],
            text_color=COLORS["text"],
            font=FONTS["mono_sm"],
        )
        self.entry.grid(row=1, column=0, sticky="ew", pady=(2, 0))

    def get(self) -> str:
        return self.entry.get()

    def set(self, value: str) -> None:
        self.entry.delete(0, "end")
        if value:
            self.entry.insert(0, value)

    def set_label(self, text: str) -> None:
        self._label_var.set(text)


class TextArea(ctk.CTkFrame):
    """Multi-line text box with a small label on top.

    With ``expand_height=True``, the textbox height tracks the frame height
    so the parent grid can split vertical space without a page-level scroll.
    """

    def __init__(
        self,
        master,
        label: str,
        *,
        height: int = 140,
        expand_height: bool = False,
        monospace: bool = True,
        **kwargs,
    ):
        super().__init__(master, fg_color="transparent", **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self._expand_height = expand_height
        self._min_tb_height = 56
        self._last_applied_h: int | None = None

        self._label = ctk.CTkLabel(
            self,
            text=label,
            font=FONTS["label_sm"],
            text_color=COLORS["text_muted"],
            anchor="w",
        )
        self._label.grid(row=0, column=0, sticky="ew")

        init_h = max(self._min_tb_height, height) if expand_height else height
        self.textbox = ctk.CTkTextbox(
            self,
            height=init_h,
            corner_radius=CORNER["input"],
            border_width=1,
            border_color=COLORS["border"],
            fg_color=COLORS["bg_alt"],
            text_color=COLORS["text"],
            font=FONTS["mono"] if monospace else FONTS["body"],
            wrap="word",
        )
        self.textbox.grid(row=1, column=0, sticky="nsew", pady=(2, 0))

        if expand_height:
            self.bind("<Configure>", self._on_configure)

    def _on_configure(self, event) -> None:
        if event.widget is not self:
            return
        self.after_idle(self._sync_textbox_height)

    def _sync_textbox_height(self) -> None:
        try:
            h = self.winfo_height()
            if h <= 1:
                return
            label_h = self._label.winfo_reqheight() + 6
            new_h = max(self._min_tb_height, h - label_h)
            if self._last_applied_h is not None and abs(new_h - self._last_applied_h) <= 2:
                return
            self._last_applied_h = new_h
            self.textbox.configure(height=int(new_h))
        except Exception:
            pass

    def get(self) -> str:
        return self.textbox.get("1.0", "end").rstrip("\n")

    def set(self, value: str) -> None:
        self.textbox.delete("1.0", "end")
        if value:
            self.textbox.insert("1.0", value)

    def clear(self) -> None:
        self.textbox.delete("1.0", "end")


class StatusPanel(ctk.CTkFrame):
    """Compact feedback area shown in the lower part of the sidebar."""

    LEVELS = {
        "info":    COLORS["info"],
        "success": COLORS["success"],
        "warn":    COLORS["warning"],
        "error":   COLORS["danger"],
        "muted":   COLORS["text_muted"],
    }

    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            fg_color=COLORS["panel"],
            border_color=COLORS["border"],
            border_width=1,
            corner_radius=CORNER["panel"],
            **kwargs,
        )
        self.grid_columnconfigure(0, weight=1)

        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew",
                    padx=PAD["md"], pady=(PAD["sm"], 0))
        header.grid_columnconfigure(1, weight=1)

        self._dot = ctk.CTkLabel(
            header,
            text="●",
            font=("Segoe UI", 12),
            text_color=COLORS["text_muted"],
        )
        self._dot.grid(row=0, column=0, padx=(0, PAD["xs"]))

        ctk.CTkLabel(
            header,
            text="STATUS",
            font=FONTS["h2"],
            text_color=COLORS["text"],
            anchor="w",
        ).grid(row=0, column=1, sticky="w")

        self._cipher_label = ctk.CTkLabel(
            self,
            text="—",
            font=FONTS["label_sm"],
            text_color=COLORS["text_dim"],
            anchor="w",
            justify="left",
        )
        self._cipher_label.grid(
            row=1, column=0, sticky="ew",
            padx=PAD["md"], pady=(PAD["sm"], 0),
        )

        self._message_label = ctk.CTkLabel(
            self,
            text="Ready.",
            font=FONTS["status"],
            text_color=COLORS["text_dim"],
            anchor="w",
            justify="left",
            wraplength=210,
        )
        self._message_label.grid(
            row=2, column=0, sticky="ew",
            padx=PAD["md"], pady=(PAD["xs"], PAD["md"]),
        )

    def set_cipher(self, name: str) -> None:
        self._cipher_label.configure(text=f"Active: {name}")

    def set(self, message: str, level: str = "info") -> None:
        color = self.LEVELS.get(level, COLORS["text_dim"])
        self._dot.configure(text_color=color)
        self._message_label.configure(text=message, text_color=color)
