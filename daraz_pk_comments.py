from utils import *



def chrome_launch() -> webdriver.Chrome:
    chrome_options = Options()
    chrome_options.add_argument("--disable-cache")
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://www.daraz.pk/products/50-i455245927-s2157195277.html")
    driver.maximize_window()

    height = driver.execute_script("return document.body.scrollHeight")
    # print(height)
    time.sleep(30)

    for i in range(0, height+500, 30):
        driver.execute_script(f"window.scrollTo(0, {i});")
        time.sleep(0.5)

    return driver


def comment_collection(ChromeDriver) -> dict:

    comment_dict = {}

    for i in range(1, 11):
        if i < 4:
            i = str(i)
            element = ChromeDriver.find_element(By.XPATH, f'//*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button[{i}]')
        elif i >= 4 and i < 10:
            i = "4"
            element = ChromeDriver.find_element(By.XPATH, f'//*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button[{i}]')
        else:
            i = "5"
            element = ChromeDriver.find_element(By.XPATH, f'//*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button[{i}]')

        element.click()
        time.sleep(5)

        all_comments = ChromeDriver.find_elements(By.CLASS_NAME, 'content')

        comment_list = []

        for j in all_comments:
            comment_list.append(j.text)

        i = str(i)
        comment_dict[f'Page{i}'] = comment_list
    
    return comment_dict


def main():
    driver = chrome_launch()
    print(comment_collection(driver))
    driver.quit()


__init__ = main()






# button1 >>> //*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button[1]
# button2 >>> //*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button[2]
# button3 >>> //*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button[3]
# button4 >>> //*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button[4]
# button5 >>> //*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button[4]
# button6 >>> //*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button[4]
# button7 >>> //*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button[4]
# button8 >>> //*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button[4]
# button9 >>> //*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button[4]
# button10 >>> //*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button[5]


# button1 >>> //*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button[1]
# button2 >>> //*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button[2]
# button3 >>> //*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button[3]
# button4 >>> //*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button[4]
# button5 >>> //*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button[4]
# button6 >>> //*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button[4]
# button7 >>> //*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button[4]