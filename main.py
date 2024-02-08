from flask import Flask, request, jsonify, render_template
from test_gpt import getMedicineSpecialize
import aiohttp

app = Flask(__name__)

@app.route('/api/search', methods=['POST'])
async def search():
    try:
        data = request.get_json()

        if 'search_query' not in data:
            return jsonify({'error': 'Missing search_query parameter'}), 400

        search_query = data['search_query']

        search_result = await getMedicineSpecialize(search_query)
        print(search_result)

        return jsonify({'search_result': search_result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/', methods=['GET', 'POST'])
async def index():
    search_result = None

    if request.method == 'POST':
        search_query = request.form['search_query']
        search_result = await getMedicineSpecialize(search_query)

    return render_template('index.html', search_result=search_result)


if __name__ == '__main__':
    app.run(debug=True)
