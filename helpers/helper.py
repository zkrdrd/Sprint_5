from random import choices
from string import ascii_lowercase, digits


def unique_email() -> str:
    """Генерация уникального email для теста."""
    random_part = "".join(choices(ascii_lowercase + digits, k=8))
    return f"testuser_{random_part}@example.com"
