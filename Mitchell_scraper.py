from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.firefox import GeckoDriverManager
from Logs.Logger import log_messages
import logging
import time

class driverMitchell:
    def __init__(self):
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    def open_mitchell(self): # open AutoCodes on Firefox
        try:

            self.driver.get("https://www.autocodes.com/")
            logging.info('Opening Mitchell OnDemand5 (proDemand) website on Firefox')
        
        except Exception as e:
            logging.error(f'Error while Opening Mitchell OnDemand5 (proDemand) website on Firefox: {str(e)}')
            
    def close_driver(self): # quit firefox
        try:

            self.driver.quit()
            logging.info('Quitting Mitchell OnDemand5 (proDemand) website on Firefox')
        
        except Exception as e:
            logging.error(f'Error while Quitting Mitchell OnDemand5 (proDemand) website on Firefox: {str(e)}')

Driver = driverMitchell() # instance of the driver mitchell class

Driver.open_mitchell() # open AutoCodes on Firefox
time.sleep(5) # wait 5 seconds to close the driver
Driver.close_driver() # close firefox
