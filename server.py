from flask import Flask, jsonify, request 
import requests
  
app = Flask(__name__) 

methods = {"am": requests.get, "ar": requests.post, "az": requests.put, "eu": requests.delete, "bg": requests.patch}
body_methods = (requests.post, requests.put, requests.patch)

@app.route('/translate', methods=['GET']) 
def helloworld(): 
    if request.method == 'GET' and request.args["text"].startswith("scratch-http|"): 
        full_txt = request.args["text"].split("|")
        txt = full_txt[1]
        body = full_txt[2]
        method = methods[request.args["language"]]
        if method in body_methods: 
            data = {"result": str(method(txt, body).text)}
        else: 
            data = {"result": str(method(txt).text)}
        print(data)
        res = jsonify(data)
        res.headers.add('Access-Control-Allow-Origin', '*')
        return res
  
  
if __name__ == '__main__': 
    app.run(host='127.0.0.1', port=443, ssl_context=("server.crt", "server.key")) 
