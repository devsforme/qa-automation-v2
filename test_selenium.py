from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import tempfile

def test_google_title():
    options = Options()
    options.add_argument("--headless=new")  # Headless режим для CI
    options.add_argument("--no-sandbox")  # Рекомендуется для GitHub Actions
    options.add_argument("--disable-dev-shm-usage")  # Для избежания shared memory проблем
    options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")  # Уникальный профиль

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()
