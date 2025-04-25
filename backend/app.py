from flask import Flask, request, jsonify

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
