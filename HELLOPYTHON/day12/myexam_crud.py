from flask import Flask, render_template, request, jsonify
from day12.mydao_exam import DaoExam

app = Flask(__name__, static_url_path="", static_folder="static")
 
@app.route('/exam')
def exam():
    dex = DaoExam()
    list = dex.selectlist()
    return render_template('exam.html', score_list=list)

@app.route('/exam_insert.axios', methods=['POST'])
def exam_insert():
    d = request.get_json()
    dex = DaoExam()
    cnt = dex.insert(d['exam_id'], d['e_id'], d['e_name'], d['tel'], d['address'])
    msg = "fail"
    if cnt == 1 :
        msg = "success" 
    
    print(d['exam_id'])
    return jsonify(result=msg)


@app.route('/exam_update.axios', methods=['POST'])
def exam_update():
    d = request.get_json()
    print(d)
    dex = DaoExam()
    cnt = dex.update(d['exam_id'], d['e_id'], d['e_name'], d['tel'], d['address'])
    msg = "fail"
    if cnt == 1 :
        msg = "success" 
    
    print(d['exam_id'])
    return jsonify(result=msg)


@app.route('/exam_delete.axios', methods=['POST'])
def exam_delete():
    d = request.get_json()
    print(d)
    dex = DaoExam()
    cnt = dex.delete(d['exam_id'])
    msg = "fail"
    if cnt == 1 :
        msg = "success" 
    
    print(d['exam_id'])
    return jsonify(result=msg)

if __name__ == '__main__':
    app.run(debug=True)
    
    
    