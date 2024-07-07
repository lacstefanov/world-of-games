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

url = os.getenv('APP_URL', 'http://world_of_games_container:5001/')


def test_score_service(url):
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")

    chrome_binary_path = '/usr/bin/google-chrome'
    service = Service(ChromeDriverManager().install())
    chrome_options.binary_location = chrome_binary_path
    driver = webdriver.Chrome(service=service, options=chrome_options)
    try:
        logger.info(f"Attempting to access URL: {url}")
        driver.get(url)
        score_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "score")))
        score_text = score_element.text
        score = int(score_text)
        is_within_range = 1 <= score <= 1000

        return is_within_range
    finally:
        driver.quit()


result = test_score_service(url)

