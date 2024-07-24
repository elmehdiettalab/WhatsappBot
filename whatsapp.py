from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
import time
import csv

try:
# Specify the path to the ChromeDriver executable



    chrome_driver_path = "/usr/local/bin/chromedriver"  # Update this path

    filename = input("Enter filepath: ")

    # Set up Chrome options (optional)
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    # chrome_options.add_argument("--headless")  # Uncomment if you want to run Chrome in headless mode
    # Create a service object
    service = Service(chrome_driver_path)
    baseUrl = "https://web.whatsapp.com"
    # Initialize the WebDriver
    browser = webdriver.Chrome(service=service, options=chrome_options)
    browser.get(baseUrl)

    # with open("contacts.csv", newline='') as csvfile:
    with open(filename, newline='') as csvfile:
        readContacts = csv.reader(csvfile)
        for phone,msg in readContacts:
            phonenum = phone
            message = msg

            sameTab = (baseUrl + '/send?phone='+str(phonenum))  

            browser.get(sameTab)

            time.sleep(14)

            content = browser.switch_to.active_element

            content.send_keys(message)

            content.send_keys(Keys.RETURN)


            time.sleep(14)
        
        browser.quit()
        quit()

    # Add a delay to see the result before closing (optional)
    # time.sleep(10)
    while(True):
       pass

except Exception as e: 
    print("An error occurred:", e)

finally:
    # Close the browser
    browser.quit()
