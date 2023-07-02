from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Variables
movie_and_rating = []
movies_links = []

estrelas = {
    "★": 1,
    "★½": 1.5,
    "★★": 2,
    "★★½": 2.5,
    "★★★": 3,
    "★★★½": 3.5,
    "★★★★": 4,
    "★★★★½": 4.5,
    "★★★★★": 5
}

# Creating scraper
DRIVER_PATH = './chromedriver.exe'
service = Service(executable_path=DRIVER_PATH)

options = Options()
#options.headless = True

driver = webdriver.Chrome(service=service, options=options)

# Coletar dados de usuários na pagina https://letterboxd.com/members/ com o scraper

users = ["renan_mind"]

driver.get("https://letterboxd.com/" + users[0] + "/films/")

while(True):
    sleep(5) # Wainting so the page can load everything

    # Getting titles, links and ratings
    films_list = driver.find_elements(By.CLASS_NAME, "poster-container")

    for item in films_list:
        try:
            e1 = item.find_element(By.CLASS_NAME, "poster-viewingdata")
            e2 = e1.find_element(By.CLASS_NAME, "rating")
            rating_user = e2.text
            rating = estrelas.get(rating_user)
        except NoSuchElementException:
            continue
        e3 = item.find_element(By.CLASS_NAME, "poster")
        e4 = e3.find_element(By.TAG_NAME, "div")
        e5 = e4.find_element(By.CLASS_NAME, "frame")
        title = e5.get_attribute('data-original-title')
        link = e5.get_attribute('href')
        movies_links.append(link)
        movie_and_rating.append([title, rating])

    try:
        next = driver.find_element(By.XPATH, "//*[@id='content']/div/div/section/div[2]/div[2]/a")
    except NoSuchElementException:
            break;
    next.click()


driver.quit()
