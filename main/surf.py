from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


print("Launching!")


# provide path to your chromedriver on local
driver = webdriver.Chrome("/Users/ryanmonroe/PycharmProjects/marketme/chromedriver");


driver.get("https://www.instagram.com/accounts/login/")


# function to log user in
def login(username, password):
    # finding username and password elements
    username_field = driver.find_element_by_name("username")
    password_field = driver.find_element_by_name("password")
    submit = driver.find_element_by_xpath("//button[contains(.,'Log in')]")
    # entering credentials
    username_field.send_keys(username)
    password_field.send_keys(password)
    submit.click()

    return;

# logging in - enter credentials
login("","")


# performs search of hashtags, places or users
# the user will define this search - for hashtags - the search will be preceeded with such
# script waits for profile picture to render on page before executing search
def search(criteria, search_type, username):
    # urls for each type of search
    # <a href="/explore/tags/plants/"/> -- hashtags
    # <a href = "/explore/locations/atlanta/"/> -- locations
    # <a href="/profilename/"/> -- profiles

    try:
        element_present = EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/' + username + '/"]'))
        WebDriverWait(driver, 5).until(element_present)
        search_url = 'https://www.instagram.com/explore'
        criteria = criteria.replace(" ", "").lower()

        if search_type == 'hashtag':
            search_url = search_url + '/tags/' + criteria
        elif search_type == 'location':
            search_url = search_url + '/locations/' + criteria
        else:
            search_url = search_url + '/' + criteria

        print('Performing search...' + search_url)
        driver.get(search_url)

    except TimeoutException:
        print
        "Timed out waiting for page to load."

    return;


# enter inputs here to test
search("Tiger woods", "hashtag", "ryanmonroe");
