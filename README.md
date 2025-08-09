# streamlit-hotkeys

[![PyPI](https://img.shields.io/pypi/v/streamlit-hotkeys.svg)](https://pypi.org/project/streamlit-hotkeys/)
[![Python Versions](https://img.shields.io/pypi/pyversions/streamlit-hotkeys.svg)](https://pypi.org/project/streamlit-hotkeys/)
[![License](https://img.shields.io/pypi/l/streamlit-hotkeys.svg)](LICENSE)
[![Wheel](https://img.shields.io/pypi/wheel/streamlit-hotkeys.svg)](https://pypi.org/project/streamlit-hotkeys/)
![Streamlit Component](https://img.shields.io/badge/streamlit-component-FF4B4B?logo=streamlit\&logoColor=white)
[![Downloads](https://static.pepy.tech/badge/streamlit-hotkeys)](https://pepy.tech/project/streamlit-hotkeys)

Keyboard hotkeys for Streamlit - capture `Ctrl/Cmd/Alt/Shift + key` anywhere in your app and trigger Python once per press (edge-triggered). Uses a single invisible manager component.

**Important:** call `activate(...)` as early as possible in each page. Activation injects CSS that collapses the manager iframe, which avoids layout flicker.

---

## Installation

```bash
pip install streamlit-hotkeys
```

## Quick start

```python
import streamlit as st
import streamlit_hotkeys as hotkeys

st.set_page_config(page_title="Hotkeys Demo")

# Activate early so the manager is hidden from the first frame
hotkeys.activate([
    hotkeys.hk("palette_mac", "k", meta=True),                # Cmd+K (macOS)
    hotkeys.hk("palette_win", "k", ctrl=True),                # Ctrl+K (Windows/Linux)
    hotkeys.hk("save", "s", ctrl=True, prevent_default=True), # Ctrl+S (block browser save)
    hotkeys.hk("down", "ArrowDown"),
], key="global")

st.title("Hotkeys demo")

if hotkeys.pressed("palette_mac") or hotkeys.pressed("palette_win"):
    st.success("Open palette")

if hotkeys.pressed("save"):
    st.success("Saved!")

if hotkeys.pressed("down"):
    st.write("Move selection down")
```

### Multi-page tip

In multi-page apps, call `activate(...)` near the top of **every page**, or from a small helper module that each page imports. Example layout:

```
streamlit_app/
├─ app.py
├─ hotkeys_config.py
└─ pages/
   ├─ 01_Editor.py
   └─ 02_Viewer.py
```

`hotkeys_config.py`

```python
import streamlit_hotkeys as hotkeys

def activate_hotkeys():
    hotkeys.activate([
        hotkeys.hk("palette_mac", "k", meta=True),
        hotkeys.hk("palette_win", "k", ctrl=True),
        hotkeys.hk("save_cmd", "s", meta=True, prevent_default=True),
        hotkeys.hk("save_ctrl", "s", ctrl=True, prevent_default=True),
        hotkeys.hk("next", "ArrowRight"),
        hotkeys.hk("prev", "ArrowLeft"),
    ], key="global")
```

Use on any page:

```python
import streamlit as st
import streamlit_hotkeys as hotkeys
from hotkeys_config import activate_hotkeys

activate_hotkeys()  # as early as possible

st.title("Editor")

if hotkeys.pressed("save_cmd") or hotkeys.pressed("save_ctrl"):
    st.success("Saved")
```

![Demo Usage](docs/image.png)

## Features

* Single invisible manager iframe that handles many bindings at once.
* Edge-triggered events - exactly once per press.
* Modifiers: `ctrl`, `alt`, `shift`, `meta` (Cmd on macOS).
* Optional `preventDefault` for browser-owned shortcuts (for example, `Ctrl/Cmd+S`).
* `KeyboardEvent.code` support (layout-independent physical keys).
* `ignore_repeat` to suppress repeated events while a key is held.

## API

### `hk(...)` - define a binding

```python
hk(
  id: str,
  key: str | None = None,           # for example, "k", "Enter", "ArrowDown"
  *,
  code: str | None = None,          # for example, "KeyK" (if set, 'key' is ignored)
  alt: bool | None = False,         # True=require, False=forbid, None=ignore
  ctrl: bool | None = False,
  shift: bool | None = False,
  meta: bool | None = False,
  ignore_repeat: bool = True,
  prevent_default: bool = False,
) -> dict
```

### `activate(*bindings, key="global", debug=False) -> None`

Register bindings and render the single manager. Accepts `hk(...)` dicts, a list of them, or a mapping `id -> spec`.

### `pressed(id, *, key="global") -> bool`

Return `True` exactly once when the binding `id` fires.

## Examples

* Command palette (`Cmd/Ctrl+K`) with arrow navigation and Enter to confirm.
* Save shortcut (`Ctrl/Cmd+S`) with `prevent_default=True`.
* Physical key binding via `code="KeyY"` regardless of layout.

See the `examples/` folder for complete scripts.

## Notes and limitations

* Browsers reserve some shortcuts. Use `prevent_default=True` to keep the event for your app when allowed.
* Combos mean modifiers + one key. The platform does not treat two non-modifier keys pressed together (for example, `A+S`) as a single combo.
* The page must have focus; events are captured at the document level.

## Similar projects

* [streamlit-keypress] - Original "keypress to Python" component by Sudarsan.
* [streamlit-shortcuts] - Keyboard shortcuts for buttons and widgets; supports multiple bindings and hints.
* [streamlit-keyup] - Text input that emits on every keyup (useful for live filtering).
* [keyboard\_to\_url (streamlit-extras)][keyboard_to_url (streamlit-extras)] - Bind a key to open a URL in a new tab.

[streamlit-keypress]: https://pypi.org/project/streamlit-keypress/
[streamlit-shortcuts]: https://pypi.org/project/streamlit-shortcuts/
[streamlit-keyup]: https://pypi.org/project/streamlit-keyup/
[keyboard_to_url (streamlit-extras)]: https://arnaudmiribel.github.io/streamlit-extras/extras/keyboard_url/

## Credits

Inspired by [streamlit-keypress] by **Sudarsan**. This implementation adds a multi-binding manager, edge-triggered events, modifier handling, `preventDefault`, and `KeyboardEvent.code`.

## Contributing

Issues and PRs are welcome.

## License

MIT. See `LICENSE`.
