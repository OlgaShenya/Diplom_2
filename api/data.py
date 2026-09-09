"""Test data and error messages for API tests."""


class ErrorMessages:
    """Error messages from API responses."""
    
    USER_ALREADY_EXISTS = "User already exists"
    REQUIRED_FIELDS = "Email, password and name are required fields"
    INVALID_CREDENTIALS = "email or password are incorrect"
    NOT_AUTHORIZED = "You should be authorised"
    INVALID_INGREDIENTS = "Ingredient ids must be provided"


class TestUserData:
    """Test data for user-related tests."""
    
    EMAIL = "test@yandex.ru"
    PASSWORD = "password123"
    NAME = "TestUser"
    UPDATED_NAME = "UpdatedName"
