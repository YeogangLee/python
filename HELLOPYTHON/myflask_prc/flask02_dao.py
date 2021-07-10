from flask import Flask
from day10.mydao_emp import DaoEmp

app = Flask(__name__)

@app.route('/')
def weekend():
    de = DaoEmp()
    msg = de.letsgo()
    print('letsgo')
    
    return msg

if __name__ == '__main__':
    app.run(debug=True)