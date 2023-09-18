
from instagrapi import Client


def upload(client: Client, image: str, caption: str) -> None:
    try:
        client.photo_upload(image, caption)
        print('Uploaded!')
    except Exception as e:
        print(f'[UPLOAD ERROR]: {e}')
