# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['setiastrosuitemac.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('/Users/franklinmarek/cosmicclarity/env/lib/python3.12/site-packages/astroquery/CITATION', 'astroquery'),
        ('celestial_catalog.csv', '.'), 
        ('astrosuite.png', '.'), 
        ('wimilogo.png', '.'), 
        ('wrench_icon.png', '.'), 
        ('eye.png', '.'), 
        ('disk.png', '.'), 
        ('nuke.png', '.'), 
        ('hubble.png', '.'), 
        ('imgs', 'imgs'),
        ('collage.png', '.'), 
        ('annotated.png', '.'), 
        ('colorwheel.png', '.'), 
        ('font.png', '.'), 
        ('spinner.gif', '.'), 
        ('cvs.png', '.'), 
        ('/Users/franklinmarek/cosmicclarity/env/lib/python3.12/site-packages/astroquery/simbad/data', 'astroquery/simbad/data'), 
        ('/Users/franklinmarek/cosmicclarity/env/lib/python3.12/site-packages/astropy/CITATION', 'astropy')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['torch', 'torchvision'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='setiastrosuitemac',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # Enable terminal console
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['/Users/franklinmarek/cosmicclarity/astrosuite.icns'],
    onefile=True  # Enable single-file mode
)


