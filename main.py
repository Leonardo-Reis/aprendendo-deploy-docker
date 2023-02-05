from flask import Flask
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Hello, Docker!'

def run():
    port = int(os.environ.get("PORT", 5000))
    #serve(app, host='0.0.0.0', port=port)

    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    run()