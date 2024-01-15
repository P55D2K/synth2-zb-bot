from selenium.webdriver.chrome.options import Options

def get_chrome_options(devmode):
  chrome_options = Options()
  chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
  chrome_options.add_argument('--log-level=3')
  chrome_options.add_argument("--start-maximized")
  chrome_options.add_argument("--disable-extensions")
  if not devmode:
    chrome_options.add_argument("--headless")
  return chrome_options