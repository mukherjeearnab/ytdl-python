from flask import Flask, request, current_app, redirect, send_file, jsonify
import downloader as ytdl
app = Flask(__name__)

@app.route('/mp3')
def index():
    url = request.args.get('url')
    return jsonify(ytdl.download(url))

if __name__ == '__main__':
    app.run()



