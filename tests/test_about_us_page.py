import unittest
from unittest.result import failfast
from selenium import webdriver
import utils.config as config
from time import sleep
from selenium.webdriver.common.by import By

class AboutUsPageTest(unittest.TestCase):
    
	def setUp(self):
		self.driver = webdriver.Chrome(config.CHROME_DRIVER_PATH)
		self.driver.maximize_window()
		self.driver.implicitly_wait(10)
		self.scroll_to_element = "arguments[0].scrollIntoView();"
	
	def test_about_us_page(self):
		self.driver.get(config.BASE_URL)
		sleep(5)

		# verfiy clicking on the nav item About US open correct page
		about_us_dropdown_item = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/a[1]/a[1]")
		about_us_dropdown_item.click()
		self.assertEqual(self.driver.current_url, config.ABOUT_US_PAGE_URL)
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

		# verify Our Mission text is displayed
		our_mission = self.driver.find_element(By.XPATH, "//h5[contains(text(),'Our Mission')]")
		self.assertTrue(our_mission.is_displayed())
		sleep(3)

		#verify clicking on Our Mission read more button open correct page
		about_us_dropdown_item = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/a[1]/a[1]")
		about_us_dropdown_item.click()
		read_more_button = self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/section[2]/section[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/a[1]")
		read_more_button.click()
		self.assertEqual(self.driver.current_url, config.OUR_MISSION_PAGE_URL)
		sleep(3)


		# verify A Glimpse Of Our Offices text is displayed
		a_glimpse_of_our_offices = self.driver.find_element(By.XPATH, "//h2[contains(text(),'A Glimpse Of Our Offices')]")
		self.assertTrue(a_glimpse_of_our_offices.is_displayed())
		sleep(3)

		#verify Our Clients text is displayed
		our_clients = self.driver.find_element(By.XPATH, "//h2[contains(text(),'Our Clients')]")
		self.assertTrue(our_clients.is_displayed())
		sleep(3)






		


