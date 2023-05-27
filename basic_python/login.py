import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestFunctionalLogin(unittest.TestCase): # TEST SCENARIO

    def setUp(self): # BUKA BROWSER
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_success_login_with_valid_email_pass(self): # TEST CASE
        self.browser.get("https://barru.pythonanywhere.com/daftar") # BUKA LINK WEB
        time.sleep(3)
        self.browser.find_element(By.ID, 'email').send_keys('dedeghulam@jagoqa.com')
        time.sleep(3)
        self.browser.find_element(By.CSS_SELECTOR, 'input#password').send_keys('dedeghulam')
        time.sleep(3)
        self.browser.find_element(By.XPATH, '/html/body/div/div[2]/form/input[3]').click()
        time.sleep(3)
        
        pop_up = self.browser.find_element(By.ID, 'swal2-title').text
        message_popup = self.browser.find_element(By.ID, 'swal2-content').text

        #VERIFIKASI 
        self.assertIn('Welcome', pop_up)
        self.assertEqual('Anda Berhasil Login', message_popup)

    def test_failed_login_with_invalid_email_pass(self): # TEST CASE
        self.browser.get("https://barru.pythonanywhere.com/daftar") # BUKA LINK WEB
        time.sleep(3)
        self.browser.find_element(By.ID, 'email').send_keys('wurimunthe@gmail.com')
        time.sleep(3)
        self.browser.find_element(By.CSS_SELECTOR, 'input#password').send_keys('12345')
        time.sleep(3)
        self.browser.find_element(By.XPATH, '/html/body/div/div[2]/form/input[3]').click()
        time.sleep(3)
        
        pop_up = self.browser.find_element(By.ID, 'swal2-title').text
        message_popup = self.browser.find_element(By.ID, 'swal2-content').text

        #VERIFIKASI 
        self.assertEqual("User's not found", pop_up)
        self.assertEqual('Email atau Password Anda Salah', message_popup)

    def test_failed_login_with_empty_pass(self): # TEST CASE
        self.browser.get("https://barru.pythonanywhere.com/daftar") # BUKA LINK WEB
        time.sleep(3)
        self.browser.find_element(By.ID, 'email').send_keys('dedeghulam@jagoqa.com')
        time.sleep(3)
        self.browser.find_element(By.CSS_SELECTOR, 'input#password').send_keys('')
        time.sleep(3)
        self.browser.find_element(By.XPATH, '/html/body/div/div[2]/form/input[3]').click()
        time.sleep(3)
        
        pop_up = self.browser.find_element(By.ID, 'swal2-title').text
        message_popup = self.browser.find_element(By.ID, 'swal2-content').text

        #VERIFIKASI 
        self.assertEqual("User's not found", pop_up)
        self.assertEqual('Email atau Password Anda Salah', message_popup)


    def test_failed_login_with_empty_email_pass(self): # TEST CASE
        self.browser.get("https://barru.pythonanywhere.com/daftar") # BUKA LINK WEB
        time.sleep(3)
        self.browser.find_element(By.ID, 'email').send_keys()
        time.sleep(3)
        self.browser.find_element(By.CSS_SELECTOR, 'input#password').send_keys()
        time.sleep(3)
        self.browser.find_element(By.XPATH, '/html/body/div/div[2]/form/input[3]').click()
        time.sleep(3)
        
        pop_up = self.browser.find_element(By.ID, 'swal2-title').text
        message_popup = self.browser.find_element(By.ID, 'swal2-content').text

        #VERIFIKASI 
        self.assertEqual("User's not found", pop_up)
        self.assertEqual('Email atau Password Anda Salah', message_popup)        

    def tearDown(self): # TUTUP BROWSER
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()