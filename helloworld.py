from math import fabs
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    print('Hi')
    iNumber = 9
    #print('Number: ' + str(iNumber))
    return 'Hello, World! ' + str(iNumber) 

app.run(debug=True)


