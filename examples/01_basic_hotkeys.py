import streamlit as st
import streamlit_hotkeys as hotkeys


hotkeys.activate([
    hotkeys.hk("palette", "k", meta=True, help="Open palette (mac)"),
    hotkeys.hk("palette", "k", ctrl=True, help="Open palette (win/linux)"),
    hotkeys.hk("save", "s", ctrl=True, prevent_default=True, help="Save"),
    hotkeys.hk("show_legend", "?", shift=True, help="Show shortcuts"),
], key="global")


def save():
    st.toast("Saved!")


if hotkeys.pressed("save"):
    st.info("Thank you for saving")

hotkeys.on_pressed("save", save)


@hotkeys.on_pressed("palette")
def open_palette():
    st.info("Palette opened")


@st.dialog("Keyboard Shortcuts")
def _shortcuts_dialog():
    hotkeys.legend()


if hotkeys.pressed("show_legend"):
    _shortcuts_dialog()

st.write("Press Cmd/Ctrl+K, Ctrl+S or Shift+?")