from bs4 import BeautifulSoup
import json



def get_elements(html: str) -> None:

    data = {}

    soup = BeautifulSoup(html, 'html.parser')

    tbody = soup.find('tbody')

    rows = tbody.find_all('tr')

    # Проходимся по каждой строке
    for row in rows:
        # Извлекаем текст из всех ячеек <td>
        cells = row.find_all('td')
        cell_texts = [cell.get_text(strip=True) for cell in cells if cell.get_text(strip=True) not in ('', 'Buy')]

        # Извлекаем ссылки из всех ячеек <td>
        cell_links = [cell.find('a')['href'] if cell.find('a') else None for cell in cells]
        cell_link = 'https://www.coingecko.com' + [link for link in cell_links if link is not None][0]
        name = [link for link in cell_links if link is not None][0].split('/')[-1]

        coin_info = {
                    "Price": cell_texts[2],
                    "1h": cell_texts[3],
                    "24h": cell_texts[4],
                    "7d": cell_texts[5],
                    "30d": cell_texts[6],
                    "24h Volume": cell_texts[7],
                    "Market Cap": cell_texts[8],
                    "Fully Diluted Valuation": cell_texts[9],
                    "link": cell_link,
                    }
        
        data[name] = coin_info

    result = json.dumps(data)
    return result