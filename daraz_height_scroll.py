import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
driver.get('https://www.daraz.com.bd/products/4g-wifi-i468701703.html')

height = driver.execute_script("return document.body.scrollHeight")
print(height)

# time.sleep(30)

for i in range(0, height+1500, 30):
    driver.execute_script(f"window.scrollTo(0, {i});")
    time.sleep(0.5)

all_comments = driver.find_elements(By.CLASS_NAME, 'content')

for i in all_comments:
    print(i.text)

driver.quit()


