from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/', methods = ['GET'] )
def home():
    return redirect('https://donnabellebooks.wordpress.com/')

if __name__ == '__main__':
    app.run(port=7000, debug=True)