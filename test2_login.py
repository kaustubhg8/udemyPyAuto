import time

from selenium import webdriver
from selenium.webdriver import Keys


def get_driver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobards")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sanfbox")
    # options.add_argument("headless=True")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("detach", True)
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://automated.pythonanywhere.com/")
    return driver


def clean_test(text):
    output = text.split()
    output_float = float(output[-1])
    return output_float

def main():
    driver = get_driver()
    time.sleep(3)
    element = driver.find_element(by="xpath", value="//*[@id = 'basicExampleNav']/div/a")
    element.click()
    username_btn = driver.find_element(by='id', value="id_username")
    username_btn.send_keys("automated")
    password_btn = driver.find_element(by="name", value="password")
    password_btn.send_keys("automatedautomated", Keys.RETURN)
    time.sleep(3)
    print(driver.current_url)
    home_btn = driver.find_element(by="xpath", value="/html/body/nav/div/a")
    home_btn.click()
    print(driver.current_url)
    time.sleep(3)
    timer_element = driver.find_element(by='xpath', value="//*[@id='displaytimer']/div")
    timer_text=timer_element.text
    print(clean_test(timer_text))
    driver.close()


main()

