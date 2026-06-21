import pytest
import jsonschema
from schemas import SUCCESS_AUTH_SCHEMA, SUCCESS_UPDATE_SCHEMA, ERROR_SCHEMA


class TestCreateUser:
    """Тесты для создания пользователя."""
    
    def test_create_unique_user(self, user_api):
        email = user_api.generate_unique_email()
        response = user_api.create_user(email, "password123", "TestUser")
        data = response.json()
        
        assert (
            response.status_code == 200 and 
            jsonschema.validate(instance=data, schema=SUCCESS_AUTH_SCHEMA) is None and 
            data["user"]["email"] == email
        )

    def test_create_existing_user(self, user_api, existing_user):
        response = user_api.create_user(existing_user["email"], existing_user["password"], existing_user["name"])
        data = response.json()
        
        assert (
            response.status_code == 403 and 
            jsonschema.validate(instance=data, schema=ERROR_SCHEMA) is None and 
            data["message"] == "User already exists"
        )

    @pytest.mark.parametrize("missing_field", ["email", "password", "name"], ids=["no_email", "no_password", "no_name"])
    def test_create_user_missing_required_field(self, user_api, missing_field):
        full_data = {"email": "test@yandex.ru", "password": "password123", "name": "TestUser"}
        del full_data[missing_field]
        
        response = user_api.session.post(f"{user_api.base_url}/api/auth/register", json=full_data)
        data = response.json()
        
        assert (
            response.status_code == 403 and 
            jsonschema.validate(instance=data, schema=ERROR_SCHEMA) is None and 
            data["message"] == "Email, password and name are required fields"
        )


class TestLoginUser:
    """Тесты для логина пользователя."""
    
    def test_login_existing_user(self, user_api, existing_user):
        response = user_api.login_user(existing_user["email"], existing_user["password"])
        data = response.json()
        
        assert (
            response.status_code == 200 and 
            jsonschema.validate(instance=data, schema=SUCCESS_AUTH_SCHEMA) is None and 
            data["user"]["email"] == existing_user["email"]
        )

    def test_login_with_wrong_credentials(self, user_api):
        response = user_api.login_user("wrong_email@yandex.ru", "wrong_password")
        data = response.json()
        
        assert (
            response.status_code == 401 and 
            jsonschema.validate(instance=data, schema=ERROR_SCHEMA) is None and 
            data["message"] == "email or password are incorrect"
        )


class TestUpdateUser:
    """Тесты для изменения данных пользователя."""
    
    @pytest.mark.parametrize("field, static_value", [
        ("name", "UpdatedName"),
        ("email", "placeholder")
    ], ids=["update_name_only", "update_email_only"])
    def test_update_user_field_with_auth(self, user_api, existing_user, field, static_value):

        unique_email = user_api.generate_unique_email()
        payload_value = {"email": unique_email, "name": static_value}[field]

        response = user_api.update_user(
            access_token=existing_user["access_token"], 
            **{field: payload_value}
        )
        data = response.json()
        
        assert (
            response.status_code == 200 and 
            jsonschema.validate(instance=data, schema=SUCCESS_UPDATE_SCHEMA) is None and 
            data["user"][field] == payload_value
        )

    @pytest.mark.parametrize("field, static_value", [
        ("name", "HackerName"),
        ("email", "placeholder")
    ], ids=["update_name_without_auth", "update_email_without_auth"])
    def test_update_user_field_without_auth(self, user_api, field, static_value):

        unique_email = user_api.generate_unique_email()
        payload_value = {"email": unique_email, "name": static_value}[field]

        response = user_api.update_user(**{field: payload_value})
        data = response.json()
        
        assert (
            response.status_code in (400, 401) and 
            jsonschema.validate(instance=data, schema=ERROR_SCHEMA) is None and 
            data["message"] == "You should be authorised"
        )
