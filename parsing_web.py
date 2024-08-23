import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from typing import Dict

def save_excel(data: Dict[str, list], file_name: str):
    """
    Save data in excel file
    """
    df = pd.DataFrame(data)

    df.to_excel(file_name, index=False)


def get_header_link(driver, url: str) -> Dict[str, list]:
    """
    Find elements in website and take car header, car link
    """
    driver.get(url)
    time.sleep(2)
    driver.find_element('xpath', '//button[@class="tds-icon-btn tds-icon-btn--medium"]').click()
    elements = driver.find_elements('xpath', '//div[contains(@class, "tcl-homepage-hero__content tcl-animate")]')

    body = driver.find_element(By.TAG_NAME, 'body')
    body.click()
    body.send_keys(Keys.PAGE_DOWN)

    names = []
    links = []
    for elem in elements:
        names.append(elem.find_element(By.TAG_NAME, "h1").text)
        links.append(elem.find_element(By.TAG_NAME, "a").get_attribute("href"))
        # data[name] = [link]

    data = {
        "car": names,
        "link": links,
    }

    return data













