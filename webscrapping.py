from selenium import webdriver

MAX_PAGE_NUM = 5
MAX_NUM_DIG = 3

with open('result.csv', 'w') as file:
    file.write('Buyers, Prices \n')

for i in range(1, MAX_PAGE_NUM + 1):
    page_num = (MAX_NUM_DIG - len(str(i))) * "0" + str(i)
    url = 'http://econpy.pythonanywhere.com/ex/' + page_num + '.html'

    driver = webdriver.Chrome()
    driver.get(url)
    buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
    prices = driver.find_elements_by_xpath('//span[@class="item-price"]')
    items = len(buyers)

    with open('result.csv', 'a') as file:
        for i in range(items):
            file.write(buyers[i].text + ',' + prices[i].text + '\n')

driver.close()
