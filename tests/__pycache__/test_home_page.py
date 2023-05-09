from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utils.config as config

class NexalinxHomePageTest(unittest.TestCase):

    def setUp(self): 
        self.driver = webdriver.Chrome(config.CHROME_DRIVER_PATH)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_homepage(self):
        #driver = self.driver
        self.driver.get(config.BASE_URL)
        sleep(5)

        # Verify the presence of the site logo
        logo = self.driver.find_element(By.XPATH, "//img[contains(@alt,'logo')]")
        self.assertTrue(logo.is_displayed())
        #logo.screenshot('logo.png') # take screenshot of logo

        # verify that click on the logo navigate to home page
        logo.click()
        sleep(3)
        self.assertEqual(self.driver.current_url, config.HOME_PAGE_URL)

        # Verify the presence of the navigation menu
        navigation_menu = self.driver.find_element(By.ID, "basic-navbar-nav")
        self.assertTrue(navigation_menu.is_displayed())
        #navigation_menu.screenshot('navbar.png') # take screenshot of navigation menu

        # Verify Get In Touch button open correct page
        button = self.driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/div[1]/div[1]/div[3]/a[1]/button[1]')
        button.click()
        self.assertEqual(self.driver.current_url, config.CONTACT_PAGE_URL)
        sleep(3)

        # verify carousel slide shows
        self.driver.find_element(By.LINK_TEXT, "Home").click()
        carousel = self.driver.find_element(By.XPATH, "//div[contains(@class,'carousel slide')]")
        self.assertTrue(carousel.is_displayed())

        # verify carousel slide automatically slides
        carousel = self.driver.find_element(By.XPATH, "//div[contains(@class,'carousel slide')]")
        # Wait for the carousel slide to change
        old_slide_text = self.driver.find_element(By.XPATH, "//div[@class='active carousel-item']//h1").text
        # Wait for the active slide to change after the time interval
        sleep(5)
        new_slide_text = self.driver.find_element(By.XPATH, "//div[@class='active carousel-item']//h1").text
        self.assertNotEqual(old_slide_text, new_slide_text)


        self.driver.quit()

    def test_navbar(self):
        self.driver.get(config.BASE_URL)
        sleep(5)

        # verfiy clicking on the nav item Home open correct page
        nav_item = self.driver.find_element(By.LINK_TEXT, "Home")
        nav_item.click()
        self.assertEqual(self.driver.current_url, config.HOME_PAGE_URL)
        sleep(3)

        # verfiy clicking on the nav item Service open dropdown menu
        nav_item = self.driver.find_element(By.LINK_TEXT, "Services")
        nav_item.click()
        nav_dropdown = self.driver.find_element(By.XPATH, "//div[contains(@class,'dropdown-menu show')]")
        self.assertTrue(nav_dropdown.is_displayed())
        sleep(3)

        # verfiy clicking on the nav item Technologies open dropdown menu
        nav_item = self.driver.find_element(By.LINK_TEXT, "Technologies")
        nav_item.click()
        nav_dropdown = self.driver.find_element(By.XPATH, "//div[contains(@class,'dropdown-menu show')]")
        self.assertTrue(nav_dropdown.is_displayed())
        sleep(3)

        # verfiy clicking on the nav item Portfolio open correct page
        nav_item = self.driver.find_element(By.LINK_TEXT, "Portfolio")
        nav_item.click()
        self.assertEqual(self.driver.current_url, config.PORTFOLIO_PAGE_URL)
        sleep(3)

        # verfiy clicking on the nav item Blog open correct page
        nav_item = self.driver.find_element(By.LINK_TEXT, "Blog")
        nav_item.click()
        self.assertEqual(self.driver.current_url, config.BLOG_PAGE_URL)
        sleep(3)

        # verfiy clicking on the nav item About US open dropdown menu
        nav_item = self.driver.find_element(By.LINK_TEXT, "About US")
        nav_item.click()
        nav_dropdown = self.driver.find_element(By.XPATH, "//div[contains(@class,'dropdown-menu show')]")
        self.assertTrue(nav_dropdown.is_displayed())
        sleep(3)



        self.driver.quit()


    
    def tearDown(self):
        self.driver.close

if __name__ == "__main__":
    unittest.main()