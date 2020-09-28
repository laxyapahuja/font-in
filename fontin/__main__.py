import os
import tempfile
import sys
import time
import ctypes
from pyunpack import Archive
import time

from fontin.install_font import install_font
from fontin import clear, is_admin

ALLFILES = os.listdir()
FILE = ''
TEMPDIR = tempfile.gettempdir()

archive_extensions = ('.7z', '.ace', '.alz', '.a', '.arc', '.arj', '.bz2', '.cab', '.Z', '.cpio', '.deb', '.dms', '.gz', '.lrz', '.lha', '.lzh', 
'.lz', '.lzma', '.lzo', '.rpm', '.rar', '.rz', '.tar', '.xz', '.zip', '.jar', '.zoo')

font_file_extensions = ('.ttf', '.otf', '.svg', '.eot', '.woff')

def find_archives():
    archives = []
    print('Searching for archives in the current directory...')
    for file in ALLFILES:
        if file.endswith(archive_extensions):
            archives.append(file)
    clear()
    print('Found the following files:')
    n=1
    for archive in archives:
        print('{}. {}'.format(str(n), archive))
        n += 1
    choice = input('Choose the font archives (Separated by commas[,]/ all): ')
    files = []
    if choice == 'all':
        files = archives
    else:
        choices = choice.split(',')
        for choic in choices:
            choic = choic.strip()
            files.append(archives[int(choic) - 1])
    return files

def extract(files):
    print('Extracting...')
    paths = []
    for file in files:
        extracted_path = TEMPDIR + '\\fontin\\' + file + '\\'
        if not os.path.exists(extracted_path):
            os.makedirs(extracted_path)
        Archive(os.getcwd() + '\\' + file).extractall(extracted_path)
        paths.append(extracted_path)
    return paths

def install_all(paths):
    for path in paths:
        fonts = os.listdir(path)
        for font in fonts:
            if font.endswith(font_file_extensions):
                font_path = path + '\\' + font
                print('Installing font: ' + font)
                install_font(font_path)

def main():
    if is_admin():
        file = find_archives()
        path = extract(file)
        install_all(path)
        print('Close? [y/n]')
        n = input().lower()
        if n == 'y':
            sys.exit()
        else:
            main()
    else:
        print('Please run the program as administrator.')

if __name__ == '__main__':
    main()