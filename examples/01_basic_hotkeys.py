import streamlit as st
from streamlit_hotkeys import keyboard_input

st.title("Basic Hotkeys")

st.write("Try these:")
st.write("- K")
st.write("- Ctrl+K (Windows/Linux)")
st.write("- Cmd+K (macOS)")
st.write("- Enter")

if keyboard_input("k", widget_key="plain-k"):
    st.success("You pressed: K")

if keyboard_input("k", ctrl=True, widget_key="ctrl-k"):
    st.success("Ctrl+K detected")

if keyboard_input("k", meta=True, widget_key="cmd-k"):
    st.success("Cmd+K detected")

if keyboard_input("Enter", widget_key="enter"):
    st.success("Enter pressed")
