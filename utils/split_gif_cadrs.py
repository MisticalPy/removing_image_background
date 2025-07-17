from PIL import Image
import os


def split_gif(gif_path, output_dir='output_frames'):
    """
    Разбивает GIF-файл на отдельные кадры и сохраняет их в указанную директорию.

    Args:
        gif_path (str): Путь к GIF-файлу.
        output_dir (str): Путь к директории, куда будут сохранены кадры.
    """
    try:
        gif = Image.open(gif_path)
    except FileNotFoundError:
        print(f"Ошибка: Файл не найден: {gif_path}")
        return
    except Exception as e:
        print(f"Ошибка при открытии GIF: {e}")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        for i in range(gif.n_frames):
            gif.seek(i)
            frame = gif.copy()
            # Сохраняем как PNG, можно выбрать другой формат
            frame.save(os.path.join(output_dir, f"frame_{i:04d}.png"), "PNG")
    except EOFError:
        pass  # Закончились кадры
    except Exception as e:
        print(f"Ошибка при сохранении кадра: {e}")

    print(f"GIF успешно разделен на кадры в {output_dir}")
