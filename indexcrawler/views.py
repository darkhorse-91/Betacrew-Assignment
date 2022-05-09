from django.shortcuts import render
from django.http import HttpResponse

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

from .models import NiftyFifty


def scrape(url, xpath_string):
	options = Options()
	# options.headless = True
	options.add_argument("--headless")
	driver = webdriver.Firefox(options = options, executable_path="/opt/homebrew/Cellar/geckodriver/0.31.0/bin/geckodriver")

	driver.get(url)

	data_elem = driver.find_elements(By.XPATH, xpath_string)
	data_elem = data_elem[0].get_attribute("innerText")

	print(data_elem)
	driver.close()
	return data_elem


def show_index(request):

	create_index_data()
	model_index_data = NiftyFifty.objects.all()
	print([(i.id,i.index_name, i.index_value, i.timestamp) for i in model_index_data])
	return HttpResponse("Nifty Fifty - ", model_index_data)


def str_to_int(s):
	new_s = ""
	for i in s:
		if i != ",":
			new_s += i
	return float(new_s)


def create_index_data():
	# foo_instance = Foo.objects.create(name='test')
	url = "https://www.nseindia.com/"
	xpath_string = "/html/body/div[9]/div[1]/section[1]/div/div/div/div/div[1]/div[2]/div/div/nav/div/div/a[1]/div/p[2]"

	index_data = scrape(url, xpath_string)

	niftyfifty_instance = NiftyFifty.objects.create(index_name = "Nifty 50", index_value = str_to_int(index_data), percent_change = 0)

	
	