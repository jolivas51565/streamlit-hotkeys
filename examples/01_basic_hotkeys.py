import streamlit as st
import streamlit_hotkeys as hotkeys

st.title("Basic hotkeys")

# Activate early
hotkeys.activate([
    hotkeys.hk("plain_k", "k", help="Show K message"),
    hotkeys.hk("open_palette", "k", meta=True, help="Open command palette"),
    hotkeys.hk("open_palette", "k", ctrl=True, help="Open command palette"),
    hotkeys.hk("enter", "Enter", help="Confirm / Run"),
    hotkeys.hk("show_legend", "?", shift=True, help="Show shortcuts"),
], key="global")

# Actions
if hotkeys.pressed("plain_k"):
    st.success("You pressed: K")

if hotkeys.pressed("open_palette"):
    st.info("Open palette")

if hotkeys.pressed("enter"):
    st.write("Enter pressed")


@st.dialog("Keyboard Shortcuts")
def _shortcuts_dialog():
    hotkeys.legend()


# Open with Shift+?
if hotkeys.pressed("show_legend"):
    _shortcuts_dialog()


# Optional button for mouse users
if st.button("See Shortcuts"):
    _shortcuts_dialog()
