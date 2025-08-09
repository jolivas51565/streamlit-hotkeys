import streamlit as st
import streamlit_hotkeys as hotkeys
from hotkeys_config import activate_hotkeys

hotkeys.preload_css(key="global")

with st.sidebar:
    activate_hotkeys()

st.title("Viewer")

images = [f"Image {i+1}" for i in range(5)]
st.session_state.setdefault("idx", 0)

if hotkeys.pressed("next"):
    st.session_state.idx = min(st.session_state.idx + 1, len(images) - 1)

if hotkeys.pressed("prev"):
    st.session_state.idx = max(0, st.session_state.idx - 1)

st.write(f"Current: {images[st.session_state.idx]}")
st.caption("Use ← / → to navigate. Cmd/Ctrl+K opens the palette. Cmd/Ctrl+S saves.")
