import time

from selenium import webdriver
from datetime import datetime

def get_driver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobards")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sanfbox")
    options.add_argument("headless=True")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://automated.pythonanywhere.com/")
    return driver


def clean_test(text):
    output = text.split()
    output_float = float(output[-1])
    return output_float

def date_and_time():
    dt0 = datetime.now()
    dt = dt0.strftime("%Y-%m-%d.%H-%M-%S")
    return dt

def txt_file_gen(text_element):
    dt = date_and_time()
    with open(dt, 'w') as file:
        file.write(dt + " " + f"{text_element}")

def main():
    driver = get_driver()
    time.sleep(3)
    a=0
    while a<10:
        element = driver.find_element(by="xpath", value="/html/body/div/div/h1[2]")
        text_element = element.text
        txt_file_gen(text_element)
        a+=1
        time.sleep(2)

print(main())
