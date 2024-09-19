import time
from selenium.webdriver.common.by import By

link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_presence_btn_add_to_basket(browser):
    print("start test")
    browser.get(link)
    time.sleep(5)
    assert browser.find_elements(By.CLASS_NAME, 'btn-add-to-basket'), 'basket button not found'
    print('finish test')