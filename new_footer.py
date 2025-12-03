from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# список ошибок
errors = []

# страницы для поиска
pages = [
    "https://only.digital",
    "https://only.digital/projects",
    "https://only.digital/company",
    "https://only.digital/fields",
    "https://only.digital/job",
    "https://only.digital/blog",
    "https://only.digital/contacts"
]

for url in pages:
    driver.get(url)
    print(f"\nПроверка страницы: {url}")

    # ожидание загрузки футера
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//footer[contains(@class, 'Footer')]"))
    )
    # проверяем наличие футера
    try:
        footer = driver.find_element(By.XPATH, "//footer[contains(@class, 'Footer')]")
        print("Футер найден")

        # проверяем наличие кнопки в футере
        try:
            button = footer.find_element(By.XPATH, ".//button[contains(@class, 'StartProjectButton_root')]")
            print("Кнопка 'Начать проект' найдена")
        except NoSuchElementException:
            msg = f"Кнопка 'Начать проект' не найдена на странице {url}"
            print(msg)
            errors.append(msg)

        # проверяем наличие ссылки в футере
        try:
            link = footer.find_element(By.XPATH, ".//a[contains(@href, 'mailto:hello@only.digital')]")
            print("Ссылка на эл.почту найдена")
        except NoSuchElementException:
            msg = f"Ссылка на эл.почту не найдена на странице {url}"
            print(msg)
            errors.append(msg)

    except NoSuchElementException:
        msg = f"Футер не найден на странице {url}"
        print(msg)
        errors.append(msg)

driver.quit()

print("\n=== РЕЗУЛЬТАТ ТЕСТА ===")
if errors:
    print("НАЙДЕНЫ ОШИБКИ:")
    for err in errors:
        print(" -", err)
else:
    print("Все проверки пройдены успешно")