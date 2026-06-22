import requests
from .helpers import generate_unique_email


class UserAPI:
    """Клиент для работы с API пользователей Stellar Burgers."""

    def __init__(self, base_url="https://stellarburgers.education-services.ru"):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def generate_unique_email(self, domain="yandex.ru"):
        """Генерация уникального email для тестов."""
        return generate_unique_email(domain)

    def create_user(self, email, password, name):
        """POST /api/auth/register"""
        data = {"email": email, "password": password, "name": name}
        return self.session.post(f"{self.base_url}/api/auth/register", json=data)

    def login_user(self, email, password):
        """POST /api/auth/login"""
        data = {"email": email, "password": password}
        return self.session.post(f"{self.base_url}/api/auth/login", json=data)

    def update_user(self, access_token=None, email=None, name=None):
        """PATCH /api/auth/user"""
        headers = {}
        if access_token is not None:
            headers["Authorization"] = access_token
        data = {}
        if email is not None:
            data["email"] = email
        if name is not None:
            data["name"] = name
        return self.session.patch(f"{self.base_url}/api/auth/user", json=data, headers=headers)

    def delete_user(self, access_token):
        """DELETE /api/auth/user"""
        headers = {"Authorization": access_token}
        return self.session.delete(f"{self.base_url}/api/auth/user", headers=headers)
