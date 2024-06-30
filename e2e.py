from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_score_service(url):
    chrome_driver_path = "/usr/local/bin/chromedriver"  # Adjust path as per your Docker setup
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

    # Specify ChromeDriver and options
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

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