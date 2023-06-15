import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form['url']
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a')
    scraped_links = [link.get('href') for link in links]
    return render_template('results.html', links=scraped_links)

if __name__ == '__main__':
    app.run(debug=True)
