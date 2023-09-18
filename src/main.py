from ig_login import login
from utils.get_image import get_last_progress_bar_image
from media_upload import upload
from year_progress_percentage import year_progress_percentage
from generate_progress_bar import create_progress_image


def main():
    try:
        print('Starting...')

        print('Creating progress image...')
        percentage = year_progress_percentage()
        create_progress_image(percentage)
        print(f'Progress image created: {percentage:.0f}%')

        print('Logging in...')
        client = login()
        print('Logged in.')

        print('Uploading progress image...')

        image = get_last_progress_bar_image()
        upload(client=client, image=image, caption=f'{percentage:.0f}%')

        print('Progress image uploaded.')
    except Exception as e:
        print(f'[ERROR]: {e}')


if __name__ == '__main__':
    main()
