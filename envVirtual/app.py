from flask import Flask
app= Flask(__name__)

@app.route('/')
def index():
    return "<h1> Hello Dev !  <h1>"

@app.route('/home')
def home():
    return "<h1> Hello depuis Home<h1>"
    
if __name__ == '__main__' :
    app.run(debug=True)
