import os.path
from typing import Dict

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from parsing_web import get_header_link, save_excel
from send_email import send_email

if __name__ == "__main__":
    file_name = "tesla.xlsx"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.page_load_strategy = "normal"

    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)

    data: Dict[str, list] = get_header_link(driver, 'https://www.tesla.com/')

    save_excel(data, file_name)

    email_sender = os.getenv("EMAIL")
    email_password = os.getenv("PASSWORD")
    email_receiver = os.getenv("RECEIVER")

    subject = "Code parser"

    body = """
        Excel file, file contain info about tesla cars
        """

    path = os.path.abspath(file_name)
    send_email(email_sender, email_password, email_receiver, subject, body, path)