from flask import Flask, request, redirect
import string
import random

app = Flask(__name__)
url_mapping = {}

def generate_short_url():
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(6))

@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.form['url']
    short_url = generate_short_url()
    url_mapping[short_url] = long_url
    return short_url

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    if short_url in url_mapping:
        long_url = url_mapping[short_url]
        return redirect(long_url)
    else:
        return "Invalid short URL"

if __name__ == '__main__':
    app.run()
