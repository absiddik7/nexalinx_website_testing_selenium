# Automated Testing for nexalinx.com using Selenium and Python
This repository contains automated tests for [nexalinx.com](https://www.nexalinx.com/) using Selenium and Python. Automated testing is crucial for ensuring the functionality and reliability of web applications. 
With Selenium and Python, you can automate the testing of various scenarios on the Nexalinx website, saving time and reducing the risk of human errors.

## Prerequisites

Before running the tests, make sure you have the following prerequisites installed:

- **Python**: Make sure you have Python installed on your system. You can download it from the [Python website](https://www.python.org/downloads/).

- **Selenium**: Install the Selenium library using pip:

  ```bash
  pip install selenium
  ```
- **WebDriver**: Download the appropriate WebDriver for your browser and make sure it's in your system's PATH. You can download WebDriver for different browsers here:
  - [ChromeDriver](https://sites.google.com/chromium.org/driver/)
  - [GeckoDriver (for Firefox)](https://github.com/mozilla/geckodriver/releases)
  - [EdgeDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

## Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/absiddik7/nexalinx_website_testing_selenium
   ```
4. Navigate to the project directory:
   ```bash
   cd nexalinx_website_testing_selenium
   ```

## Usage
This project uses Pytest for writing and running test cases. The test cases are written in Python and can be found under the 'tests' directory.

## Running all the Tests
   To run all the test cases, use the following command:
   ```bash
   pytest
   ```
      
## Running a Specific Test
  To run a specific test cases, use the following command (ex: pytest test_folder/test_file_name.py):
  ```bash
  pytest test/test_home_page.py
  ```
