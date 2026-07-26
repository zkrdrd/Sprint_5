import pytest
from selenium import webdriver

from helpers import URLData


@pytest.fixture
def web_driver():
    """Фикстура для инициализации и завершения работы драйвера."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.get(URLData.BASE_URL)
    yield driver
    driver.quit()
