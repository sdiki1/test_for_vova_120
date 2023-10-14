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
            browser.set_window_size(1920, 1080)
            
            print(account)
            cookie = {'name': 'WILDAUTHNEW_V3', 'value': account.AuthV3}
            browser.add_cookie(cookie)
            browser.refresh()
            time.sleep(3)

            browser.find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/div[2]/div[4]/a').click()

            # add clear all in our cart
            time.sleep(10)

            browser.find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/div[3]/div[1]/input').send_keys(key)
            actions = ActionChains(browser)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            time.sleep(3)
            for l in range(15):
                for i in range(1, 60):

                    browser.execute_script("window.scrollBy(0,180)")
                    try:
                        element = browser.find_element(By.XPATH, f'/html/body/div[1]/main/div[2]/div/div[2]/div/div/div[4]/div[1]/div[1]/div/article[{i}]')
                    except:
                        browser.find_element(By.XPATH, '/html/body/div[1]/a').click()
                        element = browser.find_element(By.XPATH, f'/html/body/div[1]/main/div[2]/div/div[2]/div/div/div[4]/div[1]/div[1]/div/article[{i}]')
                    article_el = element.get_attribute('data-nm-id')
                    print(f'article: {article_el}')
                    time.sleep(0.4)
                    if random.randint(0, 1) or article_el == article:
                        try:
                            browser.find_element(By.XPATH, '/html/body/div[1]/a').click()
                        except:
                            pass
                        try:
                            print(i, '- try to open it')
                            time.sleep(5)
                            element.click()
                        except:
                            browser.find_element(By.XPATH, '/html/body/div[1]/a').click()
                            print(i, '- try to open it, ERROR CORRUPTED')
                            time.sleep(5)
                            element.click()
                        
                        time.sleep(4)
                        browser.execute_script("window.scrollBy(0,1080)")
                        time.sleep(3)
                        browser.execute_script('window.scrollBy(0,-1080)')
                        time.sleep(8)
                        if article_el == article:
                            browser.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/div[3]/div/div[3]/div[11]/div/div[1]/div[3]/div/button[2]').click()
                        try:
                            browser.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/div[3]/div/div[2]/div[1]/button').click()
                        except Exception as E:
                            pass
                        time.sleep(5)
                time.sleep(10)
                browser.execute_script("window.scrollBy(0,120)")    
                browser.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/div[2]/div/div/div[5]/div/a[7]').click()

                    

            # browser.execute_script("window.scrollBy(0,1000)")

            print('ALL DONE')

            time.sleep(50)
    except Exception as e:
        print('ERROR NUHUY\n', e)
    account.Is_using = False
    session = Session()
    session.add(account)
    session.commit()
    session.close()


