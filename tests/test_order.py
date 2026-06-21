import pytest
import jsonschema
from schemas import CREATE_ORDER_SUCCESS_SCHEMA, GET_ORDERS_SUCCESS_SCHEMA, ERROR_SCHEMA


class TestCreateOrder:
    """Тесты для создания заказов."""
    
    def test_create_order_with_auth_and_valid_ingredients(self, order_api, existing_user, valid_ingredient_id):
        """Создание заказа с авторизацией и валидными ингредиентами."""
        response = order_api.create_order(
            ingredients=[valid_ingredient_id], 
            access_token=existing_user["access_token"]
        )
        data = response.json()
        
        assert (
            response.status_code == 200 and
            jsonschema.validate(instance=data, schema=CREATE_ORDER_SUCCESS_SCHEMA) is None
        )

    def test_create_order_without_auth(self, order_api, valid_ingredient_id):
        """Создание заказа без авторизации."""
        response = order_api.create_order(ingredients=[valid_ingredient_id])
        data = response.json()
        
        assert (
            response.status_code == 200 and
            jsonschema.validate(instance=data, schema=CREATE_ORDER_SUCCESS_SCHEMA) is None
        )

    def test_create_order_without_ingredients(self, order_api, existing_user):
        """Создание заказа без ингредиентов."""
        response = order_api.create_order(
            ingredients=[], 
            access_token=existing_user["access_token"]
        )
        data = response.json()
        
        assert (
            response.status_code == 400 and 
            jsonschema.validate(instance=data, schema=ERROR_SCHEMA) is None and 
            data["message"] == "Ingredient ids must be provided"
        )

    def test_create_order_with_invalid_ingredient_hash(self, order_api, existing_user):
        """Создание заказа с неверным хешем ингредиентов."""
        response = order_api.create_order(
            ingredients=["invalid_hash_12345"], 
            access_token=existing_user["access_token"]
        )
        
        assert response.status_code == 500


class TestGetUserOrders:
    """Тесты для получения заказов пользователя."""

    def test_get_user_orders_authorized(self, order_api, existing_user):
        """Получение заказов авторизованным пользователем."""
        response = order_api.get_user_orders(access_token=existing_user["access_token"])
        data = response.json()
        
        assert (
            response.status_code == 200 and
            jsonschema.validate(instance=data, schema=GET_ORDERS_SUCCESS_SCHEMA) is None
        )

    def test_get_user_orders_unauthorized(self, order_api):
        """Получение заказов неавторизованным пользователем."""
        response = order_api.get_user_orders()
        data = response.json()
        
        assert (
            response.status_code == 401 and
            jsonschema.validate(instance=data, schema=ERROR_SCHEMA) is None and
            data.get("message") == "You should be authorised"
        )
