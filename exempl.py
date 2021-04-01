from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Conf desable UI
# options = Options()
# options.headless = True
# options.add_argument("--window-size=1920,1200")

DRIVER_PATH = './chromeDriver/chromedriver'
# driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://github.com/login')
user = driver.find_element_by_id('login_field')
password = driver.find_element_by_id('password')
user.send_keys('maykealison@gmail.com')
password.send_keys('senha')
password.send_keys(Keys.ENTER)

# Cria repositorio
driver.get('https://github.com/new')
repository = driver.find_element_by_id('repository_name')
repository_description = driver.find_element_by_id('repository_description')
repository.send_keys('teste_selenium')
repository_description.send_keys('Criando repositorio com selenium')
driver.find_element_by_xpath('//div[@class="js-with-permission-fields"]/button[@type="submit"]').click()

driver.quit()
