from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\MSC.Software\Digimat\working")
options.add_argument(r'--profile-directory=Profile 2')
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.get("https://teams.microsoft.com/l/message/19:52ecbb01-4145-4865-8413-dff15dba8670_e6048679-23f5-4391-83f7-f0bb465535eb@unq.gbl.spaces/1697530514069?context=%7B%22contextType%22%3A%22chat%22%7D")

time.sleep(5)

driver.close()
driver.quit()