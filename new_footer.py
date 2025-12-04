from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Запуск браузера
driver = webdriver.Chrome()

# Список страниц для проверки
pages = [
    "https://only.digital",
    "https://only.digital/projects",
    "https://only.digital/company",
    "https://only.digital/fields",
    "https://only.digital/job",
    "https://only.digital/blog",
    "https://only.digital/contacts"
]

# Перебор страниц
for url in pages:
    driver.get(url)
    print(f"\nПроверка страницы: {url}")

    # Поиск футера на странице
    try:
        footer = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//footer[contains(@class, 'Footer')]"))
        )
        print("Футер найден")
    except TimeoutException:
        raise AssertionError(f"Футер не найден {url}")

    # Поиск кнопки внутри футера
    try:
        button = footer.find_element(By.XPATH, ".//button[contains(@class, 'StartProjectButton_root')]")
        print("Кнопка 'Начать проект' найдена")
    except NoSuchElementException:
        raise AssertionError(f"Кнопка 'Начать проект' не найдена {url}")

    # Поиск ссылки внутри футера
    try:
        footer.find_element(By.XPATH, ".//a[contains(@href, 'mailto:hello@only.digital')]")
        print("Ссылка на эл.почту найдена")
    except NoSuchElementException:
        raise AssertionError(f"Ссылка на эл.почту не найдена {url}")

# Закрытие браузерf
driver.quit()
print("\nВсе страницы успешно прошли проверку")
