# Importing the required modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Specifying the path to the ChromeDriver executable
driver_path = r"C:\Users\kmranrg\Documents\SearchEngine_Selenium.Py\chromedriver-win64\chromedriver.exe"

# Specifying the path to the Chrome binary
chrome_binary_path = r"C:\Users\kmranrg\Documents\SearchEngine_Selenium.Py\chrome-win64\chrome.exe"

# Setting Chrome options to use the specific Chrome binary
options = Options()
options.binary_location = chrome_binary_path

# Initializing the WebDriver with the Chrome options
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=options)

# Opening Google
driver.get("https://www.google.com")

# Finding the search box, entering a query, and submitting
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("kmranrg")
search_box.send_keys(Keys.RETURN)

# Waiting for the results to load
time.sleep(3)

# Finding the titles and links of the search results
results = driver.find_elements(By.CSS_SELECTOR, "div.g h3")
links = driver.find_elements(By.CSS_SELECTOR, "div.g a")

# Extracting and printing the titles and URLs
with open("search_results.txt", "w", encoding="utf-8") as file:
    for result, link in zip(results, links):
        title = result.text
        url = link.get_attribute("href")
        print(f"Title: {title}\nURL: {url}\n")
        file.write(f"Title: {title}\nURL: {url}\n\n")

# Closing the browser
driver.quit()