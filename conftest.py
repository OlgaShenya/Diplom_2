import pytest
from api.user_api import UserAPI
from api.order_api import OrderAPI
from api.data import TestUserData


@pytest.fixture
def user_api():
    """Экземпляр API пользователей."""
    return UserAPI()

@pytest.fixture
def order_api():
    """Экземпляр API заказов."""
    return OrderAPI()


@pytest.fixture
def existing_user(user_api):
    """Создает пользователя, передает данные в тест и гарантированно удаляет его после."""
    email = user_api.generate_unique_email()
    response = user_api.create_user(email, TestUserData.PASSWORD, TestUserData.NAME)
    data = response.json()
    
    if not data.get("success"):
        raise RuntimeError(f"Setup failed: {data}")

    user_info = {
        "email": email,
        "password": TestUserData.PASSWORD,
        "name": TestUserData.NAME,
        "access_token": data["accessToken"]
    }
    
    yield user_info
    
    user_api.delete_user(user_info["access_token"])

@pytest.fixture
def valid_ingredient_id(order_api):
    """
    Динамически получает первый попавшийся валидный ID ингредиента с сервера.
    Это необходимо, чтобы тест 'с ингредиентами' использовал реальные данные.
    """
    response = order_api.get_ingredients()
    data = response.json()
    
    if response.status_code != 200 or not data.get("success"):
        raise RuntimeError(f"Не удалось получить ингредиенты для теста: {data}")
    
    return data["data"][0]["_id"]