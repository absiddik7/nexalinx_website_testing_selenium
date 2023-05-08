from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class NexalinxHomePageTest(unittest.TestCase):

    def setUp(self): 
        self.driver = webdriver.Chrome("D:\QA\Website_Nexalinx_Testing\drivers")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_homepage(self):
        driver = self.driver
        driver.get("https://www.nexalinx.com/")
        sleep(5)

        # Verify the presence of the site logo
        logo = driver.find_element(By.XPATH, "//img[contains(@alt,'logo')]")
        self.assertTrue(logo.is_displayed())
        logo.screenshot('logo.png') # take screenshot of logo

        # verify click on the logo navigate to home page
        logo.click()
        sleep(5)
        self.assertEqual(driver.current_url, "https://www.nexalinx.com/#/home")

        # Verify the presence of the navigation menu
        navigation_menu = driver.find_element(By.ID, "basic-navbar-nav")
        self.assertTrue(navigation_menu.screenshot)
        navigation_menu.screenshot('navbar.png') # take screenshot of navigation menu


        # verfiy click on the nav item service open dropdown menu
        nav_item = driver.find_element(By.ID, "basic-nav-dropdown")
        item_text = nav_item.text
        if item_text == "Services":
            nav_item.click()
            sleep(5)
            #-self.assertTrue(nav_item.screenshot)
            

        # Verify the presence of the call to action button in the hero section
       # call_to_action_btn = driver.find_element_by_css_selector(".hero-section .btn")
       # self.assertTrue(call_to_action_btn.is_displayed())
       # self.assertEqual(call_to_action_btn.text, "Get Started")

        # Verify the presence of the features section
       # features_section = driver.find_element_by_css_selector(".features-section")
        #self.assertTrue(features_section.is_displayed())

        # Verify the presence of the footer section
       # footer_section = driver.find_element_by_css_selector(".footer-section")
       # self.assertTrue(footer_section.is_displayed())

    def tearDown(self):
        self.driver.close

if __name__ == "__main__":
    unittest.main()