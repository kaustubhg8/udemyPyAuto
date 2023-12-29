from selenium import webdriver


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
    driver.get("https://afzallokhandwala.com/ctc/")
    return driver


def clean_test(text):
    output = (text.split("₹ ")[1]).split("/-")[0]
    output_float = float(output.replace(',', ''))
    return output_float


def main():
    driver = get_driver()
    element = driver.find_element(by="xpath", value="//*[@data-id='ea3c3d5']/div/h2")
    text_element = element.text
    return clean_test(text_element)


print(main())
