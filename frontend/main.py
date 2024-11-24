from flask import Flask, request, render_template, url_for, redirect

from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post_message', methods=['POST', 'GET'])
def post_message():
    if request.method == 'POST':
        username = request.form['usr']
        message = request.form['msg']

        if username == '':
            username = 'Anon'
        
        
        return redirect(url_for('index'))
    else:
        return render_template('post_message.html')

@app.route('/modify_message', methods=['POST', 'GET'])
def modify_message():
    if request.method == 'POST':
        msg_id = request.form['msg_id']
        msg = request.form['msg']

        return redirect(url_for('index'))
    else:
        return render_template('modify_message.html')
    
@app.route('/delete_message', methods=['POST', 'GET'])
def delete_message():
    if request.method == 'POST':
        msg_id = request.form['msg_id']

        return redirect(url_for('index'))
    else:
        return render_template('delete_message.html')



if __name__ == '__main__':
    app.run(debug=True)

    

