pages = {
    "google_search_page": {
        "url": "https://www.google.ru/",
        "input_search": "//input[@title='Поиск']",
    },
    "search_result_page":{
        "cbr_link": "//a[contains(@href, 'www.cbr.ru')]"
    },
    "cbr_page":{
        "url": "https://www.cbr.ru/",
        "cbr_logo": "//span[@class='ico-logo']",
        "reseption": "//a[contains(text(), 'Интернет-приемная')]",
        "gratitude": "//*[contains(text(), 'Написать благодарность')]",
        "message_body": "//textarea[@id='MessageBody']",
        "agree_checkbox": "//input[@id='_agreementFlag']"
    }
}