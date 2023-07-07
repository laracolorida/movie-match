import pandas as pd


def split_url_and_get_value(url):
    split_items = url.split("/")
    return split_items[-2]


users = pd.read_csv('users_profiles.csv', encoding='utf-8')
users["link"] = users["link"].apply(split_url_and_get_value)
users_list = users["link"].tolist()

print(users_list)
