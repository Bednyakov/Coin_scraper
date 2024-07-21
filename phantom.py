import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options


def get_html(url: str) -> str:
    """
    Возвращает HTML.
    """
    chrome_options = Options()
    chrome_options.add_argument(f"--load-extension={'/home/artem/Coin_scraper/proxi_extension'}") #  подключаем расширение с прокси
    #chrome_options.add_argument('--headless')  # Запускаем в режиме без графического интерфейса
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_page_load_timeout(5)

    try:
        driver.get(url)
    except Exception as e:
        print(e)

    finally:

        # Получаем HTML-код страницы
        html = driver.page_source
        driver.quit()

        return html


def get_elements(html: str) -> None:

    soup = BeautifulSoup(html, 'html.parser')

    # Находим элемент <tbody>
    tbody = soup.find('tbody')

    # Извлекаем все элементы <tr> внутри <tbody>
    rows = tbody.find_all('tr')

    # Проходимся по каждой строке и извлекаем текст и ссылки
    for row in rows:
        # Извлекаем текст из всех ячеек <td>
        cells = row.find_all('td')
        cell_texts = [cell.get_text(strip=True) for cell in cells if cell.get_text(strip=True) != '']

        # Извлекаем ссылки из всех ячеек <td>
        cell_links = [cell.find('a')['href'] if cell.find('a') else None for cell in cells]
        cell_links = {link for link in cell_links if link is not None}

        # Выводим результаты
        print(f"Текст: {cell_texts}")
        print(f"Ссылки: {cell_links}")
        print("-" * 30)


def save_html(html: str) -> None:
    with open('page.html', 'w', encoding='utf-8') as file:
        file.write(html)


if __name__ == '__main__':
    url_to_scrape = 'https://www.coingecko.com/'
    html = get_html(url_to_scrape)
    save_html(html)
    get_elements(html)
