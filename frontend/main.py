from flask import Flask, request, render_template, url_for, redirect
from message import Message

app = Flask(__name__)
    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post_message', methods=['POST', 'GET'])
def post_message():
    if request.method == 'POST':
        username = request.form.get('usr', default='Anon')
        content = request.form.get('msg', default='')

        msg : Message = Message(0, usrname=username, msg=content)

        print(msg.to_json())
        
        return redirect(url_for('index')) #for now I route to this
                                          #since I am unsure what to do
    else:
        return render_template('post_message.html')

@app.route('/modify_message', methods=['POST', 'GET'])
def modify_message():
    if request.method == 'POST':
        msg_id = request.form.get('msg_id')
        msg = request.form.get('msg', default='')

        return redirect(url_for('index'))
    else:
        return render_template('modify_message.html')
    
@app.route('/delete_message', methods=['POST', 'GET'])
def delete_message():
    if request.method == 'POST':
        msg_id = request.form.get('msg_id')

        return redirect(url_for('index'))
    else:
        return render_template('delete_message.html')   


if __name__ == '__main__':
    app.run(debug=True)

    

