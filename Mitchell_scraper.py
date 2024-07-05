from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.firefox import GeckoDriverManager
from Logs.Logger import log_messages
import logging
import time

class driverMitchell:
    def __init__(self):
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20) # 20 seconds webdriver wait

    def open_mitchell(self): # open AutoCodes on Firefox
        try:
            logging.info('Opening AutoCodes website on Firefox')
            self.driver.get("https://www.autocodes.com/")
        
        except Exception as e:
            logging.error(f'Error while Opening AutoCodes website on Firefox: {str(e)}')
            
    def close_driver(self): # quit firefox
        try:
            logging.info('Quitting AutoCodes website on Firefox')
            self.driver.quit()
        
        except Exception as e:
            logging.error(f'Error while quitting AutoCodes website on Firefox: {str(e)}')

    def click_search_bar(self): # wait until the website loads to click on the search bar
        try:

            logging.info('Looking for the search bar before writing the error code')
            searchbar = self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/nav/header/div[4]/form/input[1]')))
            
            logging.info('Clicking search bar before writing the error code')
            searchbar.click()
        
        except Exception as e:
            logging.error(f'Error while looking or clicking the Search Bar on Firefox: {str(e)}')


Driver = driverMitchell() # instance of the driver mitchell class

Driver.open_mitchell() # open AutoCodes on Firefox
Driver.click_search_bar() # click search bar before writing the error code
time.sleep(5) # wait 5 seconds to close the driver
Driver.close_driver() # close firefox