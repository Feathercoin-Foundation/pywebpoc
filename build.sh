#!/bin/sh -x

NWJS_URL="https://dl.nwjs.io/v0.30.3/nwjs-v0.30.3-win-ia32.zip"
PYINSTALLER="wine c:/python3.5.4/scripts/pyinstaller.exe"
PYTHON="wine c:/python3.5.4/python.exe"
if [ "$(uname -s)" = "Darwin" ]; then
    NWJS_URL="https://dl.nwjs.io/v0.30.3/nwjs-v0.30.3-osx-x64.zip"
    PYINSTALLER=pyinstaller
    PYTHON=python
fi

if ! [ -f "$(basename $NWJS_URL)" ]; then
    wget "$NWJS_URL"
fi

$PYTHON setup.py install
$PYINSTALLER --asci --noconfirm pyi.spec
