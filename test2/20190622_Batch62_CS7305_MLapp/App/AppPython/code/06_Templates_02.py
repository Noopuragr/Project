from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<int:score>')
def hello_name(score):
   return render_template('hello_02.html', marks = score)

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=1234, debug = True)