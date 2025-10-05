from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

MEDIA_FOLDER = 'media'
os.makedirs(MEDIA_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = MEDIA_FOLDER

messages = []

@app.route("/api/messages", methods=["GET"])
def get_messages():
    """Tüm mesajları JSON olarak döndürür."""
    return jsonify(messages)

@app.route("/api/messages", methods=["POST"])
def post_message():
    """Yeni mesaj ekler (metin, resim, ses)."""
    text = request.form.get("text", "")
    image = None
    audio = None

    # Görsel yükleme
    if "image" in request.files:
        img = request.files["image"]
        if img.filename:
            filename = secure_filename(img.filename)
            img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            image = filename

    # Ses dosyası yükleme
    if "audio" in request.files:
        aud = request.files["audio"]
        if aud.filename:
            filename = secure_filename(aud.filename)
            aud.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            audio = filename

    # Yeni mesajı listeye ekle 
    messages.insert(0, {"text": text, "image": image, "audio": audio})
    return jsonify({"status": "success", "total": len(messages)}), 201

@app.route("/<path:filename>")
def serve_file(filename):
    """Yüklenen medya dosyalarını döndürür."""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
