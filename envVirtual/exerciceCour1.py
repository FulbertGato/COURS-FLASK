from flask import Flask
app= Flask(__name__)

@app.route('/')
def index():
    return "<h1> 1-) <a href='/page/gatoJunior' > Route dynamique </a> <h1> <br><h1> 2-) <a href='/nom/junior' > Nom en latin </a> <h1>"


@app.route('/page/<pageName>')
def name(pageName):
    return f"<h1> Hello c'est la page : {pageName} !  <h1>"

@app.route('/nom/<latinName>')
def latinName(latinName):
    nameList=list(latinName)
    if(nameList[-1] == "y"):
        nameList[-1]= "iful"
    else:
        nameList.append("y")
    latinNameConvert = "".join(nameList)
    return f"<h1> Votre nom  {latinName}  en latin  : {latinNameConvert} !  <h1>"

    
if __name__ == '__main__' :
    app.run(debug=True)
