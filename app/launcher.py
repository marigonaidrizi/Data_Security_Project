
from __future__ import annotations

from .styles import apply_theme


def run() -> None:
    apply_theme()

    from .main_window import MainWindow

    app = MainWindow()
    app.mainloop()
