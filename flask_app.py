from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "<p>Dit is de huiswerkopgave van les 11</p>"

if __name__ == '__main__':
    app.run(port=5000,debug=True)