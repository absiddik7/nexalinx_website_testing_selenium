from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import utils.config as config

class HomePageTest(unittest.TestCase):


    def setUp(self): 
        self.driver = webdriver.Chrome(config.CHROME_DRIVER_PATH)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.scroll_to_element = "arguments[0].scrollIntoView();"

    
    
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
        slider = self.driver.find_element(By.XPATH, "//div[contains(@class,'carousel slide')]")
        self.assertTrue(slider.is_displayed())

        # verify carousel slide automatically slides
        slider = self.driver.find_element(By.XPATH, "//div[contains(@class,'carousel slide')]")
        # Wait for the carousel slide to change
        old_slide_text = self.driver.find_element(By.XPATH, "//div[@class='active carousel-item']//h1").text
        # Wait for the active slide to change after the time interval
        sleep(8)
        new_slide_text = self.driver.find_element(By.XPATH, "//div[@class='active carousel-item']//h1").text
        self.assertNotEqual(old_slide_text, new_slide_text)


        self.driver.quit()

    def test_navbar(self):
        self.driver.get(config.BASE_URL)
        sleep(5)

        # verify clicking on the nav item Home open correct page
        nav_item = self.driver.find_element(By.LINK_TEXT, "Home")
        nav_item.click()
        self.assertEqual(self.driver.current_url, config.HOME_PAGE_URL)
        sleep(3)

        # verify clicking on the nav item Service open dropdown menu
        nav_item = self.driver.find_element(By.LINK_TEXT, "Services")
        nav_item.click()
        nav_dropdown = self.driver.find_element(By.XPATH, "//div[contains(@class,'dropdown-menu show')]")
        self.assertTrue(nav_dropdown.is_displayed())
        sleep(3)

        # verify clicking on the nav item Technologies open dropdown menu
        nav_item = self.driver.find_element(By.LINK_TEXT, "Technologies")
        nav_item.click()
        nav_dropdown = self.driver.find_element(By.XPATH, "//div[contains(@class,'dropdown-menu show')]")
        self.assertTrue(nav_dropdown.is_displayed())
        sleep(3)
  
        # verify clicking on the nav item Portfolio open correct page
        nav_item = self.driver.find_element(By.LINK_TEXT, "Portfolio")
        nav_item.click()
        self.assertEqual(self.driver.current_url, config.PORTFOLIO_PAGE_URL)
        sleep(3)

        # verify clicking on the nav item Blog open correct page
        nav_item = self.driver.find_element(By.LINK_TEXT, "Blog")
        nav_item.click()
        self.assertEqual(self.driver.current_url, config.BLOG_PAGE_URL)
        sleep(3)

        # verify clicking on the nav item About US open dropdown menu
        nav_item = self.driver.find_element(By.LINK_TEXT, "About US")
        nav_item.click()
        nav_dropdown = self.driver.find_element(By.XPATH, "//div[contains(@class,'dropdown-menu show')]")
        self.assertTrue(nav_dropdown.is_displayed())
        sleep(3)

        # verify clicking on the nav item About US open correct page
        about_us_dropdown_item = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/a[1]/a[1]")
        about_us_dropdown_item.click()
        self.assertEqual(self.driver.current_url, config.ABOUT_US_PAGE_URL)
        sleep(3)

        # verify clicking on the nav item Our Team open correct page
        about_us_nav_item = self.driver.find_element(By.LINK_TEXT, "About US")
        about_us_nav_item.click()
        sleep(3)
        our_team_dropdown_item = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/a[1]/a[2]")
        our_team_dropdown_item.click()
        self.assertEqual(self.driver.current_url, config.OUR_TEAM_PAGE_URL)
        sleep(3)

        self.driver.quit()

    def test_schedule_meeting(self):
        driver = self.driver
        driver.get(config.BASE_URL)
        sleep(5)

        # Javascript expression to scroll to a particular element
        js_code = "arguments[0].scrollIntoView();"

        # The WebElement you want to scroll to
        schedule_meeting_form = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/section[4]/div[1]/div[1]/div[2]/form[1]")
        schedule_meeting_h1 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/section[4]/div[1]/div[1]/div[2]/form[1]/div[1]/h3[1]")

        # verify that schedule meeting is displayed
        driver.execute_script(js_code, schedule_meeting_form, schedule_meeting_h1)
        sleep(5)
        self.assertTrue(schedule_meeting_h1.is_displayed(), "Schedule Meeting is not displayed")
        self.assertTrue(schedule_meeting_form.is_displayed(), "Schedule Meeting form is not displayed")

        sleep(5)
        self.driver.quit()

    def test_about_us(self):
        driver = self.driver
        driver.get(config.BASE_URL)
        sleep(5)

        # Javascript expression to scroll to a particular element
        js_code = "arguments[0].scrollIntoView();"

        about_us_section = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/section[6]/div[1]/div[1]/div[1]")
        read_more_button = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/section[6]/div[1]/div[1]/div[1]/div[1]/a[1]/button[1]")
        # verify that schedule meeting is displayed
        driver.execute_script(js_code, about_us_section, read_more_button)
        sleep(8)
        self.assertTrue(about_us_section.is_displayed(), "About Us is not displayed")
        self.assertTrue(read_more_button.is_displayed(), "Read More button is not displayed")

        # verify clicking on read more button opens correct page
        read_more_button.click()
        self.assertEqual(self.driver.current_url, config.ABOUT_US_PAGE_URL)

        sleep(3)
        self.driver.quit()

    
    def test_technology_partner(self):
        driver = self.driver
        driver.get(config.BASE_URL)
        sleep(5)

        # Javascript expression to scroll to a particular element
        js_code = "arguments[0].scrollIntoView();"

        technology_partner_section = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/section[7]")

        # verify that technology partner section is displayed
        driver.execute_script(js_code, technology_partner_section)
        sleep(5)
        self.assertTrue(technology_partner_section.is_displayed(), "Technology Partner section is not displayed")
        
        # more to test here

        driver.quit()


    def test_our_recent_works(self):
        driver = self.driver
        driver.get(config.BASE_URL)
        sleep(5)

        # Javascript expression to scroll to a particular element
        js_code = "arguments[0].scrollIntoView();"

        our_recent_works = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/section[11]/div[1]")

        # verify that our recent works section is displayed
        driver.execute_script(js_code, our_recent_works)
        sleep(5)

        self.assertTrue(our_recent_works.is_displayed(), "Our Recent Works section is not displayed")

        # verify owl-carousel owl-theme slider-custom owl-loaded owl-drag sliding automatically
        slider = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/section[11]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]")
        self.assertTrue(slider.is_displayed(), "Slider is not displayed")
        
        sleep(3)


        # more to test here

        driver.quit()

    def test_footer(self):
        driver = self.driver
        driver.get(config.BASE_URL)
        sleep(5)

        # Javascript expression to scroll to a particular element
        scroll_to_element = self.scroll_to_element

        back_to_top_button = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[5]/button[1]/button[1]")
        footer = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]")
        
        # verify that footer is displayed
        driver.execute_script(scroll_to_element, footer)
        self.assertTrue(footer.is_displayed(), "Footer is not displayed")
        sleep(3)

        # verify that footer items are displayed

        about_nexalinx_footer = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]")
        services_footer = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[2]/ul[1]")
        us_address_footer = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[3]/ul[1]")
        bd_address_footer = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[4]/ul[1]")
        
        self.assertTrue(about_nexalinx_footer.is_displayed(), "About Nexalinx footer is not displayed")
        self.assertTrue(services_footer.is_displayed(), "Services footer is not displayed")
        self.assertTrue(us_address_footer.is_displayed(), "US Address footer is not displayed")
        self.assertTrue(bd_address_footer.is_displayed(), "BD Address footer is not displayed")
        sleep(3)



        
        # verify that back to top button is displayed
        self.assertTrue(back_to_top_button.is_displayed(), "Back to top button is not displayed")
        # verify clicking on back to top button scrolls to top
        back_to_top_button.click()
        sleep(5)
        slider = self.driver.find_element(By.XPATH, "//div[contains(@class,'carousel slide')]")
        self.assertTrue(slider.is_displayed())




        sleep(5)
        
    def tearDown(self):
        self.driver.close

if __name__ == "__main__":
    unittest.main()
