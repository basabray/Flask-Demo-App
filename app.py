from flask import Flask
import numpy as np 

app = Flask(__name__) 

@app.route('/') 
def hello_world(): 
    return 'Hello, World!'

@app.route('/findSquraeRoot')
def testfun():
    v = 25
    return str(np.sqrt(v))




