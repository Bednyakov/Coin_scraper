import requests
from bs4 import BeautifulSoup
from config import headers

def scrape_table_data(url):
    # Отправляем GET-запрос на указанный URL
    response = requests.get(url, headers=headers)
    save_html(response)
    print(response.status_code)
    print(response.text)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Находим элемент <tbody>
    tbody = soup.find('tbody')

    # Извлекаем все элементы <tr> внутри <tbody>
    rows = tbody.find_all('tr')

    # Проходимся по каждой строке и извлекаем текст и ссылки
    for row in rows:
        # Извлекаем текст из всех ячеек <td>
        cells = row.find_all('td')
        cell_texts = [cell.get_text(strip=True) for cell in cells]

        # Извлекаем ссылки из всех ячеек <td>
        cell_links = [cell.find('a')['href'] if cell.find('a') else None for cell in cells]

        # Выводим результаты
        print(f"Текст: {cell_texts}")
        print(f"Ссылки: {cell_links}")
        print("-" * 30)

def save_html(response) -> None:
    with open('page.html', 'w', encoding='utf-8') as file:
        file.write(response.text)

# Пример использования
url_to_scrape = 'https://www.coingecko.com/'  # Замените на нужный вам URL
scrape_table_data(url_to_scrape)
