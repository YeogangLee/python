from flask import Flask
from flask import request

app = Flask(__name__)
App = Flask(__name__)
 
@app.route('/hello')
def hello_world():
    
    drink = request.args.get('drink')
    txt = drink + ' 마셔 get'
    return txt

@App.route("/post",methods=['POST'])
def post():
    drink2 = request.form['drink']
    txt2 = drink2 + ' 마셔 post'
    return txt2
 
if __name__ == '__main__':
    App.run(debug=True)
    app.run(debug=True)
