import streamlit as st
from utils import *



def streamlit_app() -> str:
    # title of the app
    st.title("Google Lead Collection App")

    # input field for the user to enter the search query
    search_term = st.text_input("Please enter the text here:")
    # print(search_term)
    return search_term


def chrome_driver() -> webdriver.Chrome:
    chrome_options = Options()
    chrome_options.add_argument("--disable-cache")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--lang=en-US,en;q=0.9")
    chrome_options.add_argument("--referer=https://www.google.com/")
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
    driver = webdriver.Chrome(options=chrome_options)
    return driver


def google_search(search_term: str, google_driver: webdriver.Chrome) -> None:
    # google_driver = uc.Chrome(headless=True,use_subprocess=False)
    google_driver.get("https://www.google.com/")
    google_driver.maximize_window()

    search_box = google_driver.find_element(By.NAME, "q")
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)

    recaptcha_checkbox = google_driver.find_element(By.CLASS_NAME, "g-recaptcha")
    time.sleep(10)
    action = ActionChains(google_driver)
    action.move_to_element(recaptcha_checkbox).click().perform()

    time.sleep(60)


def google_links(google_driver) -> dict:
    links = []

    for i in range(1, 11):
        type_i = str(i)
        link = google_driver.find_element(By.XPATH, f'//*[@id="rso"]/div[{type_i}]/div/div/div[1]/div/div/span/a/h3').get_attribute('href')
        links.append(link)
    # for link in st.session_state["google_driver"].find_elements(By.XPATH, "//a[@href]"):
    #     links[link.get_attribute("href")] = link.text
    return links


def main():
    search_term = streamlit_app()
    
    if search_term:
        google_driver = chrome_driver()
        google_search(search_term, google_driver)
        my_links = google_links()
        print(my_links)
        st.success("Search completed successfully!")

    google_driver.quit()


if __name__ == "__main__":
    main()

