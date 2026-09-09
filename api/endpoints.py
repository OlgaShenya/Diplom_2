"""API endpoints for Stellar Burgers."""


class Endpoints:
    """Collection of all API endpoints."""
    
    # Auth endpoints
    REGISTER = "/api/auth/register"
    LOGIN = "/api/auth/login"
    UPDATE_USER = "/api/auth/user"
    DELETE_USER = "/api/auth/user"
    
    # Orders endpoints
    GET_INGREDIENTS = "/api/ingredients"
    CREATE_ORDER = "/api/orders"
    GET_ORDERS = "/api/orders"
