from scraper_selenium import get_html
from parser_html import get_elements
from scraper_req_html import get_rendered_html

url = "https://www.coingecko.com"


def save_html(html: str) -> None:
    with open('page.html', 'w', encoding='utf-8') as file:
        file.write(html)


if __name__ == '__main__':
    html = get_rendered_html(url)
    save_html(html)
    print(get_elements(html))