Feature: тестовое задание

   Scenario: сценарий
        Given open page google_search_page
        Then to me present input_search on google_search_page
        Given type Цетральный банк РФ in input_search on google_search_page
        And press enter in input_search on google_search_page
        Then to me present cbr_link on search_result_page
        Given click cbr_link on search_result_page
        And switch to cbr_page
        Then to me present cbr_logo on cbr_page
        Given click reseption on cbr_page
        And click gratitude on cbr_page
        And type Текст благодарности in message_body on cbr_page
        And scroll to agree_checkbox on cbr_page
        And click agree_checkbox on cbr_page
        #Сделает скриншот текущей страницы
        #Отправит этот скриншот на указанный e-mail