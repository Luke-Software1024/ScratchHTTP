from flask import Flask, request 
import requests
  
app = Flask(__name__) 

@app.route('/synth', methods=['GET']) 
def server(): 
    txt = request.args["text"]

    res = app.make_response(requests.get(txt).content)
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res
  
if __name__ == '__main__': 
    app.run(host='127.0.0.1', port=443, ssl_context=("sound-server.crt", "sound-server.key"))
