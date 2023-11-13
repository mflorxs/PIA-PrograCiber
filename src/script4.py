import argparse
import logging
from modulo_webscraping import web_scraping

def guardar_reporte(links, filename="reporte_webscraping.txt"):
    with open(filename, "w") as file:
        for link in links:
            file.write(f"{link}\n")

def main():
    logging.basicConfig(filename='cybersecsuite.log', level=logging.INFO)
    parser = argparse.ArgumentParser(description="CyberSecSuite - Herramienta de Web Scraping")
    parser.add_argument("--url", help="URL para realizar el web scraping", required=True)
    args = parser.parse_args()

    try:
        links = web_scraping(args.url)
        guardar_reporte(links)
        print(f"Enlaces extraídos guardados en reporte_webscraping.txt")
    except Exception as e:
        logging.error(f"Error en la ejecución principal: {e}")

if __name__ == "__main__":
    main()
