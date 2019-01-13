from pageobject import pages

@Then('to me present {element} on {page}')
def check_element(context, page, element):
    context.browser.find_element_by_xpath(
        pages[page][element]
    )