import streamlit as st
import streamlit_hotkeys as hotkeys

st.title("Basic hotkeys (manager API)")

# Activate the single manager once (ideally near app start)
hotkeys.activate([
    hotkeys.hk("plain_k", "k"),
    hotkeys.hk("open_palette_mac", "k", meta=True),   # Cmd+K (macOS)
    hotkeys.hk("open_palette_win", "k", ctrl=True),   # Ctrl+K (Windows/Linux)
    hotkeys.hk("enter", "Enter"),
], key="global")

if hotkeys.pressed("plain_k"):
    st.success("You pressed: K")

if hotkeys.pressed("open_palette_mac") or hotkeys.pressed("open_palette_win"):
    st.info("Open palette")

if hotkeys.pressed("enter"):
    st.write("Enter pressed")
