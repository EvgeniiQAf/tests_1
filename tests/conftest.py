import sys
from pathlib import Path
import uuid
import pytest
from src.client.favqs_client import FavQsClient
from src.data.user_payloads import create_user_payload, update_user_payload
from src.utils.statuses import HTTP_OK

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))


@pytest.fixture(scope="session")
def client():
    return FavQsClient()


@pytest.fixture
def created_user(client):
    login = f"user_{uuid.uuid4().hex[:6]}"
    email = f"{login}@test.com"

    response = client.create_user(
        create_user_payload(login, email)
    )
    assert response.status_code == HTTP_OK

    data = response.json()

    return {
        "client": client,
        "login": login,
        "email": email,
        "user_token": data["User-Token"],
        "response": data,
    }


@pytest.fixture
def updated_user(client, created_user):
    old_login = created_user["login"]
    user_token = created_user["user_token"]

    new_login = f"{old_login}_upd"
    new_email = f"{new_login}@upd.com"

    response = client.update_user(
        old_login,
        user_token,
        update_user_payload(new_login, new_email)
    )
    assert response.status_code == HTTP_OK

    return {
        "client": client,
        "login": new_login,
        "email": new_email,
        "user_token": user_token,
        "response": response.json(),
    }
