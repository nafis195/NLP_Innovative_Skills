import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("laptop shop near me")
search_box.send_keys(Keys.RETURN)

recaptcha_checkbox = driver.find_element(By.CLASS_NAME, "g-recaptcha")
time.sleep(10)
action = ActionChains(driver)
action.move_to_element(recaptcha_checkbox).click().perform()


time.sleep(60)
driver.quit()