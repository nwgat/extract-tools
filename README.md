# isoextract
simple script to extract files from iso

# Install
* `wget https://raw.githubusercontent.com/nwgat/isoextract/main/isoextract`
* `install isoextract /usr/bin`
* `isoextract file.iso` (the files will extract to the same location as the iso file)


# .py to executable
pip install pyinstaller
cd /path/to/your/program
pyinstaller --onefile yourscript.py
