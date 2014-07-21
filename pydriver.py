import logging 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time

#"\\input[@name='cams_cb_username' and @tabindex='1']")

class WebDriver:
	def __init__(self, starturl):
	    self.start_url = "http://%s" % starturl
	    self.driver = None

	def create_browser(self, args):
		self.browser_type = args[0]
		if self.browser_type == 'firefox':
			self.driver = webdriver.Firefox()
		elif self.browser_type == 'ie':
			self.driver = webdriver.Ie()

		else:
			errmsg = "invalid browser type"
			print errmsg
		self.driver.maximize_window()
		self.driver.get(self.start_url)

	def back(self):
		self.driver.back()

	def click_text_link(self, args):
		self.jquery_highlight_inject()
		link = self.driver.find_element_by_link_text(args[0])
		link.click()
		time.sleep(1)
		
	def submit_text_field(self, args):
		self.jquery_highlight_inject1()
		field = self.driver.find_element_by_name(args[0])
		field.send_keys(args[1])
		field.send_keys(Keys.ENTER)
		time.sleep(1)
		
	def entry_text_field(self, args):
		self.jquery_highlight_inject1()
		field = self.driver.find_element_by_name(args[0])
		field.send_keys(args[1])

	def submit_form(self, args):
		field = self.driver.find_element_by_name(args[0])
		field.send_keys(Keys.ENTER)
		time.sleep(1)
		
	def click_button(self, args):
		field = self.driver.find_element_by_name(args[0])
		field.click()
		time.sleep(1)
		
	def click_check_box(self, args):
		check_box = self.driver.find_element_by_name(args[0])
		check_box.click()

	def get_element_by_text(self, search_term):
		return self.driver.find_elements_by_xpath("//*[contains(text(), %s)]" % search_term)

	def get_element_by_tab_index(self, index):
		pass

	def select_dropdown_option(self, args):
		dropdown = self.driver.find_element_by_name(args[0])
		dropdown.send_keys(args[1])
		
	def jquery_highlight_inject(self):
		self.driver.execute_script(" $('a').click(function(){ $(this).css('background','none'); $(this).css({'background-color': 'yellow', 'display':'block', 'box-shadow':'0 0 10px 10px #FFF700', 'z-index':'9999'}); }); ")

	def jquery_highlight_inject1(self):
		self.driver.execute_script(" $('input').focus(function(){ $(this).css('background','none'); $(this).css('background','none'); $(this).css({'background-color': 'yellow', 'display':'block', 'box-shadow':'0 0 10px 10px #FFF700', 'z-index':'9999'}); }); ")

	def refresh(self, args):
		self.driver.refresh()

	def click_button_by_value(self, args):
		self.jquery_highlight_inject()
		dd = self.driver.find_elements_by_xpath("//*[@value='Update']")
		dd.pop().click()

	# let's get some helper functions up in this biatch
	def moveslow(self, mouse, xdest, ydest):
	    #find the current position of the mouse
	    xorig, yorig = mouse.position()
	    xDir = 1 # 'right'
	    yDir = 1 # 'down'
	    done = False
	    if xorig > xdest:
	        # we're to the right and need to decriment
	        xDir = -1 # 'left'
	    if yorig > ydest:
	        # we're below and will need to decriment
	        yDir = -1 # 'up'
	    while not done:
	        # move y
	        if yorig != ydest:
	            yorig = yorig + yDir
	            mouse.move(xorig, yorig)
	        # move x
	        if xorig != xdest:
	            xorig = xorig + xDir
	            mouse.move(xorig, yorig)
	        time.sleep(.001)      
	        # test if done
	        if xorig == xdest and yorig == ydest:
	            done = True

		