# -*- coding: utf-8 -*-
# @Author: cjzz
# @Date:   2018-04-14 15:12:13
# @Last Modified by:   cjzz
# @Last Modified time: 2018-04-14 17:54:59
import requests
from bs4 import BeautifulSoup

def detail_page(url):
	req = requests.get(url)
	html = req.text
	soup = BeautifulSoup(html,'lxml')
	detail_job_name = soup.select('.new_job_name')[0].string
	detail_company_name = soup.select('.com-name')[0].string
	detail_money = soup.select('.job_money')[0].string.encode('utf-8')
	detail_money = detail_money.replace(b'\xee\xa4\x85',b'1')
	detail_money = detail_money.replace(b'\xee\xa9\x93',b'3')
	detail_money = detail_money.replace(b'\xee\xb1\x9d',b'0')
	detail_money = detail_money.decode()

	print(detail_job_name,detail_company_name,detail_money)
	
for page in range(1,3):
	req = requests.get('https://www.shixiseng.com/interns/c-310100_st-intern_?k=%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98&p={}'.format(page))
	html = req.text

	soup = BeautifulSoup(html,'lxml')
	for item in soup.select('a.name'):
		detail_url = item.get('href')
		
		detail_page('https://www.shixiseng.com'+detail_url)




