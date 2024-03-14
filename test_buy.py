from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

URL='https://www.saucedemo.com/'
NAME='standard_user'
CRED='secret_sauce'
FIRST='NIYOG'
LAST='V'
POSTAL='560072'


def test_buy():
    driver=webdriver.Chrome()
    wait=WebDriverWait(driver, 60)
    driver.get(URL)
    Titlecheck=wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="login_logo"]')))
    assert Titlecheck.text=='Swag Labs'
    driver.find_element(By.NAME, 'user-name').send_keys(NAME)
    driver.find_element(By.ID, 'password').send_keys(CRED)
    driver.find_element(By.ID, 'login-button').click()
    h3TitleCheck=wait.until(EC.presence_of_element_located((By.TAG_NAME, 'span')))
    assert h3TitleCheck.text=='Products'
    driver.find_element(By.XPATH, '//div[@class="inventory_item"][2]/div[2]/div[2]/button').click()
    driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]').click()
    driver.find_element(By.XPATH, '//button[2]').click()
    driver.find_element(By.NAME, 'firstName').send_keys(FIRST)
    driver.find_element(By.NAME, 'lastName').send_keys(LAST)
    driver.find_element(By.NAME, 'postalCode').send_keys(POSTAL)
    driver.find_element(By.XPATH, '//input[@type="submit"]').click()
    driver.find_element(By.XPATH, '//button[2]').click()
    spanTitleCheck=driver.find_element(By.TAG_NAME, 'span')
    assert spanTitleCheck.text=='Checkout: Complete!'
