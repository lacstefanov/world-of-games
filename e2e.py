from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_score_service(url):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--remote-debugging-port=9222')

    # Set up Chrome service
    service = ChromeService(executable_path='/usr/local/bin/chromedriver')

    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)
        score_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "score")))
        score_text = score_element.text
        score = int(score_text)
        is_within_range = 1 <= score <= 1000
        return is_within_range
    finally:
        driver.quit()


url = "http://127.0.0.1:5001/"
result = test_score_service(url)
print("Score is within range: ", result)