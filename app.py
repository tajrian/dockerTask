from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hi Tajrian!"

if __name__ == "__main__":
    app.run(debug=True)