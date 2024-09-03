from requests_html import HTMLSession

def get_rendered_html(url):
    session = HTMLSession()
    
    response = session.get(url)
    
    response.html.render(timeout=60)  # Тайм-аут в секундах на случай долгого выполнения
    
    return response.html.html
