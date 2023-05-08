#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from random import randint
#from time import sleep

#driver = webdriver.Chrome("D:\Python\Login_Selenium_Automation\drivers")

##Open the website:

#driver.get("https://www.nexalinx.com/")

##Verify the title:
#expectedTitle = "NexaLinX - Digital Transformation and Web Development Services"
#actualTitle = driver.getTitle()
#assertEquals(expectedTitle, actualTitle)


##Verify the logo:
#logo = driver.findElement(By.cssSelector("img[class='site-logo']"));
#assertTrue(logo.isDisplayed());


##Verify the navigation menu:
#navItems = driver.findElements(By.cssSelector("ul[class='nav-menu'] > li"));
#assertEquals(6, navItems.size());

#expectedNavItems = Arrays.asList("Home", "About Us", "Services", "Portfolio", "Blog", "Contact Us");
#actualNavItems = navItems.stream().map(WebElement::getText).collect(Collectors.toList());

#assertEquals(expectedNavItems, actualNavItems);


##Verify the hero section:
#heroTitle = driver.findElement(By.cssSelector("h1[class='hero-title']"));
#heroSubtitle = driver.findElement(By.cssSelector("h2[class='hero-subtitle']"));
#heroCta = driver.findElement(By.cssSelector("a[class='btn btn-primary']"));

#assertEquals("Transform Your Business", heroTitle.getText());
#assertEquals("with Innovative Digital Solutions", heroSubtitle.getText());
#assertTrue(heroCta.isDisplayed());
#assertEquals("Get in Touch", heroCta.getText());


##Verify the services section:
#servicesSection = driver.findElement(By.cssSelector("section[id='services']"));
#assertTrue(servicesSection.isDisplayed());

#serviceItems = servicesSection.findElements(By.cssSelector("div[class='service-item']"));
#assertEquals(3, serviceItems.size());

#expectedServiceTitles = Arrays.asList("Web Development", "Mobile App Development", "Digital Marketing");
#actualServiceTitles = serviceItems.stream().map(item -> item.findElement(By.cssSelector("h3")).getText()).collect(Collectors.toList());
#assertEquals(expectedServiceTitles, actualServiceTitles);

##Verify the footer section:
#footer = driver.findElement(By.cssSelector("footer"));
#assertTrue(footer.isDisplayed());

#footerLogo = footer.findElement(By.cssSelector("img[class='footer-logo']"));
#assertTrue(footerLogo.isDisplayed());

#footerSocialLinks = footer.findElement(By.cssSelector("div[class='social-links']"));
#assertTrue(footerSocialLinks.isDisplayed());

#footerNavItems = footer.findElements(By.cssSelector("ul[class='footer-menu'] > li"));
#assertEquals(4, footerNavItems.size());

#expectedFooterNavItems = Arrays.asList("Home", "About Us", "Services", "Contact Us");
#actualFooterNavItems = footerNavItems.stream().map(WebElement::getText).collect(Collectors.toList());
#assertEquals(expectedFooterNavItems, actualFooterNavItems);

