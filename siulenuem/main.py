import random, time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from database import engine, Accounts
from sqlalchemy.orm import sessionmaker



def add_to_cart(key: str, article: str):
    Session = sessionmaker(bind=engine)
    session = Session()
    free_accounts = session.query(Accounts).filter(Accounts.Is_using == False).all()
    account = free_accounts[random.randint(0, len(free_accounts)-1)]
    authv3 = account.AuthV3
    account.Is_using == True
    session.add(account)
    session.commit()
    account = session.query(Accounts).filter(Accounts.AuthV3 == authv3).first()
    session.close()

    try:
        with webdriver.Chrome() as browser:
            url = 'https://www.wildberries.ru'
            browser.get(url)

            print(account)
            cookie = {'name': 'WILDAUTHNEW_V3', 'value': account.AuthV3}
            browser.add_cookie(cookie)
            browser.refresh()
            time.sleep(3)

            browser.find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/div[2]/div[4]/a').click()

            # add clear all in our cart


            browser.find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/div[3]/div[1]/input').send_keys(key)
            actions = ActionChains(browser)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            time.sleep(3)

            browser.execute_script("window.scrollBy(0,1000)")

            time.sleep(50)
    except Exception as e:
        print(e)
    account.Is_using = False
    session = Session()
    session.add(account)
    session.commit()
    session.close()


