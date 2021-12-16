from flask import Flask, render_template
app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    return render_template('index.html', message="花子さん")

@app.route('/hello/<name>')
def hello(name):
    return name

# if __name__ == "__main__":
app.run(port=8000, debug=True)