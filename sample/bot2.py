from selenium import webdriver
from selenium.webdriver.support.ui import Select
from config2 import keys
import time


def order(k):
    start = time.time()

    driver.get(k['product_url'])

    driver.find_element_by_class_name('wp-block-button__link').click()

    Select(driver.find_element_by_id('pa_size')).select_by_visible_text('5')

    time.sleep(.5)

    addcart = driver.find_element_by_class_name('single_add_to_cart_button')
    addcart.click()

    time.sleep(.4)

    driver.find_element_by_xpath('//*[@id="main"]/div[1]/div/a[1]').click()
    
    driver.find_element_by_xpath('//*[@id="billing_first_name"]').send_keys(k['f_name'])

    driver.find_element_by_xpath('//*[@id="billing_last_name"]').send_keys(k['l_name'])

    driver.find_element_by_xpath('//*[@id="billing_address_1"]').send_keys(k['address'])

    driver.find_element_by_xpath('//*[@id="billing_city"]').send_keys(k['city'])

    Select(driver.find_element_by_id('billing_state')).select_by_visible_text(k['state'])

    time.sleep(.5)

    driver.find_element_by_xpath('//*[@id="billing_postcode"]').send_keys(k['zipcode'])

    driver.find_element_by_xpath('//*[@id="billing_phone"]').send_keys(k['phone'])

    driver.find_element_by_xpath('//*[@id="billing_email"]').send_keys(k['email'])

    time.sleep(1.5)

    driver.find_element_by_xpath('//*[@id="place_order"]').click()

    #debit card payment

    #time.sleep(4)
    #driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/ul/li[3]/a').click()
    #time.sleep(1.5)
    #driver.find_element_by_xpath('//*[@id="card-number"]').send_keys(k['carde'])
    #driver.find_element_by_id('card-expiry-month').send_keys(k['monthe'])
    #driver.find_element_by_id('card-expiry-year').send_keys(k['yeare'])
    #driver.find_element_by_id('card-cvv').send_keys(k['cvv'])

    #For gpay payment

    #time.sleep(4)
    #payment = driver.find_element_by_class_name('btn')
    #payment.click()
    #gpay = driver.find_element_by_class_name('grid__item--unit')
    #gpay.click()
    #upi_id = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/form/div/div/ul/div/div/ul/li/div[2]/div[2]/input')
    #upi_id.send_keys("r1habcarbon")
    #verify = driver.find_element_by_class_name('btn-block')
    #verify.click()

    end = time.time()

    print(f"time to execute is{end - start}")


if __name__ == "__main__":
    driver = webdriver.Chrome()
    #driver.maximize_window()
    order(keys)
    