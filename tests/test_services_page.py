import unittest
from selenium import webdriver
import utils.config as config
from time import sleep
from selenium.webdriver.common.by import By

class ServicesPageTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(config.CHROME_DRIVER_PATH)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.scroll_to_element = "arguments[0].scrollIntoView();"
        

    def test_blog_page(self):
        self.driver.get(config.BASE_URL)
        sleep(5)

        # verfiy clicking on the nav item Service open dropdown menu
        nav_item = self.driver.find_element(By.LINK_TEXT, "Services")
        nav_item.click()
        nav_dropdown = self.driver.find_element(By.XPATH, "//div[contains(@class,'dropdown-menu show')]")
        self.assertTrue(nav_dropdown.is_displayed())
        sleep(3)
        
		# verify clicking on the Offshore software development  open correct page
        Offshore = self.driver.find_element(By.XPATH, "//a[contains(@href,'#/developmentcompany')]")
        self.click_service_items(Offshore, config.OFFSHORE_PAGE_URL)
        
		# verify clicking on the Full Stack Development open correct page
        full_Stack= self.driver.find_element(By.XPATH, "//a[contains(@href,'#/full-stack-development')]")
        self.click_service_items(full_Stack, config.FULL_STACK_PAGE_URL)
        
		# verify clicking on the Amazon Web Services open correct page
        amazon_Web_Services = self.driver.find_element(By.XPATH, "//a[contains(@href,'#/amazon-web-services')]")
        self.click_service_items(amazon_Web_Services, config.AMAZON_WEB_SERVICES_PAGE_URL)
        
		# verify clicking on the IT Consulting Services open correct page
        it_Consulting = self.driver.find_element(By.XPATH, "//a[contains(@href,'#/it-consulting-services')]")
        self.click_service_items(it_Consulting, config.IT_CONSULTING_PAGE_URL)
        
		# Verify clicking on the Software Maintenance open correct page
        software_maintenance = self.driver.find_element(By.XPATH, "//a[contains(@href,'#/software-maintenance-support-services')]")
        self.click_service_items(software_maintenance, config.SOFTWARE_MAINTEANCE_PAGE_URL)
        
        # Verify clicking on the Software QA open correct page
        software_QA = self.driver.find_element(By.XPATH, "//a[contains(@href,'#/software-qa-and-testing-services')]")
        self.click_service_items(software_QA, config.SOFTWARE_QA_PAGE_URL)
        
		# verify clicking on the UI/UX open correct page
        ui_ux = self.driver.find_element(By.XPATH, "//a[contains(@href,'#/ui-ux-design')]")
        self.click_service_items(ui_ux, config.UI_UX_PAGE_URL)
        
		# verify clicking on the Database Management open correct page
        database_management = self.driver.find_element(By.XPATH, "//a[contains(@href,'#/database-management-services')]")
        self.click_service_items(database_management, config.DATABSE_MANAGEMENT_PAGE_URL)
        
		# verify clicking on the Cyber Security open correct page
        cyber_security = self.driver.find_element(By.XPATH, "//a[contains(@href,'#/cyber-security')]")
        self.click_service_items(cyber_security, config.CYBER_SECURITY_PAGE_URL)
        
        # verify clicking on the Angularjs open correct page
        angularjs = self.driver.find_element(By.XPATH, "//a[contains(@href,'#/angular')]")
        self.click_service_items(angularjs, config.ANGULARJS_PAGE_URL)

        # verify clicking on the Reactjs open correct page
        reactjs = self.driver.find_element(By.XPATH, "//a[contains(@href,'#/reactjs')]")
        self.click_service_items(reactjs, config.REACTJS_PAGE_URL)

        # verify clicking on the Nodejs open correct page
        nodejs = self.driver.find_element(By.XPATH, "//a[contains(@href,'#/nodejs')]")
        self.click_service_items(nodejs, config.NODEJS_PAGE_URL)

        # verify clicking on the Python open correct page
        python = self.driver.find_element(By.XPATH, "//a[contains(@href,'#/python')]")
        self.click_service_items(python, config.PYTHON_PAGE_URL)

        # verify clicking on the Vuew JS open correct page
        vuejs = self.driver.find_element(By.XPATH, "//a[contains(@href,'#/vuejs')]")
        self.click_service_items(vuejs, config.VUEJS_PAGE_URL)

        # verify clicking on the PHP open correct page
        php = self.driver.find_element(By.XPATH, "//a[contains(@href,'#/php')]")
        self.click_service_items(php, config.PHP_PAGE_URL)

        # verify clicking on the Progressive Web App open correct page
        progressive_web = self.driver.find_element(By.XPATH, "//a[contains(@href,'#/progressive-web-app-development')]")
        self.click_service_items(progressive_web, config.PROGRESSIVE_WEB_PAGE_URL)

        # verify clicking on the ERP open correct page
        erp = self.driver.find_element(By.XPATH, "//a[contains(@href,'#/erp-software-development-services')]")
        self.click_service_items(erp, config.ERP_PAGE_URL)

        # verify clicking on the JAVA  open correct page
        java = self.driver.find_element(By.XPATH, "//a[contains(@href,'#/java-development')]")
        self.click_service_items(java, config.JAVA_PAGE_URL)
        
		
    
        self.driver.quit()
        
        

    def click_service_items(self, element, page_url):
        element.click()
        self.assertEqual(self.driver.current_url, page_url)
        sleep(1)
        self.driver.back()
        sleep(1)
        tech_navbar = self.driver.find_element(By.LINK_TEXT, "Services")
        tech_navbar.click()
        sleep(1)
    
	

    def tearDown(self):
        self.driver.close


    if __name__ == "__main__":
        unittest.main()
    
