from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>CTF Backend Challenge</h1>
        <p>Send a POST request to /getflag with key=opensesame</p>
    '''

@app.route('/getflag', methods=['POST'])
def get_flag():
    if request.form.get('key') == 'opensesame':
        return jsonify(flag='FLAG{post_request_success}')
    return jsonify(error='Invalid key')

@app.route('/challenge1')
def challenge1():
    return render_template('challenge1_source.html')

@app.route('/challenge2')
def challenge2():
    return render_template('challenge2_cookie.html')

@app.route('/challenge3')
def challenge3():
    return render_template('challenge3_script.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
