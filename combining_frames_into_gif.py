from PIL import Image
import os


def create_gif(image_folder, output_path, duration=50):
    """
    Создает GIF-анимацию из изображений в указанной папке.

    Args:
        image_folder: Путь к папке с изображениями.
        output_path: Путь для сохранения GIF.
        duration: Задержка между кадрами в миллисекундах.
    """
    images = []
    for filename in sorted(os.listdir(image_folder)):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(image_folder, filename)
            img = Image.open(img_path)
            images.append(img)

    if images:
        images[0].save(output_path, save_all=True,
                       append_images=images[1:], duration=duration, loop=0)
        print(f"GIF создан: {output_path}")
    else:
        print(f"В папке {image_folder} не найдены изображения.")


# Пример использования
image_folder = 'output_frames'  # Папка с изображениями
output_gif = 'output.gif'  # Имя выходного файла
create_gif(image_folder, output_gif, duration=50)
