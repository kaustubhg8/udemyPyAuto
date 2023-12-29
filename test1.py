import time

from selenium import webdriver


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
    element = driver.find_element(by="xpath", value="/html/body/div/div/h1[2]")
    text_element = element.text
    return clean_test(text_element)


print(main())
