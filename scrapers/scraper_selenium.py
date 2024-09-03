from selenium import webdriver
from loggers import logger
from selenium.webdriver.chrome.options import Options


def get_html(url: str) -> str:
    """
    Возвращает HTML.
    """

    chrome_options = Options()
    chrome_options.add_argument(f"--load-extension={'/home/artem/Coin_scraper/proxi_extension'}") #  подключаем расширение с прокси
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_page_load_timeout(5)

    try:
        driver.get(url)
    except Exception as e:
        logger.error(e)

    finally:

        # Получаем HTML-код страницы
        html = driver.page_source
        driver.quit()

        return html


