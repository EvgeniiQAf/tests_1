# src/client/favqs_client.py

import requests

from src.config import BASE_URL, API_KEY


class FavQsClient:
    def __init__(self):
        self.base_headers = {
            "Authorization": f'Token token="{API_KEY}"',
            "Content-Type": "application/json",
        }

    def create_user(self, payload: dict):
        return requests.post(
            url=f"{BASE_URL}/users",
            json=payload,
            headers=self.base_headers,
        )

    def get_user(self, login: str, user_token: str):
        headers = {
            **self.base_headers,
            "User-Token": user_token,
        }
        return requests.get(
            url=f"{BASE_URL}/users/{login}",
            headers=headers,
        )

    def update_user(self, login: str, user_token: str, payload: dict):
        headers = {
            **self.base_headers,
            "User-Token": user_token,
        }
        return requests.put(
            url=f"{BASE_URL}/users/{login}",
            json=payload,
            headers=headers,
        )
