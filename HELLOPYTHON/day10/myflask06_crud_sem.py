from flask import Flask, render_template
from day10.mydao_emp import DaoEmp

app = Flask(__name__)
 
@app.route('/emp_sem')
def emp():
    de = DaoEmp()
    list = de.selectlist()
    return render_template('emp_sem.html', list=list)

if __name__ == '__main__':
    app.run(debug=True)
