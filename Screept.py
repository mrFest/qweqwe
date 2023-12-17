from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def fetch_jar_data_selenium():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get("https://send.monobank.ua/jar/7bcFc8cDxg")
        time.sleep(5)  # Чекаємо, щоб сторінка завантажилася

        # Отримання значень за класом
        values = driver.find_elements(By.CLASS_NAME, "stats-data-value")
        if len(values) >= 2:
            jar_goal = values[0].text  # Перший елемент для jarGoal
            jar_amount = values[1].text  # Другий елемент для jarAmount
        else:
            print("Недостатньо елементів знайдено.")
            return None, None

        return jar_goal, jar_amount
    finally:
        driver.quit()

goal, amount = fetch_jar_data_selenium()
if goal and amount:
    print(f"Цільова сума: {goal}, Поточна сума: {amount}")
else:
    print("Помилка при отриманні даних.")
