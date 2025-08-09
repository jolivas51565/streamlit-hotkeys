import streamlit as st
import streamlit_hotkeys as hotkeys
from hotkeys_config import activate_hotkeys

# PRELOAD CSS *first* — before any other UI
hotkeys.preload_css(key="global")

with st.sidebar:
    activate_hotkeys()

st.title("Home")

if hotkeys.pressed("palette_mac") or hotkeys.pressed("palette_win"):
    st.info("Open command palette (Home)")

# You can react to global bindings on any page
if hotkeys.pressed("save_cmd") or hotkeys.pressed("save_ctrl"):
    st.success("Saved from Home")

st.write("Go to the pages in the left sidebar.")
