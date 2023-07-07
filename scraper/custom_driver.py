from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options



class CustomDriver:
    
    DRIVER_PATH = './chromedriver.exe'
    
    def __init__(self, headless = False, driver_path = DRIVER_PATH):
        self.driver_path = driver_path
        self.service = None
        self.driver = None

        options = Options()
        # options.add_extension("scraper\extension_5_8_0_0.crx")
        options.headless = headless

        self.service = Service(executable_path=self.driver_path)
        self.driver = webdriver.Chrome(service=self.service, options=options)
        
    def driver(self):
        return self.driver

    def __del__(self):
        if self.driver:
            self.driver.quit()
