# streamlit_hotkeys/__init__.py
from __future__ import annotations

from .manager import hk, activate, pressed, preload_css

__all__ = ["hk", "activate", "pressed", "preload_css"]
__version__ = "0.3.0"
