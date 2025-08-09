(() => {
  let config = {
    targetKey: null,      // e.g. "k", "Enter", "Escape", "ArrowLeft"
    alt: false,           // True=require, False=forbid, null/undefined=ignore
    ctrl: false,
    shift: false,
    meta: false,          // Cmd on macOS / Win key on Windows
    useCode: false,       // if True, match e.code (e.g. "KeyK") instead of e.key
    ignoreRepeat: true,   // ignore auto-repeat while key is held
    preventDefault: false // prevent browser default on match (e.g., Ctrl+S)
  };

  function normalizeKey(k) {
    if (k == null) return null;
    const s = String(k);
    const lower = s.toLowerCase();
    const map = {
      esc: "Escape", escape: "Escape",
      " ": " ", space: " ",
      enter: "Enter", return: "Enter",
      tab: "Tab",
      up: "ArrowUp", down: "ArrowDown", left: "ArrowLeft", right: "ArrowRight",
      cmd: "Meta", command: "Meta", win: "Meta", meta: "Meta",
      control: "Control", ctrl: "Control",
      alt: "Alt", option: "Alt",
      shift: "Shift"
    };
    if (map[lower] !== undefined) return map[lower];
    if (s.length === 1) return lower; // compare letters case-insensitively
    return s;
  }

  function modOk(need, have) {
    if (need === null || need === undefined) return true; // don't care
    return (!!have) === (!!need);
  }

  function matches(e) {
    if (config.ignoreRepeat && e.repeat) return false;

    const desired = normalizeKey(config.targetKey);
    if (!desired) return false;

    const actual = config.useCode ? e.code : e.key;
    const actualNorm = config.useCode ? actual : normalizeKey(actual);

    const sameKey = config.useCode
      ? actualNorm === desired
      : (desired.length === 1
          ? (typeof actualNorm === "string" && actualNorm.length === 1 && actualNorm.toLowerCase() === desired)
          : actualNorm === desired);

    if (!sameKey) return false;
    if (!modOk(config.ctrl, e.ctrlKey)) return false;
    if (!modOk(config.alt, e.altKey)) return false;
    if (!modOk(config.shift, e.shiftKey)) return false;
    if (!modOk(config.meta, e.metaKey)) return false;

    return true;
  }

  function onKeyDown(e) {
    if (matches(e)) {
      if (config.preventDefault) e.preventDefault();
      Streamlit.setComponentValue(true); // edge-triggered pulse
    }
  }

  // Attach global listener once per iframe
  window.addEventListener("load", () => {
    window.parent.document.addEventListener("keydown", onKeyDown);
    Streamlit.setComponentReady();
    Streamlit.setComponentValue(null); // clear on init
  });

  // Receive args from Python on each render
  Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, (event) => {
    const args = event.detail.args || {};
    config = {
      targetKey: args.targetKey ?? args.key ?? config.targetKey,
      alt: args.alt ?? false,
      ctrl: args.ctrl ?? false,
      shift: args.shift ?? false,
      meta: args.meta ?? false,
      useCode: args.useCode ?? false,
      ignoreRepeat: args.ignoreRepeat ?? true,
      preventDefault: args.preventDefault ?? false
    };
    // Clear the last pulse so it doesn't stick across reruns
    Streamlit.setComponentValue(null);
    Streamlit.setFrameHeight(0);
  });

  window.addEventListener("beforeunload", () => {
    window.parent.document.removeEventListener("keydown", onKeyDown);
  });
})();
