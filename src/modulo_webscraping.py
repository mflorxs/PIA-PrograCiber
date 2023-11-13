import requests
from bs4 import BeautifulSoup
import logging

def web_scraping(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True)]

        return links

    except requests.RequestException as e:
        logging.error(f"Error al realizar la solicitud HTTP: {e}")
        raise
    except Exception as e:
        logging.error(f"Error en web scraping: {e}")
        raise
