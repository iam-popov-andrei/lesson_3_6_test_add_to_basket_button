from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def test_add_to_basket_button(browser):
    # Открываем страницу с товаром
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    try:
        # Ждем, пока кнопка 'Добавить в корзину' не станет видимой
        button = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket"))
        )
        # Проверяем наличие кнопки
        assert button
        print("Кнопка 'Добавить в корзину' найдена")
    except TimeoutException:
        # В случае, если кнопка не была найдена тест проваливается
        pytest.fail("Не удалось найти кнопку 'Добавить в корзину' за отведенное время.")
    finally:
        time.sleep(30)
        browser.quit()
