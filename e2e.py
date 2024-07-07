import os
import logging
import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Set up stdout handler to ensure immediate flushing
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
stdout_handler.setFormatter(formatter)
logger.addHandler(stdout_handler)


url = os.getenv('APP_URL', 'http://world_of_games_container:5001/')
logger.info(f"URL being tested: {url}")
with open('/app/logs/test_output.log', 'r') as file:
    print(file.read())


def test_score_service(url):
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")

    chrome_binary_path = '/usr/bin/google-chrome'
    service = Service(ChromeDriverManager().install())
    chrome_options.binary_location = chrome_binary_path
    logger.info("Initializing WebDriver...")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    logger.info(f"WebDriver initialized: {driver}")
    try:
        logger.info(f"Attempting to access URL: {url}")
        driver.get(url)
        score_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "score")))
        score_text = score_element.text
        score = int(score_text)
        is_within_range = 1 <= score <= 1000
        logger.info(f"Score retrieved: {score}, is_within_range: {is_within_range}")
        return is_within_range
    finally:
        driver.quit()


result = test_score_service(url)
print("Score is within range: ", result)
