import unittest
from unittest.result import failfast
from selenium import webdriver
import utils.config as config
from time import sleep
from selenium.webdriver.common.by import By

class OurTeamPageTest(unittest.TestCase):
    

	def setUp(self):
		self.driver = webdriver.Chrome(config.CHROME_DRIVER_PATH)
		self.driver.maximize_window()
		self.driver.implicitly_wait(10)
		self.scroll_to_element = "arguments[0].scrollIntoView();"
	
	def test_about_us_page(self):
		self.driver.get(config.BASE_URL)
		sleep(5)

		our_team_dropdown_item = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/a[1]/a[2]")
		our_team_dropdown_item.click()
		self.assertEqual(self.driver.current_url, config.OUR_TEAM_PAGE_URL)
		sleep(3)

		# verify Who We Are text is displayed
		who_we_are = self.driver.find_element(By.XPATH, "//h2[contains(text(),'Who We Are')]")
		self.assertTrue(who_we_are.is_displayed())
		sleep(3)

		# verify Our Vision text is displayed
		our_vision = self.driver.find_element(By.XPATH, "//h5[contains(text(),'Our Vision')]")
		self.assertTrue(our_vision.is_displayed())
		sleep(3)

		#verify clicking on Our Vision read more button open correct page
		read_more_button = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/section[2]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/a[1]")
		read_more_button.click()
		self.assertEqual(self.driver.current_url, config.OUR_VISION_PAGE_URL)
		sleep(3)

		






		


