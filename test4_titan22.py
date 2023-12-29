
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
    options.add_argument("headless=True")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("detach", True)
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://titan22.com/account/login?return_url=%2Faccount")
    return driver


def clean_test(text):
    output = text.split()
    output_float = float(output[-1])
    return output_float

def main():
    driver = get_driver()
    time.sleep(3)
    # element = driver.find_element(by="xpath", value="//*[@id = 'basicExampleNav']/div/a")
    # element.click()
    print(driver.current_url)
    driver.find_element(by='name', value='customer[email]').send_keys("kgtest812@gmail.com")
    driver.find_element(by='name', value='customer[password]').send_keys("333akash", Keys.RETURN)
    time.sleep(2)
    driver.find_element(by='xpath',value="//*[@id='shopify-section-footer']/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a").click()
    print(driver.current_url)
main()

