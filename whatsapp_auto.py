from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
import time

try:
# Specify the path to the ChromeDriver executable
    chrome_driver_path = "/usr/local/bin/chromedriver"  # Update this path

    # Set up Chrome options (optional)
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--headless")  # Uncomment if you want to run Chrome in headless mode
    # Create a service object
    service = Service(chrome_driver_path)

    # Initialize the WebDriver
    browser = webdriver.Chrome(service=service, options=chrome_options)
    browser.get("https://web.whatsapp.com")

    wait=WebDriverWait(browser,100)
    target='"Simo"'
    message="Hello There From Python Bot"
    number_of_times=10 #No. of times to send a message

    contact_path='//span[contains(@title,'+ target +')]'
    contact=wait.until(EC.presence_of_element_located((By.XPATH,contact_path)))
    contact.click()
    message_box_path='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
    message_box=wait.until(EC.presence_of_element_located((By.XPATH,message_box_path)))
    for x in range(number_of_times):
        message_box.send_keys(message + Keys.ENTER)
        time.sleep(0.2)
    # Open the website

    # Add a delay to see the result before closing (optional)
    # time.sleep(10)
    while(True):
       pass

except Exception as e: 
    print("An error occurred:", e)

finally:
    # Close the browser
    browser.quit()
