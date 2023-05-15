import unittest
from selenium import webdriver
import utils.config as config
from time import sleep
from selenium.webdriver.common.by import By


class TechnologiesPageTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(config.CHROME_DRIVER_PATH)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.scroll_to_element = "arguments[0].scrollIntoView();"
        

    def test_technologies_page(self):
        self.driver.get(config.BASE_URL)
        sleep(5)

        # verfiy clicking on the nav item Blog open correct page
        tech_navbar = self.driver.find_element(By.LINK_TEXT, "Technologies")
        tech_navbar.click()
        nav_dropdown = self.driver.find_element(By.XPATH, "//div[contains(@class,'dropdown-menu show')]")
        self.assertTrue(nav_dropdown.is_displayed())
        sleep(3)

        # verify clicking on the Angularjs open correct page
        angularjs_tag = self.driver.find_element(By.XPATH, "//a[contains(@href,'#/angular')]")
        self.click_tech_items(angularjs_tag, config.ANGULARJS_PAGE_URL)

        # verify clicking on the Reactjs open correct page
        reactjs_tag = self.driver.find_element(By.XPATH, "//a[contains(@href,'#/reactjs')]")
        self.click_tech_items(reactjs_tag, config.REACTJS_PAGE_URL)

        # verify clicking on the Nodejs open correct page
        nodejs_tag = self.driver.find_element(By.XPATH, "//a[contains(@href,'#/nodejs')]")
        self.click_tech_items(nodejs_tag, config.NODEJS_PAGE_URL)

        # verify clicking on the Python open correct page
        python_tag = self.driver.find_element(By.XPATH, "//a[contains(@href,'#/python')]")
        self.click_tech_items(python_tag, config.PYTHON_PAGE_URL)

        # verify clicking on the Vuew JS open correct page
        vuejs_tag = self.driver.find_element(By.XPATH, "//a[contains(@href,'#/vuejs')]")
        self.click_tech_items(vuejs_tag, config.VUEJS_PAGE_URL)

        # verify clicking on the Magento open correct page
        magento_tag = self.driver.find_element(By.XPATH, "//a[contains(@href,'#/magento')]")
        self.click_tech_items(magento_tag, config.MAGNETO_PAGE_URL)

        # verify clicking on the PHP open correct page
        php_tag = self.driver.find_element(By.XPATH, "//a[contains(@href,'#/php')]")
        self.click_tech_items(php_tag, config.PHP_PAGE_URL)

        # verify clicking on the Laravel open correct page
        laravel_tag = self.driver.find_element(By.XPATH, "//a[contains(@href,'#/laravel')]")
        self.click_tech_items(laravel_tag, config.LARAVEL_PAGE_URL)

        # verify clicking on the Wordpress open correct page
        wordpress_tag = self.driver.find_element(By.XPATH, "//a[contains(@href,'#/wordpress')]")
        self.click_tech_items(wordpress_tag, config.WORDPRESS_PAGE_URL)

        # verify clicking on the ASP.NET MVC open correct page
        aspnet_tag = self.driver.find_element(By.XPATH, "//a[contains(@href,'#/aspnet')]")
        self.click_tech_items(aspnet_tag, config.ASPNET_PAGE_URL)


        self.driver.quit()


    def click_tech_items(self, element, page_url):
        element.click()
        self.assertEqual(self.driver.current_url, page_url)
        sleep(3)
        self.driver.back()
        sleep(3)
        tech_navbar = self.driver.find_element(By.LINK_TEXT, "Technologies")
        tech_navbar.click()
        sleep(3)
        
        
    def tearDown(self):
        self.driver.close


    if __name__ == "__main__":
        unittest.main()
    
