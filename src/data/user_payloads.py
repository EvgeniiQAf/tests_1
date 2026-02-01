def create_user_payload(login: str, email: str):
    return {
        "user": {
            "login": login,
            "email": email,
            "password": "Password123!"
        }
    }


def update_user_payload(new_login: str, new_email: str):
    return {
        "user": {
            "login": new_login,
            "email": new_email,
        }
    }
