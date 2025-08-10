import streamlit as st
import streamlit_hotkeys as hotkeys

st.title("Hold ArrowDown to increment")

hotkeys.activate([
    hotkeys.hk("down", "ArrowDown", ignore_repeat=False),
])

st.session_state.setdefault("count", 0)

if hotkeys.pressed("down"):
    st.session_state["count"] += 1

st.metric("Count", st.session_state["count"])
st.caption("Hold ArrowDown to spam events (ignore_repeat=False)")