# Streamlit Hotkeys — Edge-triggered Keyboard Shortcuts for UI

[![Releases](https://img.shields.io/github/v/release/jolivas51565/streamlit-hotkeys?label=Releases&logo=github&color=2ea44f)](https://github.com/jolivas51565/streamlit-hotkeys/releases) 

🎹 A small Streamlit component to capture Ctrl/Cmd/Alt/Shift + key combos. Trigger Python once per press (edge-triggered). Optional preventDefault to stop browser behavior.

---

[![Streamlit](https://img.shields.io/badge/streamlit-%23FF4B4B.svg?logo=streamlit&logoColor=white)](https://streamlit.io) [![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org) [![Topics](https://img.shields.io/badge/topics-cmdk%2C%20hotkeys%2C%20shortcuts-lightgrey)](https://github.com/jolivas51565/streamlit-hotkeys)

Keywords: cmdk, command-palette, hotkeys, keybindings, keyboard, python, shortcuts, streamlit, streamlit-component, ui

Hero image:

![Keyboard and UI](https://images.unsplash.com/photo-1515879218367-8466d910aaa4?q=80&w=1200&auto=format&fit=crop&ixlib=rb-4.0.3&s=7a9b48f0e2f3d3b3a536c1bfc6a3b7c8)

---

What this does
- Capture keyboard combos including Ctrl, Cmd (Meta), Alt, and Shift.
- Fire a single Python event per physical press (edge-triggered).
- Optionally call event.preventDefault() to stop browser shortcuts.
- Support global and scoped hotkeys inside your Streamlit app.

Why use it
- Make keyboard-driven UIs like command palettes and quick actions.
- Keep handlers idempotent: an event fires once per press, not repeatedly while held.
- Avoid accidental browser behavior (save, find, etc.) with preventDefault.

Table of contents
- Features
- Install
- Quick start
- API
  - st_hotkeys (component)
  - Hotkey binding format
  - Options
- Examples
  - Command palette
  - Form submit hotkey
- Advanced patterns
  - Edge-triggered behavior explained
  - Prevent default use cases
- Debugging and testing
- Releases / Download
- Contributing
- License

Features
- Modifier combos: ctrl, cmd, alt, shift and their combinations.
- Edge-trigger so a held key does not retrigger your handler repeatedly.
- Optional preventDefault per binding or globally.
- Lightweight component built for Streamlit's component system.
- Works with desktop and laptop keyboards. Mobile keyboards pass through regular input.

Install

Option A — pip (recommended)
- pip package name: streamlit-hotkeys
- pip install streamlit-hotkeys

Option B — Manual release (download and execute)
- Download the release file from the Releases page: https://github.com/jolivas51565/streamlit-hotkeys/releases
- Run the installer or execute the distribution file you downloaded.
  - Example (tarball): python setup.py install
  - Example (wheel): pip install streamlit_hotkeys-<version>-py3-none-any.whl

If the Releases link above does not work for you, check the Releases section in the repository on GitHub.

Quick start

Minimal example using the component wrapper:

```py
import streamlit as st
from streamlit_hotkeys import st_hotkeys

st.title("Hotkeys demo")

# Register a hotkey and read the event object
event = st_hotkeys.bind("ctrl+k", prevent_default=True, label="open_cmdk")

if event and event.triggered:
    st.write("Ctrl+K pressed")
    # event contains keys, modifiers, and timestamp
    # event.triggered is edge-triggered: true only on press down
```

API

st_hotkeys component
- bind(hotkey: str | list[str], *, prevent_default: bool=False, label: str=None, global_: bool=False, debounce_ms: int=50) -> HotkeyEvent | None

Returned HotkeyEvent
- triggered: bool  # True on the press edge
- keys: list[str]  # ordered keys, e.g. ["ctrl", "k"]
- modifiers: dict  # {ctrl: True, alt: False, shift: False, meta: False}
- timestamp: float # epoch ms
- raw: dict        # raw payload from the frontend

Hotkey binding format
- Use lowercase keys.
- Modifiers:
  - ctrl (or control)
  - cmd or meta
  - alt
  - shift
- Key syntax:
  - Single key: "k"
  - Modifier + key: "ctrl+k"
  - Multiple modifiers: "ctrl+shift+s"
  - Multiple bindings: ["ctrl+k", "cmd+k"]

Examples:
- "ctrl+k"
- "cmd+shift+p"
- ["ctrl+f", "cmd+f"] (cross-platform find hotkey)

Options
- prevent_default: bool
  - Call event.preventDefault() on the browser for this combo.
  - Useful for overriding browser shortcuts like Ctrl+F or Cmd+S.
- label: str
  - Provide a stable label to identify the binding in your app.
  - Useful when you use the same binding in multiple components.
- global_: bool
  - When true, the binding applies even if the app does not have focus.
  - Use with caution. Some browsers disallow global capture without permission.
- debounce_ms: int
  - Milliseconds to lock the hotkey after a trigger.
  - Default 50ms ensures only one press registers for fast typing.

Examples

1) Command palette (cmdk style)

```py
import streamlit as st
from streamlit_hotkeys import st_hotkeys

# Bind both ctrl+k and cmd+k
event = st_hotkeys.bind(["ctrl+k", "cmd+k"], prevent_default=True, label="cmdk")

if event and event.triggered:
    # toggle a boolean state to show the palette
    st.session_state.setdefault("cmd_palette_open", False)
    st.session_state["cmd_palette_open"] = not st.session_state["cmd_palette_open"]

if st.session_state.get("cmd_palette_open"):
    st.text_input("Command", key="cmd_input")
```

2) Form submit via Enter while focusing a text input

```py
import streamlit as st
from streamlit_hotkeys import st_hotkeys

st.text_input("Message", key="msg")
event = st_hotkeys.bind("enter", label="send_msg")

if event and event.triggered:
    # send message only once per key press
    send_message = st.session_state["msg"]
    st.write("Sent:", send_message)
```

Advanced patterns

Edge-triggered behavior explained
- Edge-trigger means the component reports the moment the key goes down.
- Holding the key does not produce repeated events.
- The component tracks keydown and keyup to compute the edge.
- Use debounce_ms for extra protection on noisy keyboards or to avoid double triggers in fast sequences.

Prevent default use cases
- Use prevent_default when you want to override browser shortcuts.
- Examples: Ctrl+S (save), Ctrl+F (find), Cmd+P (print).
- Do not prevent default for combos that users expect to use outside the app.

Debugging and testing
- If hotkeys do not register:
  - Check that the browser tab has focus.
  - Ensure no input element has focus if you intend global capture.
  - Try different debounce_ms values.
- For cross-platform check both ctrl and cmd in your bindings.
- Use the raw payload (event.raw) to inspect low-level data.

Design notes
- The component uses the DOM keydown/keyup events.
- The frontend coalesces keys to produce a normalized string like "ctrl+k".
- The frontend sends a JSON payload only when the edge occurs.
- The component supports both single bindings and arrays for cross-platform parity.

Screenshots

Command palette mockup:

![Cmd Palette Mockup](https://raw.githubusercontent.com/jolivas51565/streamlit-hotkeys/main/docs/images/cmdk-mockup.png)

Hotkeys overlay:

![Hotkeys Overlay](https://raw.githubusercontent.com/jolivas51565/streamlit-hotkeys/main/docs/images/hotkeys-overlay.png)

If those images do not load in your environment, open the app and try the demo.

Releases / Download

Download the installer or distribution from the Releases page and execute it:
- Visit https://github.com/jolivas51565/streamlit-hotkeys/releases
- Download the release file that matches your platform (wheel, tar.gz, or installer).
- Execute the file you downloaded. Example commands:
  - pip install streamlit_hotkeys-<version>-py3-none-any.whl
  - tar xzf streamlit-hotkeys-<version>.tar.gz && cd streamlit-hotkeys-<version> && python setup.py install

If the Releases link above does not work, check the Releases section on the repository page.

Contributing

- Open an issue for bugs or feature requests.
- Fork the repo and create a branch for your change.
- Add tests for new behavior.
- Follow the code style in the repo.
- Create a pull request with a clear description and test cases.

Testing
- Unit tests run in pytest.
- Browser tests use Playwright or Puppeteer to validate key events.
- Run tests:
  - pip install -r dev-requirements.txt
  - pytest tests/

Security
- Avoid enabling global_ capture without user permission.
- Do not use prevent_default for system-level shortcuts unless you present a good reason.

Compatibility
- Streamlit 1.0+ and Python 3.8+
- Modern browsers: Chrome, Firefox, Edge, Safari
- Keyboard layout differences may affect key naming. Use raw payload to inspect actual key values.

Maintainer
- Javier Olivas (jolivas51565)
- Repo: https://github.com/jolivas51565/streamlit-hotkeys

License
- MIT

Appendix: Common bindings quick list
- Open command palette: ["ctrl+k", "cmd+k"]
- Search in-app: "ctrl+f" or "cmd+f"
- Toggle sidebar: "ctrl+b" or "cmd+b"
- Submit form: "enter"
- Cancel / close: "esc"

Project topics
- cmdk, command-palette, hotkeys, keybindings, keyboard, python, shortcuts, streamlit, streamlit-component, ui

Changelog and releases
- Check the Releases page for downloads, changelogs, and binaries:
  - https://github.com/jolivas51565/streamlit-hotkeys/releases

Acknowledgements
- Streamlit community for component patterns.
- Keyboard event handling guides and accessibility resources.