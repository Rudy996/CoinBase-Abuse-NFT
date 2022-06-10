import re
from multiprocessing import Pool
from random import choice
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--disable-gpu')
options.add_argument('--disable-infobars')
options.add_argument("--mute-audio")
options.add_argument("--disable-blink-features")
options.add_argument('--profile-directory=Default')
options.add_argument("--mute-audio")
options.add_extension("Coinbase.crx")

acc = 5 # сколько зарегать акков
o = ("1")
mail42 = o * acc

f = open('eth.txt', 'r')
i = 0
for line in f:
    i
    i += 1
with open("eth.txt", "r") as f:
    private = f.read().split('\n')
    i = i - 1




def work(private):
    try:
        print(private)
        driver = webdriver.Chrome(executable_path=r"chromedriver\chromedriver.exe", options=options)
        wait = WebDriverWait(driver, 30)
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="btn-import-existing-wallet"]'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="btn-import-recovery-phrase"]'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@data-testid="seed-phrase-input"]'))).send_keys(private)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="btn-import-wallet"]'))).click()
        user = "".join([choice("abcdefghijklmnopqrstuvwxyz") for _ in range(1)]) + "".join([choice("abcdefghijklmnopqrstuvwxyz013456789") for _ in range(8)])
        wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@data-testid="username-input"]'))).send_keys(user)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="btn-submit-username"]'))).click()
        password = "".join([choice("abcdefghijklmnopqrstuvwxyz013456789") for _ in range(13)])
        wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@data-testid="setPassword"]'))).send_keys(password)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@data-testid="setPasswordVerify"]'))).send_keys(password)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@data-testid="terms-and-privacy-policy-parent"]'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="btn-password-continue"]'))).click()
        driver.get("https://matic.coinbasewalletnft.io/minting")
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'sc-dkzDqf'))).click()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'jBQrVW'))).click()
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[2])
        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="allow-authorize-button"]'))).click()
        driver.switch_to.window(driver.window_handles[0])
        wait = WebDriverWait(driver, 160)
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'frHloG'))).click()
        with open('reg.txt', 'a') as file:
            file.write(f'{private}\n')
        time.sleep(1)














    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    p = Pool(processes=1) # кол-во потоков
    p.map(work, private)
