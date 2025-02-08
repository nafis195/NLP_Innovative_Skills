import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options


# Path to the Firefox binary (adjust this path if needed)
firefox_binary_path = "/usr/bin/firefox"

# Path to the Geckodriver (adjust this path if needed)
geckodriver_path = "/snap/bin/geckodriver"

# Set up Firefox options
options = Options()
options.binary_location = firefox_binary_path

# Set up the Firefox WebDriver
service = Service(executable_path=geckodriver_path)
driver = webdriver.Firefox(service=service, options=options)

# Open the webpage
driver.get("https://www.daraz.com.bd/routers/")
driver.maximize_window()

# Wait for the element to appear
wait = WebDriverWait(driver, 10)
link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 
    '#root > div > div.ant-row.FrEdP.css-1bkhbmc.app > div:nth-child(1) > div > div.ant-col.ant-col-20.ant-col-push-4.Jv5R8.css-1bkhbmc.app > div._17mcb > div:nth-child(1) > div > div > div.buTCk > div.RfADt > a')))

# Print the href attribute of the link
print(link.get_attribute('href'))

# Wait and close the browser
time.sleep(500)
driver.close()
