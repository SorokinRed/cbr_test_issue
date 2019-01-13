import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

from behave import fixture, use_fixture

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait

import config

@fixture
def selenium_browser_chrome(context):
    chrome_options = webdriver.ChromeOptions()
    if config.headless:
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--ignore-certificate-errors')

    context.browser = webdriver.Chrome(
        executable_path=config.path_to_driver,
        chrome_options=chrome_options
    )
    context.browser.set_window_size(config.width, config.height)
    context.main_tab = context.browser.current_window_handle
    context.browser.implicitly_wait(3)
    context.browser.set_page_load_timeout(config.page_load_timeout)
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()

@fixture
def send_mail(send_from, send_to, passwd, subject, text, files=None,
              server="127.0.0.1"):
    assert isinstance(send_to, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)


    smtp = smtplib.SMTP_SSL('smtp.yandex.ru:465')
    #smtp = smtplib.SMTP(server)
    smtp.login(config.from_email, config.email_passwd)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()

@fixture
def take_screenshot(context):
    context.browser.save_screenshot('screen.png')

@fixture
def webdriver_wait(context):
    context.wait = WebDriverWait(context.browser, 5)
    yield context.wait

def before_feature(context, feature):
    use_fixture(selenium_browser_chrome, context)
    use_fixture(webdriver_wait, context)

def after_feature(context, feature):
    use_fixture(take_screenshot, context)
    use_fixture(
        send_mail(
            config.from_email,
            [config.to_email],
            config.email_passwd,
            "Скриншот после теста",
            "В приложении содержится скриншот при завершении работы",
            ['screen.png'],
            server = config.smtp_server
        ),
        context
    )