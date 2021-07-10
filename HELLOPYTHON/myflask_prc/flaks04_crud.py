from flask import Flask, render_template
from myflask_prc.mydao_prc import MydaoPrc

app = Flask(__name__)

@app.route('/')
def prc():
    de = MydaoPrc()
    max = de.selec_stock_max()
    max = str(max)[2:7]
    min = de.selec_stock_min()
    min = str(min)[2:7]
    print(max)
    print(min)
    div = int(max)/int(min)
    return render_template('stock.html', result=div)

if __name__ == '__main__':
    app.run(debug=True)
    
    