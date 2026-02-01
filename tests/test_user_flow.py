from src.utils.statuses import HTTP_OK


def test_create_and_get_user(client, created_user):
    """
    Create a user and retrieve it via GET.
    Validate returned login and API behavior for email field.
    """

    login = created_user["login"]
    email = created_user["email"]
    user_token = created_user["user_token"]

    # --- Validate CREATE response ---
    assert created_user["response"]["login"] == login
    assert "email" not in created_user["response"]

    print(
        f"[CREATE USER] sent_login='{login}', sent_email='{email}', "
        f"api_response={created_user['response']}"
    )

    # --- Get user ---
    get_response = client.get_user(login, user_token)
    assert get_response.status_code == HTTP_OK

    data = get_response.json()

    # --- Validate GET response ---
    assert data["login"] == login
    assert "email" not in data

    print(
        f"[GET USER] login='{data['login']}', "
        f"email_field_present={'email' in data}, "
        f"api_response={data}"
    )


def test_update_user(client, updated_user):
    """
    Update existing user and verify updated fields via GET.
    """

    new_login = updated_user["login"]
    new_email = updated_user["email"]
    user_token = updated_user["user_token"]

    print(
        f"[UPDATE USER] login updated to='{new_login}', "
        f"email sent='{new_email}', "
        f"api_response={updated_user['response']}"
    )

    # --- Get updated user ---
    get_response = client.get_user(new_login, user_token)
    assert get_response.status_code == HTTP_OK

    data = get_response.json()

    # --- Validate updated data ---
    assert data["login"] == new_login
    assert "email" not in data
