import platform
import os

binaries = [("./nwjs-v0.30.1-win-ia32.zip", ".")]
if platform.system() == "Darwin":
    binaries = [("./nwjs-v0.30.1-osx-x64.zip", ".")]
a = Analysis(['./main.py'],
             binaries=binaries)


exe_portable = EXE(
    PYZ(a.pure),
    a.scripts,
    a.binaries,
    a.datas,
    name=os.path.join('build\\', "pywebpoc-portable.exe"),
    debug=True,
    strip=None,
    upx=False,
    console=True)
