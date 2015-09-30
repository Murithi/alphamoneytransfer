from selenium import webdriver
browser = webdriver.Firefox()
# Regina has about our online money transfer service. She goes
# to check out it's home page

browser.get('http://localhost:8000')

# She notices the page title and header mention pata-pesa
assert 'pata-pesa money transfer' in browser.title

# She is invited to sign up straight away

# She types