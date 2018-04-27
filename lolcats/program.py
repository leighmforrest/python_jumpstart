import os
import cat_service
import platform
import subprocess


def main():
    # print the header
    print_header()
    # get or create output folder
    folder = get_or_create_output_folder()
    # download cats
    download_cats(folder)
    # display cats
    display_cats(folder)
    print('HELLO FROM MAIN')


def print_header():
    print('--------------------------------------------------')
    print("                   CAT FACTORY")
    print('--------------------------------------------------')
    print()


def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    full_path = os.path.join('.', folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print(f'Creating new directory at {full_path}')
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    print('Contacting server to download...')
    cat_count = 8

    for i in range(1, cat_count + 1):
        name = 'lolcat_{}'.format(i)
        cat_service.get_cat(folder, name)


def display_cats(folder):
    if platform.system() == 'Darwin':
        subprocess.call(['open', folder])
    else:
        print('Unable. Malfunction. Need input!')

if __name__ == '__main__':
    main()