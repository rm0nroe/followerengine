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


def scan_posts(criteria):	
    criteria = criteria.replace(" ", "").lower()	
    matcher = "tagged=" + criteria	
    hrefs = []	
    posts = driver.find_elements_by_xpath("//a[@href]")	
    for post in posts:	
        if matcher in post.get_attribute("href"):	
            hrefs.append(post.get_attribute("href"))	

    return hrefs;	


def like_post(links):	
    for link in links:	
        driver.get(link)	
    like_xpath = "//a[@role='button']/span[text()='Like']/.."	
    unlike_xpath = "//a[@role='button']/span[text()='Unlike']"	
    spans = [x.text.lower() for x in driver.find_elements_by_xpath("//article//a[@role='button']/span")]	

    if 'like' in spans:	
        like_elem = driver.find_elements_by_xpath(like_xpath)	

        # sleep real quick right before clicking the element	
        # sleep(2)	
        # click_element(driver, like_elem[0])	
        like_elem[0].click()	
        # check now we have unlike instead of like	
        liked_elem = driver.find_elements_by_xpath(unlike_xpath)	
        if len(liked_elem) == 1:	
            print("like succeeded")	
            # logger.info('--> Image Liked!')	
            # update_activity('likes')	
            # if blacklist['enabled'] is True:	
            #     action = 'liked'	
            #     add_user_to_blacklist(	
            #         username, blacklist['campaign'], action, logger, logfolder	
            #     )	
            # sleep(2)	
            return True;	
        else:	
            # if like not seceded wait for 2 min	
            # logger.info('--> Image was not able to get Liked! maybe blocked ?')	
            # sleep(120)	
            print('put sleep here')	
    else:	
        liked_elem = driver.find_elements_by_xpath(unlike_xpath)	
        if len(liked_elem) == 1:	
            print("like not in spans")	
    return False	



# enter inputs here to test	
search("Tiger woods", "hashtag", "ryanmonroe")	
like_post(scan_posts("Tiger woods"))	
# need to add functionality to check whether a photo has already been liked	
# need to add list of like photos to check against
