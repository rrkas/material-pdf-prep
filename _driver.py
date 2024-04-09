import os
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains


def set_chrome_options(debug=False):
    chrome_options = Options()
    args = [
        "enable-automation",
        "start-maximized",
        "disable-infobars",
        "--disable-infobars",
        "--no-sandbox",
        "--force-device-scale-factor=1",
        "--disable-extensions",
        "--disable-dev-shm-usage",
        "--disable-gpu",
    ]

    if not debug:
        args.extend(
            [
                "--headless",
            ]
        )

    for e in args:
        chrome_options.add_argument(e)

    chrome_prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    return chrome_options


def get_driver(url, debug=False):
    os.makedirs("./bin/drivers/", exist_ok=True)
    chromedriver_exc_path = chromedriver_autoinstaller.install(path="./bin/drivers/")
    service = Service(executable_path=chromedriver_exc_path)
    driver = webdriver.Chrome(
        service=service,
        options=set_chrome_options(debug=debug),
    )
    driver.implicitly_wait(0.05)
    driver.set_page_load_timeout(60 * 60 * 60)
    driver.get(url)
    return driver
