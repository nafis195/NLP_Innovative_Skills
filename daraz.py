import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
driver.get("https://www.daraz.com.bd/routers/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)
link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#root > div > div.ant-row.FrEdP.css-1bkhbmc.app > div:nth-child(1) > div > div.ant-col.ant-col-20.ant-col-push-4.Jv5R8.css-1bkhbmc.app > div._17mcb > div:nth-child(1) > div > div > div.buTCk > div.RfADt > a')))
print(link.get_attribute('href'))

time.sleep(500)
driver.close()
