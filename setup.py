import pathlib
import setuptools

HERE = pathlib.Path(__file__).parent
readme_path = HERE / "README.md"
long_description = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""

setuptools.setup(
    # ---- Distribution metadata ----
    name="streamlit-hotkeys",
    version="0.1.0",
    description="Keyboard hotkeys for Streamlit (Ctrl/Cmd/Alt/Shift combos) with edge-triggered events.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    license_files=["LICENSE"],

    # ---- Project metadata ----
    author="Viktor Shcherbakov",
    author_email="viktoroo.sch@gmail.com",
    maintainer="Viktor Shcherbakov",
    maintainer_email="viktoroo.sch@gmail.com",
    url="https://github.com/viktor-shcherb/streamlit-hotkeys",
    project_urls={
        "Source": "https://github.com/viktor-shcherb/streamlit-hotkeys",
        "Issue Tracker": "https://github.com/viktor-shcherb/streamlit-hotkeys/issues",
        "Similar: streamlit-keypress": "https://pypi.org/project/streamlit-keypress/",
        "Similar: streamlit-shortcuts": "https://pypi.org/project/streamlit-shortcuts/",
        "Similar: streamlit-keyup": "https://pypi.org/project/streamlit-keyup/",
        "Similar: keyboard_to_url (streamlit-extras)": "https://arnaudmiribel.github.io/streamlit-extras/extras/keyboard_url/",
    },
    keywords=["streamlit", "hotkeys", "shortcuts", "keyboard", "keypress", "component"],

    # ---- Packages & data ----
    packages=setuptools.find_packages(exclude=("examples", "docs", "tests")),
    include_package_data=True,  # use MANIFEST.in if you prefer
    package_data={
        # ship the front-end assets inside your Python package
        "streamlit_hotkeys": ["component/*"],   # e.g., index.html, index.js, streamlit-component-lib.js
    },

    # ---- Requirements ----
    python_requires=">=3.8",
    install_requires=[
        "streamlit>=1.25.0",
    ],

    # ---- Trove classifiers ----
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
    ],
)
