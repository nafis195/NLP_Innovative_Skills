from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time



chrome_options = Options()
chrome_options.add_argument("--disable-cache")
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)

# driver = webdriver.Chrome()
# driver.get("https://www.daraz.com.bd/routers/")

link_list = []

for page_no in range(1, 3):
    driver.get(f"https://www.daraz.pk/routers/?page={page_no}")
    driver.maximize_window()
    
    for i in range(1, 11):
        type_i = str(i)
        link = driver.find_element(By.XPATH, f'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[{type_i}]/div/div/div[2]/div[2]/a').get_attribute('href')
        link_list.append(link)

# print(link_list)

time.sleep(120)
driver.close()
