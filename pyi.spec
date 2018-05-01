import platform
import os

binaries = [("./nwjs-v0.30.1-win-ia32.zip", ".")]
name = os.path.join('build\\', "pywebpoc.exe")
if platform.system() == "Darwin":
    binaries = [("./nwjs-v0.30.1-osx-x64.zip", ".")]
    name = "pywebpoc"
a = Analysis(['./main.py'],
             binaries=binaries)


exe = EXE(
    PYZ(a.pure),
    a.scripts,
    a.binaries,
    a.datas,
    name=name,
    debug=True,
    strip=None,
    upx=False,
    console=True)

if platform.system() == "Darwin":
    BUNDLE(exe,
           version='0.0.0',
           name='pywebpoc.app',
           bundle_identifier=None,
           info_plist={
              'NSHighResolutionCapable': 'True',
              'NSSupportsAutomaticGraphicsSwitching': 'True'
           }
           )
