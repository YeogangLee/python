from flask import Flask, render_template
 
app = Flask(__name__)

@app.route('/')
@app.route('/member')
def index():
    arr = ['김소희', '이여강', '오수연', '최윤지', '김지수']
    arr2 = [
        {'name':'김소희', 'tel':'010-2222-3333'},
        {'name':'이여강', 'tel':'010-3333-4444'}
      ]
  
    # arr2=arr2 -> 자바의 setAttribute("arr2", arr2)
    return render_template('index.html', dan=2, arr=arr, arr2=arr2)


if __name__ == '__main__':
    app.run(debug=True)