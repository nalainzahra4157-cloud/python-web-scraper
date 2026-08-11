import requests
from bs4 import BeautifulSoup
import pandas as pd

def clean_text(text):
    if text:
        text = text.replace('“', '"').replace('”', '"')
        text = text.replace('’', "'").replace('‘', "'")
        text = text.replace('â€œ', '"').replace('â€', '"')
    return text.strip()

def scrape_quotes():
    url = "http://quotes.toscrape.com/"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes_list = []
        
        quotes = soup.find_all('div', class_='quote')
        
        for q in quotes:
            raw_text = q.find('span', class_='text').text
            raw_author = q.find('small', class_='author').text
            clean_quote = clean_text(raw_text)
            clean_author = clean_text(raw_author)
            
            quotes_list.append({
                'Quote': clean_quote,
                'Author': clean_author
            })
            
        df = pd.DataFrame(quotes_list)
        df.to_csv('quotes_output.csv', index=False, encoding='utf-8-sig')
        print("Scraping Complete! Clean data saved to 'quotes_output.csv'")
    else:
        print("Failed to retrieve website page.")

scrape_quotes()
