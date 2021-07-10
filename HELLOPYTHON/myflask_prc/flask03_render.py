from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
@app.route('/member')
def member():

    date = str(datetime.datetime.now())[:19]
    arr = ['오렌지', '레몬', '블루레몬']
    arr_json = [
            {'favorite':'오렌지', 'color':'orange'}
            ,{'sour':'레몬', 'color':'yellow'}
            ,{'great':'블루레몬', 'color':'blue_yellow'}
        ]

    return render_template('colors.html', date=date, arr=arr, arr2=arr_json)

if __name__ == '__main__':
    app.run(debug=True)