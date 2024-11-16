import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Specify the interface language")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")  # Получаем значение языка из аргументов
    # Добавим обработку случая, когда пользователь не указывает язык интерфейса
    if not user_language:
        raise pytest.UsageError("--Specify the interface language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    # Инициализируем браузер
    browser = webdriver.Chrome(options=options)
    yield browser  # Возвращаем объект браузера для тестов
    browser.quit()  # Закрываем браузер после завершения теста
