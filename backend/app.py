from flask import Flask, request, jsonify
import os
from datetime import datetime
from flask_cors import CORS
from whisper_transcribe import transcribe_audio
from summarize import summarize_text
from database import init_db, save_summary

UPLOAD_FOLDER = 'uploads' 

app = Flask(__name__)
CORS(app) 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'mp3','mp4','wav','m4a','acc','mov'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload',methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
        
    file = request.files['file']
    if file.filename=='':
        return jsonify({"error": "No file selected"}), 400
    
    if not allowed_file(file.filename):
        return jsonify({"error": "Unsupported file format"}), 400
    
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    transcribe = transcribe_audio(filepath)

    summary, actions = summarize_text(transcribe)

    save_summary(file.filename, transcribe, summary, actions)

    return jsonify({
        "transcribe": transcribe,
        "summary": summary,
        "action_text": actions,
        "time": datetime.now().isoformat() 
    })

if __name__ == '__main__':
    init_db()
    app.run(debug=True)