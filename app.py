import json
from serpapi import GoogleSearch
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def search_results():
    # Set the search query parameters
    params = {
      "engine": "google",
      "q": "bahis siteleri ",
      "location": "Ankara, Ankara, Turkey",
      "google_domain": "google.com.tr",
      "gl": "tr",
      "hl": "tr",
      "device": "mobile"
    }

    # Make the API request and get the JSON response
    search = GoogleSearch(params)
    results = search.get_dict()

    # Extract the search results and create the HTML table
    table_rows = ''
    for result in results['organic_results']:
        position = result['position']
        title = result['title']
        link = result['link']
        displayed_link = result['displayed_link']
        row = f'<tr><td>{position}</td><td>{title}</td><td><a href="{link}">{displayed_link}</a></td></tr>'
        table_rows += row

    # Render the HTML template with the search results
    return render_template('search_results.html', table_rows=table_rows)

if __name__ == '__main__':
    app.run(debug=True)
