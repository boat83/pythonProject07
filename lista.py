#def con_feed_listt():
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(ChromeDriverManager().install())
try:
    driver.get('http://localhost:1667/#/login')
    #wait = WebDriverWait(driver, 5)
    # tesztfelhasználó: email: testuser1@example.com password: Abcd123$ bejelentkezés

    driver.find_element_by_xpath('//fieldset//input[@placeholder="Email"]').send_keys('testuser1@example.com')
    driver.find_element_by_xpath('//fieldset//input[@placeholder="Password"]').send_keys('Abcd123$')
    driver.find_element_by_xpath('//form/button').click()
    time.sleep(2)


    # user blogbejegyzéseinek listázása:

    driver.find_element_by_xpath('//div[@class="container"]//ul/li[4]/a').click()
    # az oldalon lévő címek kilistázása és a lista mentése fájlba
    time.sleep(3)
    #wait_profile_page = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="profile-page"]//h4')))
    my_articles = driver.find_elements_by_xpath('//div[@class="article-preview"]//h1')

    list_of_feed = []
    for row in my_articles:
        list_of_feed.append(row.text + '\n')
    print(list_of_feed)
    with open('user_articles.txt', 'w') as x:
        for i in list_of_feed:
            x.write(i)
finally:
    driver.close()