

from __future__ import annotations

APP_TITLE = "Cipher Console"

WINDOW_MIN_SIZE = (960, 560)
WINDOW_DEFAULT_SIZE = (1080, 620)

SIDEBAR_WIDTH = 250

COLORS = {
    "bg":            "#0B0F14",
    "bg_alt":        "#0F141B",
    "panel":         "#121821",
    "panel_alt":     "#161D27",
    "panel_hi":      "#1B2330",
    "border":        "#1F2A36",
    "border_soft":   "#172029",

    "text":          "#E6F1FF",
    "text_dim":      "#9AB0C4",
    "text_muted":    "#5C7187",

    "accent":        "#00E5C7",
    "accent_hover":  "#1FF2D6",
    "accent_press":  "#00B89F",
    "accent_soft":   "#0E2F2C",

    "danger":        "#FF6B6B",
    "warning":       "#FFC857",
    "success":       "#5BE7A9",
    "info":          "#7FB3FF",
}

FONTS = {
    "title":     ("Segoe UI Semibold", 16),
    "subtitle":  ("Segoe UI", 11),
    "h1":        ("Segoe UI Semibold", 18),
    "h2":        ("Segoe UI Semibold", 13),
    "label":     ("Segoe UI", 11),
    "label_sm":  ("Segoe UI", 10),
    "body":      ("Segoe UI", 11),
    "mono":      ("Cascadia Mono", 12),
    "mono_sm":   ("Cascadia Mono", 11),
    "tab":       ("Segoe UI Semibold", 12),
    "button":    ("Segoe UI Semibold", 12),
    "status":    ("Segoe UI", 10),
}

PAD = {
    "xs": 4,
    "sm": 8,
    "md": 12,
    "lg": 16,
    "xl": 22,
}

CORNER = {
    "panel": 10,
    "button": 8,
    "tab": 8,
    "input": 8,
}


def apply_theme() -> None:
    """Configure CustomTkinter global appearance once at startup."""
    import customtkinter as ctk

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
