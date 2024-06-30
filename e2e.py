import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

url = os.getenv('APP_URL', 'http://localhost:8777/')
def test_score_service(url):
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")

    chrome_binary_path = '/opt/google/chrome/chrome'
    service = Service(ChromeDriverManager().install())
    chrome_options.binary_location = chrome_binary_path
    driver = webdriver.Chrome(service=service, options=chrome_options)
    print(driver)

    try:
        driver.get(url)
        score_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "score")))
        score_text = score_element.text
        score = int(score_text)
        is_within_range = 1 <= score <= 1000
        return is_within_range
    finally:
        driver.quit()

container_id = os.getenv('CONTAINER_ID')
if container_id:
    url = f"http://{container_id}:8777/"
    result = test_score_service(url)
    print("Score is within range: ", result)
else:
    print("Container ID not found. Test cannot be executed.")