import unittest
from selenium import webdriver
import utils.config as config
from time import sleep
from selenium.webdriver.common.by import By

class BlogPageTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(config.CHROME_DRIVER_PATH)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.scroll_to_element = "arguments[0].scrollIntoView();"
        

    def test_blog_page(self):
        self.driver.get(config.BASE_URL)
        sleep(5)

        # verfiy clicking on the nav item Blog open correct page
        blog_navbar = self.driver.find_element(By.LINK_TEXT, "Blog")
        blog_navbar.click()
        self.assertEqual(self.driver.current_url, config.BLOG_PAGE_URL)
        sleep(5)
        # verify carsoel slider auto play
        carousel_slider = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]")
        self.assertTrue(carousel_slider.is_displayed())
        #self.assertTrue(read_more_btn.is_displayed())
        initial_position = carousel_slider.location['x']
        sleep(3)

		# Get the current position of the slider element
        current_position = carousel_slider.location['x']
        # Check if the position has changed
        if current_position != initial_position:
            self.assertTrue(True, "Slider is sliding automatically")
        else:
            self.assertTrue(False, "Slider is not sliding automatically")
        
        sleep(5)
      
        
        self.driver.quit()
        

    def tearDown(self):
        self.driver.close


    if __name__ == "__main__":
        unittest.main()
    
