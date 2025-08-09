import os
import streamlit.components.v1 as components


_parent = os.path.dirname(os.path.abspath(__file__))
_build_dir = os.path.join(_parent, "component")
_key_component = components.declare_component("key_press_listener", path=_build_dir)


def keyboard_input(key: str,
                   *,
                   alt: bool | None = False,
                   ctrl: bool | None = False,
                   shift: bool | None = False,
                   meta: bool | None = False,
                   use_code: bool = False,
                   ignore_repeat: bool = True,
                   prevent_default: bool = False,
                   widget_key: str | None = None) -> bool:
    """
    Return True exactly once when the specified key combo is pressed.

    Args:
        key: Key to match (e.g., "k", "Enter", "Escape", "ArrowLeft").
        alt/ctrl/shift/meta:
            True=require pressed, False=forbid (default), None=ignore.
            Use meta=True for Cmd on macOS (or Windows key on Windows).
        use_code: Match KeyboardEvent.code (e.g., "KeyK") instead of .key.
        ignore_repeat: Ignore auto-repeat while key is held.
        prevent_default: Prevent browser default on match (e.g., Ctrl+S).
        widget_key: Optional Streamlit widget key (for multiple listeners).

    Example:
        if keyboard_input("k", ctrl=True):
            st.write("Ctrl+K")

        # Cmd/Ctrl+Enter (allow either by using meta=True on mac; provide two listeners if needed)
        if keyboard_input("Enter", meta=True):
            st.write("Cmd+Enter")
    """
    # NOTE: do not pass param named "key" to the component (reserved as widget key)
    pulse = _key_component(
        targetKey=key,
        alt=alt, ctrl=ctrl, shift=shift, meta=meta,
        useCode=use_code,
        ignoreRepeat=ignore_repeat,
        preventDefault=prevent_default,
        default=False,          # edge-trigger default
        key=widget_key,         # Streamlit widget key
    )
    return bool(pulse)
