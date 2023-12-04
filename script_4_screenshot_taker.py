import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def take_screenshot(html_file, save_path):
    # Initialize the Firefox driver
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    # Open the HTML file
    driver.get("file://" + html_file)

    # Take screenshot and save it
    driver.save_screenshot(save_path)

    # Close the browser
    driver.quit()

def process_folders(base_data_path, source_subfolder, image_name):
    # Define source path using the base data path
    source_path = os.path.join(os.getcwd(), base_data_path, source_subfolder)
    
    counter = 0
    for item in os.listdir(source_path):
        counter += 1
        print(f"({counter}/{len(os.listdir(source_path))}) Taking screenshot for {item}.")
        full_path = os.path.join(source_path, item)
        html_file = os.path.join(full_path, "index.html")
        screenshot_path = os.path.join(full_path, image_name)
        take_screenshot(html_file, screenshot_path)


# Define the base 'data' folder path
base_data_path = 'data'

# Define the source subfolder
source_subfolder = '3_Accepted'

image_name = 'preview.png'


process_folders(base_data_path, source_subfolder, image_name)
