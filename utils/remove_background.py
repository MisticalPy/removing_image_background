from PIL import Image
from rembg import remove
import os


def remove_img_background(name_file):
    input_img = f'output_frames/{name_file}'
    output_img = f'source/1{name_file}'

    open_image = Image.open(input_img)
    output = remove(open_image)

    output.save(output_img)


def iter_files_in_folder(folder_path='./output_frames'):
    """
    Итерируется по всем файлам в указанной папке.

    Args:
      folder_path: Путь к папке.
    """
    for filename in os.listdir(folder_path):
        remove_img_background(filename)
