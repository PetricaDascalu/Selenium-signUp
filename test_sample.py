from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest

class TestSignUp():
   @pytest.fixture()
   def test_setup(self):
      global driver
      PATH = r"C:\Program Files (x86)\chromedriver.exe"
      driver = webdriver.Chrome(PATH)
      driver.implicitly_wait(10)
      driver.maximize_window()
      yield 
      #driver.close()
      #driver.quit()
      print("Test Completed")
   

   def test_signup(self,test_setup):
      driver.get("https://politrip.com/account/sign-up")

#clicking ok cookies still doesnt close the window
      #cookies = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "cookiescript_close")))
      #cookies.click()

      
      driver.find_element_by_id('first-name').send_keys("Petrica")
      driver.find_element_by_id('last-name').send_keys("Dascalu")
      driver.find_element_by_id('email').send_keys("asd@gmail.com")
      driver.find_element_by_id('sign-up-password-input').send_keys("Qwertyuiop11")
      driver.find_element_by_id('sign-up-confirm-password-input').send_keys("Qwertyuiop11")
      select = Select(driver.find_element_by_id('sign-up-heard-input'))
      select.select_by_value('other')
      driver.implicitly_wait(5)

#Sign up with facebook / google / isntagram / VK
      button = driver.find_element_by_xpath('//*[@id="socialmedia-account-component-div"]/div[1]/div[1]')
      href_data = button.get_attribute('href')
      if href_data is None:
         is_clickable = False

      button = driver.find_element_by_xpath('//*[@id="socialmedia-account-component-div"]/div[1]/div[2]')
      href_data = button.get_attribute('href')
      if href_data is None:
         is_clickable = False
      
      button = driver.find_element_by_xpath('//*[@id="socialmedia-account-instagram-button"]')
      href_data = button.get_attribute('href')
      if href_data is None:
         is_clickable = False
      
      button = driver.find_element_by_xpath('//*[@id="socialmedia-account-component-div"]/div[2]/div')
      href_data = button.get_attribute('href')
      if href_data is None:
         is_clickable = False
         
      button = driver.find_element_by_xpath('/html/body/app-root/app-access-account/app-page-template/div/app-sign-up/app-sign-in-container/div/div[2]/div/a')
      href_data = button.get_attribute('href')
      if href_data is None:
         is_clickable = False
         
# scroll down the page
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      driver.implicitly_wait(5)

# click on Sign up button
      sign_up = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, " qa_loader-button")))
      sign_up.click()

# check if the second page has loaded
      driver.find_element_by_xpath('/html/body/app-root/app-access-account/app-page-template/div/app-sign-up-type/div/app-sign-up-as/app-sign-in-container/div/div[1]/div[1]/span[2]')
     # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

      x = driver.title
      assert x == "Sign up | Politrip"









