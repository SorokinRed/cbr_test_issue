import time

from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as SeExceptions
from selenium.webdriver.common.by import By

from pageobject import pages

@given('open page {page}')
def open_page(context, page):
    context.browser.get(pages[page]['url'])

@given('click {elem_locator} on {page}')
def click(context, elem_locator, page):
    elem = context.wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, pages[page][elem_locator])
        )
    )
    elem.click()

@given('type {value} in {elem_locator} on {page}')
def type_text(context, value, elem_locator, page):
    elem = context.wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, pages[page][elem_locator])
        )
    )
    elem.send_keys(value)
    #webdriver печатает быстрее чем успевает рендерить
    time.sleep(0.5)

@given('press enter in {elem_locator} on {page}')
def press_enter(context, elem_locator, page):
    type_text(context, u'\ue007', elem_locator, page)

@given('switch to {page}')
def switch_to_page(context, page):
    for handler in context.browser.window_handles:
        context.browser.switch_to_window(handler)
        if context.browser.current_url == pages[page]['url']:
            break
    #raise Exception("Страница не найдена")

@given('scroll to {elem_locator} on {page}')
def scroll_to_element(context, elem_locator, page):
    webelement = context.browser.find_element_by_xpath(
        pages[page][elem_locator]
    )
    context.browser.execute_script("arguments[0].scrollIntoView();", webelement)
