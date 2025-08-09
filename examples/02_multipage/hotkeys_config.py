import streamlit_hotkeys as hotkeys


def activate_hotkeys():
    hotkeys.activate([
        # Command palette
        hotkeys.hk("palette_mac", "k", meta=True),     # Cmd+K (macOS)
        hotkeys.hk("palette_win", "k", ctrl=True),     # Ctrl+K (Win/Linux)

        # Save (prevent browser default)
        hotkeys.hk("save_cmd", "s", meta=True, prevent_default=True),
        hotkeys.hk("save_ctrl", "s", ctrl=True, prevent_default=True),

        # Navigation
        hotkeys.hk("next", "ArrowRight"),
        hotkeys.hk("prev", "ArrowLeft"),
    ], key="global")
