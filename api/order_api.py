import requests
from .endpoints import Endpoints


class OrderAPI:
    """Клиент для работы с API заказов и ингредиентов Stellar Burgers."""

    def __init__(self, base_url="https://stellarburgers.education-services.ru"):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def get_ingredients(self):
        """
        GET /api/ingredients
        Получение списка ингредиентов (нужен для получения валидного _id в тестах)
        """
        return self.session.get(f"{self.base_url}{Endpoints.GET_INGREDIENTS}")

    def create_order(self, ingredients, access_token=None):
        """
        POST /api/orders
        Создание заказа. Требует список ID ингредиентов и опционально токен авторизации.
        """
        headers = {}
        if access_token is not None:
            headers["Authorization"] = access_token
            
        return self.session.post(
            f"{self.base_url}{Endpoints.CREATE_ORDER}",
            json={"ingredients": ingredients},
            headers=headers
        )

    def get_user_orders(self, access_token=None):
        """
        GET /api/orders
        Получение заказов конкретного пользователя. Без токена вернет 401.
        """
        headers = {}
        if access_token is not None:
            headers["Authorization"] = access_token
            
        return self.session.get(
            f"{self.base_url}{Endpoints.GET_ORDERS}",
            headers=headers
        )
