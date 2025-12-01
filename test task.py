# Подключаем selenium
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

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
        footer = driver.find_element(By.XPATH, "//footer[contains(@class, 'Footer')]")
        print("Футер найден")

        # Поиск кнопки внутри футера
        try:
            button = footer.find_element(By.XPATH, ".//button[contains(@class, 'StartProjectButton_root')]")
            print("Кнопка 'Начать проект' найдена")
        except NoSuchElementException:
            print("Кнопка 'Начать проект' не найдена")

        # Поиск ссылки внутри футера
        try:
            link = footer.find_element(By.XPATH, ".//a[contains(@href, 'mailto:hello@only.digital')]")
            print("Ссылка на эл.почту найдена")
        except NoSuchElementException:
            print("Ссылка на эл.почту внутри футера отсутствует")

    except NoSuchElementException:
        print("Футер не найден")

# Закрытие браузер
driver.quit()