from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def hello_world():
    return render_template('index.html')

@app.route('/team1.html')
def team1():
    return render_template('team1.html')

@app.route('/team2.html')
def team2():
    return render_template('team2.html')

@app.route('/team3.html')
def team3():
    return render_template('team3.html')

@app.route('/team4.html')
def team4():
    return render_template('team4.html')

@app.route('/team5.html')
def team5():
    return render_template('team5.html')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
  
