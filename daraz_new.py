from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-cache")
chrome_options.add_argument("--incognito")
# chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.6834.110 Safari/537.36")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.daraz.pk/products/orignal-p47-headphone-wireless-earbuds-invisible-ultra-small-bluetooth-handfree-for-all-cell-phones-i166492518-s1815011592.html")
print(driver.title)

driver.quit()