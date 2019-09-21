#import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_user_should_see_basket_button(browser):
    browser.get(link)
    #time.sleep(30)
    basket_button = browser.find_elements_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")
    assert len(basket_button) == 1, "No basket button"