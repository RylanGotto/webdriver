import pydriver as dd
import time

pd = dd.WebDriver('10.0.112.4/HiPM')

funcs = {
			'click_text_link':pd.click_text_link,
			'click_check_box':pd.click_check_box,
			'click_button':pd.click_button,
			'click_button_by_value':pd.click_button_by_value,
			'create_browser':pd.create_browser,
			'entry_text_field':pd.entry_text_field,
			'select_dropdown_option':pd.select_dropdown_option,
			'submit_text_field':pd.submit_text_field,
			'submit_form':pd.submit_form,
			'wait':time.sleep,
			'back':pd.back,
			'refresh':pd.refresh,
			
		}