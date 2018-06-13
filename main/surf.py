from selenium import webdriver


print("Hellow!")
# provide path to your chromedriver on local
driver = webdriver.Chrome("/Users/ryanmonroe/PycharmProjects/marketme/chromedriver");

driver.get("http://www.hotnewhiphop.com");

