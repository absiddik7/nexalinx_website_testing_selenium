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
   git clone https://github.com/absiddik7/API_Testing_Python
   ```
4. Navigate to the project directory:
   ```bash
   cd nexalin test
   ```

## Configuration

Before running the tests, you need to configure the test suite by editing the `config.py` file. Update the following settings:

- `BASE_URL`: Set this to the URL of the Nexalinx website.

- `BROWSER`: Specify the browser you want to use for testing (e.g., "chrome" or "firefox").

- Other settings like login credentials, URLs, or test data can also be configured in this file as needed.
- python run_tests.py
