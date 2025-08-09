import streamlit as st
import streamlit_hotkeys as hotkeys
from hotkeys_config import activate_hotkeys

hotkeys.preload_css(key="global")

with st.sidebar:
    activate_hotkeys()

st.title("Editor")

st.text_area("Document", height=200, key="doc")

if hotkeys.pressed("save_cmd") or hotkeys.pressed("save_ctrl"):
    st.success("Document saved")

if hotkeys.pressed("palette_mac") or hotkeys.pressed("palette_win"):
    st.info("Open editor palette")
