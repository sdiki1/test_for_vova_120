import random, time, datetime
import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from database import engine, Accounts
from sqlalchemy.orm import sessionmaker

logging.basicConfig(level=logging.INFO, filename="Buy.log", filemode="w")


def get_random_timig():
    res = {
        "level1": random.randint(1, 4),
        "level2": random.randint(4, 10),
        "level3": random.randint(10, 15),
        "level4": random.randint(20, 40),
    }
    return res


def add_to_cart(key: str, article: str, size: str):
    res = False
    values = get_random_timig()
    while True:
        try:
            Session = sessionmaker(bind=engine)
            session = Session()
            free_accounts = (
                session.query(Accounts).filter(Accounts.Is_using == False).all()
            )
            account = free_accounts[random.randint(0, len(free_accounts) - 1)]
            authv3 = account.AuthV3
            account.Is_using = True
            session.add(account)
            session.commit()
            account = session.query(Accounts).filter(Accounts.AuthV3 == authv3).first()
            session.close()
            logging.info("account found")
            break
        except Exception as e:
            print("ERROR, NO FREE ACCOUNTS, WHAIT THE FREE ACCOUNT", e)
            time.sleep(values["level4"])

    try:
        with webdriver.Chrome() as browser:
            url = "https://www.wildberries.ru"
            browser.get(url)
            browser.set_window_size(1920, 1080)

            cookie = {"name": "WILDAUTHNEW_V3", "value": account.AuthV3}
            browser.add_cookie(cookie)
            browser.refresh()
            time.sleep(values["level2"])

            browser.find_element(
                By.XPATH, "/html/body/div[1]/header/div/div[2]/div[2]/div[4]/a"
            ).click()

            # add clear all in our cart
            time.sleep(values["level2"])

            browser.find_element(
                By.XPATH, "/html/body/div[1]/header/div/div[2]/div[3]/div[1]/input"
            ).send_keys(key)
            actions = ActionChains(browser)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            time.sleep(values["level1"])
            cont = True
            browser.execute_script("window.scrollBy(0,-1000)")
            for l in range(15):
                if not cont:
                    break
                for i in range(1, 101):
                    browser.execute_script("window.scrollBy(0,95)")
                    try:
                        element = browser.find_element(
                            By.XPATH,
                            f"/html/body/div[1]/main/div[2]/div/div[2]/div/div/div[4]/div[1]/div[1]/div/article[{i}]",
                        )
                    except:
                        logging.error(
                            f"element {i} on page: {l+1} not found, try to close page with another article"
                        )
                        print("ERROR, CHECK LOG")
                        browser.execute_script("window.scrollBy(0,500)")
                        time.sleep(values["level4"])
                        browser.execute_script("window.scrollBy(0,-500)")
                        time.sleep(values["level4"])
                        try:
                            browser.find_element(
                                By.XPATH, "/html/body/div[1]/a"
                            ).click()
                        except:
                            pass
                        try:
                            element = browser.find_element(
                                By.XPATH,
                                f"/html/body/div[1]/main/div[2]/div/div[2]/div/div/div[4]/div[1]/div[1]/div/article[{i}]",
                            )
                        except:
                            browser.execute_script(f"window.scrollBy(0,{90*i})")
                            element = browser.find_element(
                                By.XPATH,
                                f"/html/body/div[1]/main/div[2]/div/div[2]/div/div/div[4]/div[1]/div[1]/div/article[{i}]",
                            )
                    article_el = element.get_attribute("data-nm-id")
                    print(f"article: {article_el}")
                    time.sleep(values["level1"])
                    if random.randint(0, 1) or article_el == article:
                        try:
                            browser.find_element(
                                By.XPATH, "/html/body/div[1]/a"
                            ).click()
                        except:
                            pass
                        print(i, "- try to open it")
                        time.sleep(values["level2"])
                        try:
                            element.click()
                        except:
                            logging.error("Couldn't open card with product")
                            time.sleep(20)
                            try:
                                element.click()
                            except:
                                logging.error("Wait, that U will check it")
                        time.sleep(values["level1"])
                        browser.execute_script("window.scrollBy(0,1080)")
                        time.sleep(values["level2"])
                        browser.execute_script("window.scrollBy(0,-1080)")
                        time.sleep(values["level3"])
                        if article_el == article:
                            print("THIS IS ARTICLE THAT WE NEED")
                            if size != "":
                                elements = browser.find_elements(
                                    By.CLASS_NAME, "sizes-list__item"
                                )
                                el = None
                                for element in elements:
                                    if (
                                        element.find_element(
                                            By.CLASS_NAME, "sizes-list__size"
                                        ).text
                                        == size
                                    ):
                                        el = element
                            el.click()
                            browser.find_element(
                                By.XPATH,
                                "/html/body/div[1]/main/div[2]/div/div[3]/div/div[3]/div[11]/div/div[1]/div[3]/div/button[2]",
                            ).click()
                            time.sleep(5)
                            res = True
                            cont = False
                            print("try to open cart")
                            time.sleep(10)
                            browser.find_element(
                                By.XPATH,
                                "/html/body/div[1]/main/div[2]/div/div[3]/div/div[3]/div[11]/div/div[1]/div[3]/div/a",
                            ).click()
                            time.sleep(20)
                            logging.info("try to choose order point")
                            browser.find_element(
                                By.XPATH,
                                "/html/body/div[1]/main/div[2]/div/div[4]/div/div[1]/form/div[1]/div[2]/div[2]",
                            ).click()
                            time.sleep(10)
                            adress = "г Москва, Улица Вертолётчиков 9к2"
                            browser.find_element(
                                By.XPATH,
                                "/html/body/div[1]/div/div/div[4]/div[1]/ymaps/ymaps/ymaps/ymaps[4]/ymaps[1]/ymaps[1]/ymaps/ymaps[1]/ymaps/ymaps/ymaps/ymaps/ymaps[1]/ymaps/ymaps[1]/ymaps[1]/input",
                            ).send_keys("г Москва, Улица Вертолётчиков 9к2")
                            time.sleep(5)
                            browser.find_element(
                                By.XPATH,
                                "/html/body/div[1]/div/div/div[4]/div[1]/ymaps/ymaps/ymaps/ymaps[4]/ymaps[1]/ymaps[1]/ymaps/ymaps[1]/ymaps/ymaps/ymaps/ymaps/ymaps[1]/ymaps/ymaps[2]/ymaps/ymaps",
                            ).click()
                            time.sleep(10)
                            browser.find_element(
                                By.XPATH,
                                "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/div",
                            ).click()
                            time.sleep(5)
                            browser.find_element(
                                By.XPATH,
                                "/html/body/div[1]/div/div/div[2]/div[2]/div/div[3]/button",
                            ).click()
                            break
                        try:
                            browser.find_element(
                                By.XPATH,
                                "/html/body/div[1]/main/div[2]/div/div[3]/div/div[2]/div[1]/button",
                            ).click()
                            time.sleep(30)
                        except Exception as E:
                            pass

                if cont:
                    time.sleep(10)
                    browser.execute_script("window.scrollBy(0,120)")
                    browser.find_element(
                        By.XPATH,
                        "/html/body/div[1]/main/div[2]/div/div[2]/div/div/div[5]/div/a[7]",
                    ).click()
                    break

            # browser.execute_script("window.scrollBy(0,1000)")

            print("ALL DONE")

            time.sleep(50)
            browser.close()
    except Exception as e:
        print("ERROR NUHUY\n", e)
    finally:
        account.Is_using = False
        account.Date_active = datetime.datetime.today()
        session = Session()
        session.add(account)
        session.commit()
        session.close()
        print("end!")
    if res:
        return 1
    return 0
