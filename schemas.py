SUCCESS_AUTH_SCHEMA = {
    "type": "object",
    "required": ["success", "accessToken", "refreshToken", "user"],
    "properties": {
        "success": {"type": "boolean", "const": True},
        "accessToken": {"type": "string"},
        "refreshToken": {"type": "string"},
        "user": {
            "type": "object",
            "required": ["email", "name"],
            "properties": {
                "email": {"type": "string"},
                "name": {"type": "string"}
            },
            "additionalProperties": False
        }
    },
    "additionalProperties": False
}

SUCCESS_UPDATE_SCHEMA = {
    "type": "object",
    "required": ["success", "user"],
    "properties": {
        "success": {"type": "boolean", "const": True},
        "user": {
            "type": "object",
            "required": ["email", "name"],
            "properties": {
                "email": {"type": "string"},
                "name": {"type": "string"}
            },
            "additionalProperties": False
        }
    },
    "additionalProperties": False
}

# ==============================================================================
# СХЕМЫ ДЛЯ ЗАКАЗОВ И ИНГРЕДИЕНТОВ (Order API)
# ==============================================================================

# Схема для ответа GET /api/ingredients (нужна для надежности фикстуры valid_ingredient_id)
INGREDIENTS_SUCCESS_SCHEMA = {
    "type": "object",
    "required": ["success", "data"],
    "properties": {
        "success": {"type": "boolean", "const": True},
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["_id", "name", "type"],
                "properties": {
                    "_id": {"type": "string"},
                    "name": {"type": "string"},
                    "type": {"type": "string"}
                },
                "additionalProperties": False
            }
        }
    },
    "additionalProperties": False
}

# Схема для успешного создания заказа POST /api/orders (200 OK)
CREATE_ORDER_SUCCESS_SCHEMA = {
    "type": "object",
    "required": ["success", "name", "order"],
    "properties": {
        "success": {"type": "boolean", "const": True},
        "name": {"type": "string"},
        "order": {
            "type": "object",
            "required": ["number"],
            "properties": {
                "number": {"type": "integer"}
            }
        }
    },
    "additionalProperties": False
}

# Схема для успешного получения заказов GET /api/orders (200 OK)
GET_ORDERS_SUCCESS_SCHEMA = {
    "type": "object",
    "required": ["success", "orders", "total", "totalToday"],
    "properties": {
        "success": {"type": "boolean", "const": True},
        "orders": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["_id", "status", "number", "createdAt", "updatedAt", "ingredients"],
                "properties": {
                    "_id": {"type": "string"},
                    "status": {"type": "string"},
                    "number": {"type": "integer"},
                    "createdAt": {"type": "string"},
                    "updatedAt": {"type": "string"},
                    "ingredients": {
                        "type": "array",
                        "items": {"type": "string"}
                    }
                },
                "additionalProperties": False
            }
        },
        "total": {"type": "integer"},
        "totalToday": {"type": "integer"}
    },
    "additionalProperties": False
}

# ==============================================================================
# УНИВЕРСАЛЬНАЯ СХЕМА ОШИБОК (400, 401, 403)
# ==============================================================================

ERROR_SCHEMA = {
    "type": "object",
    "required": ["success", "message"],
    "properties": {
        "success": {"type": "boolean", "const": False},
        "message": {"type": "string"}
    },
    "additionalProperties": False
}