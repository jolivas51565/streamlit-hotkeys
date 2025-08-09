import streamlit as st
from streamlit_hotkeys import keyboard_input

st.title("Command Palette (Cmd/Ctrl+K)")

# State
st.session_state.setdefault("palette_open", False)
st.session_state.setdefault("palette_query", "")
st.session_state.setdefault("palette_index", 0)

# Open palette with Cmd+K or Ctrl+K
if keyboard_input("k", meta=True, widget_key="open-cmdk") or keyboard_input("k", ctrl=True, widget_key="open-ctrlk"):
    st.session_state.palette_open = True
    st.session_state.palette_index = 0

# Demo commands
COMMANDS = [
    "Open Settings",
    "Toggle Dark Mode",
    "New File",
    "Open File",
    "Save",
    "Run All Cells",
    "Show Shortcuts",
    "Reload App",
]

def search(q: str):
    q = (q or "").strip().lower()
    if not q:
        return COMMANDS
    return [c for c in COMMANDS if q in c.lower()]

def render_results(results, index):
    for i, cmd in enumerate(results):
        prefix = "→ " if i == index else "  "
        st.write(f"{prefix}{cmd}")

# Close palette with Esc
if st.session_state.palette_open and keyboard_input("Escape", widget_key="palette-esc"):
    st.session_state.palette_open = False

# Navigation inside palette
if st.session_state.palette_open and keyboard_input("ArrowDown", widget_key="palette-down"):
    st.session_state.palette_index = min(st.session_state.palette_index + 1, max(0, len(search(st.session_state.palette_query)) - 1))

if st.session_state.palette_open and keyboard_input("ArrowUp", widget_key="palette-up"):
    st.session_state.palette_index = max(0, st.session_state.palette_index - 1)

# Confirm with Enter
if st.session_state.palette_open and keyboard_input("Enter", widget_key="palette-enter"):
    results = search(st.session_state.palette_query)
    if results:
        chosen = results[st.session_state.palette_index]
        st.success(f"Executed: {chosen}")
    st.session_state.palette_open = False

# UI
if st.session_state.palette_open:
    st.info("Palette open (Esc to close, ↑/↓ to navigate, Enter to run)")
    st.session_state.palette_query = st.text_input("Type a command", value=st.session_state.palette_query, key="palette-input")
    results = search(st.session_state.palette_query)
    st.write("Results:")
    render_results(results, st.session_state.palette_index)
else:
    st.write("Press Cmd+K (mac) or Ctrl+K (win/linux) to open the palette.")
