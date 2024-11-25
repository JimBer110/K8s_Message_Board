from flask import Flask, request, render_template, url_for, redirect
import requests
import json
import os
import datetime

app = Flask(__name__)
BACKENDURL = os.environ['BACKEND_URL']
    

@app.route('/')
def index():
    url = BACKENDURL + "/list"
    req = requests.get(url)
    msg_list = json.loads(req.text)

    return render_template('index.html', msg_list=msg_list)

@app.route('/post_message', methods=['POST', 'GET'])
def post_message():
    if request.method == 'POST':
        username = request.form.get('usr', default='Anon')
        content = request.form.get('msg', default='')

        data = {
            "username":username,
            "message":content
            }
        
        url =  BACKENDURL + "/create"
        requests.post(url, data)
        
        return redirect(url_for('index')) #for now I route to this
                                          #since I am unsure what to do
    else:
        return render_template('post_message.html')

@app.route('/modify_message', methods=['POST', 'GET'])
def modify_message():
    if request.method == 'POST':
        msg_id = request.form.get('msg_id', type=int)
        content = request.form.get('msg', default='')

        data = {
            "message_id" : msg_id,
            "message" : content
        }

        url =  BACKENDURL + "/update"
        requests.post(url, data)

        return redirect(url_for('index'))
    else:
        return render_template('modify_message.html')
    
@app.route('/delete_message', methods=['POST', 'GET'])
def delete_message():
    if request.method == 'POST':
        msg_id = request.form.get('msg_id')

        data = {
            "message_id" : msg_id
        }

        url =  BACKENDURL + "/delete"
        requests.post(url, data)

        return redirect(url_for('index'))
    else:
        return render_template('delete_message.html')   


if __name__ == '__main__':
    app.run(debug=True)

    

