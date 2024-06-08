from selenium import webdriver

driver = webdriver.Chrome()  # or webdriver.Firefox()
driver.get("(link unavailable)")
element = driver.find_element_by_name("q")
driver.quit()