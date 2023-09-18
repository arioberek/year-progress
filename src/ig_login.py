
from instagrapi import Client
import os
from dotenv import load_dotenv

load_dotenv()


def login():
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')
    if username is None or password is None:
        raise ValueError("Username or password environment variable not set")

    client = Client()
    client.login(username, password)

    return client
