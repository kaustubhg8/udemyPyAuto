from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options
import time
# options = Options()
cap = {"EDGE_CHROMIUM_DRIVER":{"ms:edgeOptions":{"args":["-disable-notifications","-start-maximized"]},"ms:edgeChromium":"true"}}

driver = webdriver.Edge(EdgeChromiumDriverManager().install(),options = options)
driver.get("https://teams.microsoft.com/l/message/19:52ecbb01-4145-4865-8413-dff15dba8670_e6048679-23f5-4391-83f7-f0bb465535eb@unq.gbl.spaces/1697530514069?context=%7B%22contextType%22%3A%22chat%22%7D")

time.sleep(5)

driver.close()
driver.quit()
