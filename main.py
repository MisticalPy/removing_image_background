import os
from utils import split_gif_cadrs, combining_frames_into_gif
from utils.remove_background import iter_files_in_folder


def start_process(start_gif_name, end_gif_name):
    os.makedirs('output_frames', exist_ok=True)
    os.makedirs('source', exist_ok=True)
    split_gif_cadrs.split_gif(start_gif_name, 'output_frames')
    iter_files_in_folder('./output_frames')
    combining_frames_into_gif.create_gif(end_gif_name, )


if __name__ == "__main__":
    start_process('gogojo.gif', 'done21.gif')
