import setuptools  # type: ignore

MAJOR, MINOR, PATCH = 0, 1, 0
VERSION = f"{MAJOR}.{MINOR}.{PATCH}"
"""This project uses semantic versioning.
Please consult the following page for more information:
    https://semver.org/
"""

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

extras_require = {"testing": ["nose"]}

setuptools.setup(
    name="walkman",
    version=VERSION,
    license="GPL",
    description="play audio files in performance contexts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Levin Eric Zimmermann",
    author_email="tim.pauli@folkwang-uni.de, levin.eric.zimmermann@posteo.eu",
    url="https://github.com/mutwo-org/mutwo",
    packages=["walkman"],
    setup_requires=[],
    install_requires=[
        # for audio
        "pyo==1.0.4",
        # for GUI
        "PySimpleGUI==4.60.0",
        # for CLI
        "click==8.1.3",
        # to read config files
        "tomlkit==0.10.2",
        # to catch keyboard input
        "pynput==1.7.6",
    ],
    extras_require=extras_require,
    python_requires="==3.8",
)
