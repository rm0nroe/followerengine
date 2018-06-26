from selenium import webdriver
import time

print("Hellow!")
# provide path to your chromedriver on local
driver = webdriver.Chrome("/Users/ryanmonroe/PycharmProjects/marketme/chromedriver");

driver.get("https://www.instagram.com/accounts/login/");


# function to log user in
def login(username, password, submit):
    username.send_keys("");
    password.send_keys("");
    submit.click();
    return;


# finding username and password elements
username = driver.find_element_by_name("username");
password = driver.find_element_by_name("password");
submitButton = driver.find_element_by_xpath("//button[contains(.,'Log in')]");

# logging in
login(username, password, submitButton);

# <a class="_2dbep qNELH kIKUG" href="/ryanmonroe/" style="width: 50px; height: 50px;">
# performs search of hashtags, places or users
def search(criteria):
    time.sleep(2);
    driver.find_element_by_css_selector("input[type=text]").send_keys(criteria);
    return;


search("Tiger woods");

# <button class="_5f5mN       jIbKX KUBKM      yZn4P   ">Log in</button>
