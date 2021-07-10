from flask import Flask
from day10.mydao_emp import DaoEmp

app = Flask(__name__)
 
@app.route('/')
def hello_world():
    de = DaoEmp()
    cnt = de.insert()
    print(cnt)
    
    return 'Hello Flask!'
 
if __name__ == '__main__':
    app.run(debug=True)
