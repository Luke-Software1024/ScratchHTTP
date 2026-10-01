from flask import Flask, jsonify, request 
import requests
from io import BytesIO
from PIL import Image, ImageOps

app = Flask(__name__) 

methods = {"am": requests.get, "ar": requests.post, "az": requests.put, "eu": requests.delete, "bg": requests.patch, "zu": lambda url: requests.Response()}
body_methods = (requests.post, requests.put, requests.patch)

color_to_b64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
def process_image(_image: bytes):
    image = Image.open(BytesIO(_image))
    image = image.convert("RGB")

    image = ImageOps.contain(image, (256, 256))

    palette = Image.open("palette.png")
    image = image.quantize(palette=palette)

    string = ""
    for j in range(image.height):
        for i in range(image.width):
            pixel = image.getpixel((i, j))
            char = color_to_b64[pixel]
            string += char
        string += " "

    return string

@app.route('/translate', methods=['GET']) 
def server(): 
    full_txt = request.args["text"].split("|")
    txt = full_txt[0]
    body = full_txt[1]

    method = methods[request.args["language"]]
    if method in body_methods: 
        result = method(txt, body)
        data = {"result": "|".join((str(result.status_code), result.text))}
    else: 
        result = method(txt)

        if request.args["language"] == "zu":
            result.headers["content-type"] = "application/octet-stream"

        if result.headers["content-type"].startswith("image/"):
            text = process_image(result.content)
        else:
            text = result.text
        data = {"result": "|".join((str(result.status_code), text))}
    
    print(data)
    res = jsonify(data)
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res
  
if __name__ == '__main__': 
    app.run(host='127.0.0.1', port=443, ssl_context=("text-server.crt", "text-server.key"))
