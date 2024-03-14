import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL='https://www.saucedemo.com/'

# Test 1 not passing usernname and password clicking on submit button

# Test 2 passing only username
USERNAME='standard_user'

# Test 3 passing only password
PASSWORD='secret_sauce'

# Test 4 passing invalid cred
USER='NIYOG'
PASS='Test@123'

# Test 5 passing valid cred
NAME='standard_user'
CRED='secret_sauce'

class Test_login():

    @pytest.fixture()
    def test_invoke(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        self.driver=webdriver.Chrome(options=chrome_options)
        # self.driver=webdriver.Chrome()
        wait=WebDriverWait(self.driver, 60)
        self.driver.get(URL)
        Titlecheck=wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="login_logo"]')))
        assert Titlecheck.text=='Swag Labs'

    def test_1(self,test_invoke):
        wait=WebDriverWait(self.driver, 60)
        self.driver.find_element(By.ID, 'login-button').click()
        h3titlecheck=wait.until(EC.presence_of_element_located((By.TAG_NAME, 'h3')))
        assert h3titlecheck.text=='Epic sadface: Username is required'

    def test_2(self,test_invoke):
        wait=WebDriverWait(self.driver, 60)
        self.driver.find_element(By.NAME, 'user-name').send_keys(USERNAME)
        self.driver.find_element(By.ID, 'login-button').click()
        h3titlecheck=wait.until(EC.presence_of_element_located((By.TAG_NAME, 'h3')))
        assert h3titlecheck.text=='Epic sadface: Password is required'

    def test_3(self,test_invoke):
        wait=WebDriverWait(self.driver, 60)
        self.driver.find_element(By.ID, 'password').send_keys(PASSWORD)
        self.driver.find_element(By.ID, 'login-button').click()
        h3titlecheck=wait.until(EC.presence_of_element_located((By.TAG_NAME, 'h3')))
        assert h3titlecheck.text=='Epic sadface: Username is required'

    def test_4(self,test_invoke):
        wait=WebDriverWait(self.driver, 60)
        self.driver.find_element(By.NAME, 'user-name').send_keys(USER)
        self.driver.find_element(By.ID, 'password').send_keys(PASS)
        self.driver.find_element(By.ID, 'login-button').click()
        h3TitleCheck=wait.until(EC.presence_of_element_located((By.TAG_NAME, 'h3')))
        assert h3TitleCheck.text=='Epic sadface: Username and password do not match any user in this service'

    def test_5(self,test_invoke):
        wait=WebDriverWait(self.driver, 60)
        self.driver.find_element(By.NAME, 'user-name').send_keys(NAME)
        self.driver.find_element(By.ID, 'password').send_keys(CRED)
        self.driver.find_element(By.ID, 'login-button').click()
        h3TitleCheck=wait.until(EC.presence_of_element_located((By.TAG_NAME, 'span')))
        assert h3TitleCheck.text=='Products'






