from sys import argv
from os import scandir, system, path
import time

def replace(str):
   return str.replace('\\', '/')

def implode(arr, sep = '/'):
    if len(arr) <= 1:
        arr = arr + ['']
    return sep.join(arr)

def save_last_pathsrc(src):
    file = open('history.txt', 'w')
    file.write(src)
    file.close()

def load_last_pathsrc():
    try:
        file = open('history.txt')
        src = file.read()
        file.close()
        print(['path', src])
        return None if src == '' else src
    except FileNotFoundError:
        print('history.txt not found!')
        file = open('history.txt', 'w+')
        file.close()
    return None

imageList = ['svg', 'jpg', 'gif', 'png', 'webp', 'jpeg', 'bmp', 'raw']
textList = ['txt', 'ini', 'inf', 'conf', 'cfg', 'md', 'env', 'htaccess', 'gitignore']
logList = ['log']
codeList = ['php', 'py', 'html', 'css', 'js', 'rsc', 'toml']
mediaList = ['wav', 'mp3', 'mp4', 'avi', 'ogg', 'mp2']
binList = ['bin', 'dll', 'dat']
exeList = ['exe', 'msi']
zipList = ['zip', '7z', 'arj', 'gz', 'tgz', 'rar', 'cab', 'pak', '001']
keyList = ['key']

groupList = {
    'I': imageList,
    'T': textList,
    'C': codeList,
    'L': logList,
    'M': mediaList,
    'B': binList,
    'X': exeList,
    'Z': zipList,
    'K': keyList
}

symbols = ['═╡', ' ├─ ', '─', '─┤', '□', '▪', '└─', '─┘', '│', ' ┬', '⌂', '☼']
elementSymbol = {'D': '⌂', 'I': '☼', 'T': '₸', 'M': '♫', 'B': '▒', 'X': '█', 'Z': 'Z'}
elementEmoji = {
    '.': '\U0001F0CF',
    '?': '\N{memo}',
    'D': '\N{open file folder}',
    'I': '\U0001F5BC',
    'T': '\N{page facing up}',
    'C': '\N{bookmark tabs}',
    'L': '\N{scroll}',
    'M': '\N{musical note}',
    'B': '\N{file cabinet}',
    'X': '\N{video game}', #'\U00002699',
    'Z': '\N{package}',
    'K': '\U0001F512',
}

last_pathsrc = load_last_pathsrc()
path_src = replace("C:/Users/Public") if last_pathsrc == None else last_pathsrc
if len(argv) > 1:
    path_src = replace(argv[1])

path_list = []
for particle in path_src.split('/'):
    if not particle == '':
        path_list.append(particle)

def check_directory(src_path, tmp):
    try:
        scandir(implode(src_path))
        return src_path
    except PermissionError:
        print(symbols[0], "❌  Brak dostępu do katalogu:", src_path)
    except FileNotFoundError:
        print(symbols[0], "👻  Katalog nie istnieje:", src_path)
    except Exception as e:
        print(symbols[0], "💀  Wystąpił nieoczekiwany błąd:", e)
    return tmp


def get_icon_element(obj):
    symbol = symbols[2]
    if obj.is_dir():
        return elementEmoji['D'] or symbols[10]
    elif obj.is_file():
        file = obj.name.split('.')
        ext = file[-1]
        icon = elementEmoji['.'] 
        for list in groupList:
            if ext in groupList[list]:
                icon = elementEmoji[list]
        return icon
    return symbol

def dir_element(index, name, len, fileIcon):
    print('{s1}{: >{n}} {s2} {: <{m}} {s3}'.format(index, name, n = len, m = 48, s1 = symbols[1], s2 = fileIcon, s3 = symbols[3]))

def txt_element(index, name, len, *args):
    print(' {s1} {: >{n}} {s2} {: <{m}} {s3}'.format(index, name, n = len, m = 48, s1 = args[0], s2 = args[1], s3 = args[2]))

def dir_count_file(path):
    scan = scandir(implode(path))
    file_count = 0
    for obj in scan:
        file_count += 1
    return len(str(file_count))

def dir_show_elements(path):
    i = 0
    elements = []
    src_path = implode(path)
    len_max_count_number = dir_count_file(path)
    if len(path) > 1:
        dir_element(0, '..', len_max_count_number, elementEmoji['D'] or symbols[10])
    for obj in scandir(src_path):
        i += 1
        dir_element(i, obj.name, len_max_count_number, get_icon_element(obj))
        elements.append(obj)
    txt_element(symbols[4], 'Choose file or directory:', len_max_count_number, symbols[6], elementEmoji['?'] or symbols[2], symbols[7])
    return elements

def main():
    global path_list
    file_name = False
    tmp_path_list = path_list
    while True:
        system('cls')
        print(f"{symbols[9]} 💾  SIMPLE FILE MANAGER 💾")
        file_name = True
        if path.isdir(implode(path_list)):
            path_list = check_directory(path_list, tmp_path_list)
            save_last_pathsrc(implode(path_list))
            print(f" {symbols[8]} Start a path directory:")
            print(symbols[0], implode(path_list))
            file_name = False

        if file_name == True:
            print('import file_reader;', path_list, implode(path_list))
            import file_reader
            file_reader.main(implode(path_list), [symbols[0]])
            del file_reader
            txt_element(symbols[4], 'Choose [0 - exit]:', 30, symbols[6], elementEmoji['?'] or symbols[2], symbols[7])
        else:
            dir_elements = dir_show_elements(path_list)
  
        key_file = input('') or -1
        
        if not key_file.isnumeric() or int(key_file) <= -1:
            print('Close Program > exit')
            break

        if int(key_file) == 0:
            print('Change Directory > cd ..')
            tmp_path_list = path_list
            path_list = path_list[:-1]
        else:
            key = int(key_file) - 1
            if dir_elements[key].is_dir():
                print('Change Directory > cd', dir_elements[key].name)
                tmp_path_list = list(path_list)
                path_list.append(dir_elements[key].name)
            else:
                file_name = dir_elements[key].name
                path_list.append(file_name)
            print(dir_elements[key])

if __name__ == '__main__':
    main()
