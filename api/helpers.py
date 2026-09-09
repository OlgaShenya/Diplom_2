"""Вспомогательные функции для работы с API клиентами."""

import uuid


def generate_unique_email(domain: str = "yandex.ru") -> str:
    """
    Генерирует уникальный email для тестов.
    
    Args:
        domain: доменное имя для email (по умолчанию yandex.ru)
    
    Returns:
        Строка с уникальным email адресом
    """
    unique_id = uuid.uuid4().hex[:10]
    return f"test_{unique_id}@{domain}"
