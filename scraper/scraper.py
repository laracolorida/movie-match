from time import sleep
import pandas as pd

from custom_driver import CustomDriver

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Variables
movie_and_rating = []
movies_links = []

starts = {
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

df = pd.DataFrame({
        'user': [],
        "movie_link" : [],
        'movie_title': [],
        'rating' : [],
})

def split_url_and_get_value(url):
    split_items = url.split("/")
    return split_items[-2]

cd = CustomDriver(headless=False)

# Coletar dados de usuários na pagina https://letterboxd.com/members/ com o scraper

users = pd.read_csv('users_profiles.csv', encoding='utf-8')
users["link"] = users["link"].apply(split_url_and_get_value)
users = users["link"].tolist()

def iterate_over_users(users_list):
    
    df = pd.DataFrame({
        'user': [],
        "letterbox_movie" : [],
        "movie_link" : [],
        'movie_title': [],
        'rating' : [],
    })
    
    for user in users_list:
        user_data = get_users_ratings(user)
        user_data = pd.DataFrame(user_data)
        df = pd.concat([df,user_data], ignore_index=True)
        
    df.to_csv("users_ratings.csv", index=False)


def get_users_ratings(user):
    
    df_buffer = []
        
    cd.driver.get("https://letterboxd.com/" + user + "/films/")
    
    while(True):
        sleep(5)

        films_list = cd.driver.find_elements(By.CLASS_NAME, "poster-container")

        for item in films_list:
            try:
                e1 = item.find_element(By.CLASS_NAME, "poster-viewingdata")
                e2 = e1.find_element(By.CLASS_NAME, "rating")
                rating_user = e2.text
                rating = starts.get(rating_user)
                
            except NoSuchElementException:
                continue
            
            e3 = item.find_element(By.CLASS_NAME, "poster")
            e4 = e3.find_element(By.TAG_NAME, "div")
            e5 = e4.find_element(By.CLASS_NAME, "frame")
            
            title = e5.get_attribute('data-original-title')
            link = e5.get_attribute('href')
            
            new_data = {
                'user': user,
                "letterbox_movie": split_url_and_get_value(link),
                "movie_link" : link,
                'movie_title': title,
                'rating' : rating
            }
            
            df_buffer.append(new_data)
            
            movies_links.append(link)
            movie_and_rating.append([title, rating, user])

        try:
            try:
                close_ad = cd.driver.find_element(By.XPATH, "//*[@id='pw-close-btn']/span/svg")
                close_ad.click()
            except NoSuchElementException:
                continue
            next_button = cd.driver.find_element(By.XPATH, "//*[@id='content']/div/div/section/div[2]/div[2]/a")
            next_button.click()
        except NoSuchElementException:
                break
    
    return df_buffer

iterate_over_users(users)