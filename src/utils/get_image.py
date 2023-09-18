import os


def get_last_progress_bar_image():
    dir_path = 'generated_images'

    most_recent_file = max(os.listdir(
        dir_path), key=lambda f: os.path.getmtime(os.path.join(dir_path, f)))

    return os.path.join(dir_path, most_recent_file)
