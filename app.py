from flask import Flask, render_template, 
request
from markupsafe import escape
import matplotlib.pyplot as plt
app = Flask(__name__)
@app.route('/num_start')
def num_start():
    return render_template('plot.html');
@app.route('/numbers',methods=['POST'])
def numbers():
    data = request.form['numbers']
    print(type(data))
    print(data)
    ypoints = data.split(',')
    plt.clf()
    plt.plot(ypoints, marker = 'o')
    fname = './static/linechart.jpg'
    plt.savefig(fname)
    return fname
