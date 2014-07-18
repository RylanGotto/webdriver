import logging 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class WebDriver:
	def __init__(self, sizew, sizeh, browser, starturl):
	    self.window_sizew = sizew
	    self.window_sizeh = sizeh
	    self.browser_type =  browser
	    self.start_url = "http://%s" % starturl
	    self.driver = None
	    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='logging.log',
                    filemode='a')

	def create_browser(self):
		if self.browser_type is 'firefox':
			driver = webdriver.Firefox()
		elif self.browser_type == 'internet':
			driver = webdriver.Ie()
		else:
			errmsg = "invalid browser type"
			print errmsg
			logging.WARNING(errmsg)
		driver.set_window_size(self.window_sizew, self.window_sizeh)
		driver.get(self.start_url)



