from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

# Function to scrape data from a website
def scrape_data():
    url = 'https://google.com'  # Replace with the URL you want to scrape
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the title of the page
    title = soup.title.string
    
    # Extract all the links on the page
    links = [a['href'] for a in soup.find_all('a', href=True)]
    
    return title, links

@app.route('/')
def index():
    # Scrape data
    title, links = scrape_data()
    
    return render_template('index.html', title=title, links=links)

if __name__ == '__main__':
    app.run(debug=True)
