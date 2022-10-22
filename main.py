from flask import Flask, request
#initialize flask
app = Flask(__name__)

data = {'present students' : ['tanveer', 'ajay', 'deepak', 'saurav', 'mani']}

@app.route('/', methods = ['GET'])
def home():
    return('welcome to learning deployement')

@app.route('/get_names',methods = ['GET'])
def get_names():
    return data

@app.route('/post_names', methods = ['POST'])
def post_names():
    updated_data = request.json['new_data']
    data['present students'].append(updated_data)
    return {'status': 'success'}

@app.route('/put_names', methods = ['PUT'])
def put_names():
    updated_data1 = request.json['new_data']
    print(updated_data1)
    return {'status': 'success'}

#run the app
app.run(debug = True)
