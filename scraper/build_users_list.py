from time import sleep
import csv
from custom_driver import CustomDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

cd = CustomDriver(headless=False)

def build_user_list(page):
    cd.driver.get(f"https://letterboxd.com/members/popular/this/all-time/page/{page}")
    person_table = cd.driver.find_elements(By.TAG_NAME, 'tr')
    
    users_profiles = set()
    
    for person in person_table:
        try:
            avatar = person.find_element(By.CLASS_NAME, "avatar")
            users_profiles.add(avatar.get_attribute('href'))
        except NoSuchElementException:
            continue
        
    return users_profiles

def iterate_over_users_page(pages_range):
    users_profiles = set()
    for i in range(1, pages_range + 1):
        print(f"Scraping page {i} ...")
        
        users_profiles = users_profiles.union(build_user_list(i))
        
        try:
            cd.driver.find_element(By.XPATH, "//*[@id='content']/div/div/section/div[2]/div[2]/a")
        except NoSuchElementException:
            break;
        
    return users_profiles

profiles = iterate_over_users_page(2)

header = ['link']

with open("users_profiles.csv", 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(header)
    
    for profile in profiles:
        writer.writerow([profile])
