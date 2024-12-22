# pyVTAC

Data manipulation with Tkinter TTK and Pandas.

## Build

To compile to `.exe` with internal directory, run from root:

`python -m PyInstaller src/main.py -n pyVTAC.exe --log-level ERROR --onedir --clean`

For a single `.exe` file for production, run from root:

`python -m PyInstaller src/main.py -n pyVTAC.exe --log-level ERROR --onefile --clean`

`.exe` and other files will be in the `/dist` folder.
