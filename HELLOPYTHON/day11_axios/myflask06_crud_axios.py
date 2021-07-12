from flask import Flask, render_template, request, jsonify
from day11_axios.mydao_emp_axios import DaoEmp

app = Flask(__name__, static_url_path="", static_folder="static")
 
@app.route('/emp_axios')
def emp():
    de = DaoEmp()
    list = de.selectlist()
    return render_template('emp_axios.html', list=list)


@app.route('/emp_insert.ajax', methods=['POST'])
def ajax():
    d = request.get_json()
    de = DaoEmp()
    cnt = de.insert(d['e_id'], d['e_name'], d['tel'], d['address'])
    msg = "fail"
    if cnt == 1 :
        msg = "success" 
    
    print(d['e_id'])
    return jsonify(result=msg)


if __name__ == '__main__':
    app.run(debug=True)
