from flask import Flask, request

app = Flask(__name__)

@app.route('/uploads', methods=['POST'])
def upload_file():
    if 'file' in request.files:
        f = request.files['file']
        f.save(f"./uploads/{f.filename}")
        return "File received succesfully", 200
    return "There is no file", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
