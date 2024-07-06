from flask import Flask, render_template
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    api_url = os.getenv('API_URL')
    id_instance = os.getenv('ID_INSTANCE')
    api_token_instance = os.getenv('API_TOKEN_INSTANCE')
    return render_template('main.html', api_url=api_url, id_instance=id_instance, api_token_instance=api_token_instance)

if __name__ == '__main__':
    app.run(debug=True)
