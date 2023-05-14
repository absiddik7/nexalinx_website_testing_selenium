import unittest
from unittest.result import failfast
from selenium import webdriver
import utils.config as config
from time import sleep
from selenium.webdriver.common.by import By

class ContactPageTest(unittest.TestCase):
    
 
	def setUp(self):
		self.driver = webdriver.Chrome(config.CHROME_DRIVER_PATH)
		self.driver.maximize_window()
		self.driver.implicitly_wait(10)
		self.scroll_to_element = "arguments[0].scrollIntoView();"
	
	def test_contact_page(self):
		self.driver.get(config.BASE_URL)
		sleep(5)

		# Verify Get In Touch button open correct page
		button = self.driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/div[1]/div[1]/div[3]/a[1]/button[1]')
		button.click()
		self.assertEqual(self.driver.current_url, config.CONTACT_PAGE_URL)
		sleep(3)

		# verify map is displayed
		map = self.driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/section[2]/div[2]/div[1]/div[2]/div[1]/iframe[1]')
		self.driver.execute_script(self.scroll_to_element, map)
		sleep(5)
		self.assertTrue(map.is_displayed())
		sleep(3)

		#varify Our Headquarter text is displayed
		our_headquarter = self.driver.find_element(By.XPATH, "//h2[contains(text(),'Our Headquarter')]")
		self.assertTrue(our_headquarter.is_displayed())
		sleep(3)

		# verify USA adress is displayed
		usa_name = self.driver.find_element(By.XPATH, "//h4[contains(text(),'United States')]")
		usa_address = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/section[2]/div[2]/div[1]/div[2]/div[2]/div[1]/ul[1]/li[1]/label[1]")
		usa_phone = self.driver.find_element(By.XPATH, "//label[contains(text(),'(332) 203-6066')]")
		self.driver.execute_script(self.scroll_to_element, usa_name, usa_address, usa_phone)
		sleep(5)
		self.assertTrue(usa_name.is_displayed())
		self.assertTrue(usa_address.is_displayed())
		self.assertTrue(usa_phone.is_displayed())
		sleep(3)




		


