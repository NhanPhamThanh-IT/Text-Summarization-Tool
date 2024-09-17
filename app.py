from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
import requests
from summarize import Summarize
from utils.fileprocess import ReadFile
from utils.urlprocess import URL

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/summarize-file', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return render_template('home.html', error="No file part in the request !")
    file = request.files['file']
    if file.filename == '':
        return render_template('home.html', error="No file selected for uploading !")
    if file:
        filename = secure_filename(file.filename)
        if not os.path.exists('uploads'):
            os.mkdir('uploads')
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        try:
            file.save(file_path)
            file_helper = ReadFile(file_path)
            os.remove(file_path)
            content = Summarize(file_helper.content)
            summarized_content = content.summarizeBySentence(5)
            return render_template('home.html', summary=summarized_content)
        except Exception as e:
            return render_template('home.html', error=f"An error occurred: {str(e)}")
    return render_template('home.html', error="Something went wrong !")

@app.route('/summarize-doc', methods=['POST'])
def summarize_text():
    if request.method == 'POST':
        text = request.form['text']
        if not text:
            return render_template('home.html', error="Please enter some text to summarize !")
        content = Summarize(text)
        summarized_content = content.summarizeBySentence(5)
        return render_template('home.html', summary=summarized_content)
    return render_template('home.html', error="Something went wrong !")

@app.route('/summarize-file-url', methods=['POST'])
def get_online_file():
    if request.method == 'POST':
        url = request.form.get('url')
        if not url:
            return render_template('home.html', error="Please enter url !")
        try:
            response = requests.get(url)
            response.raise_for_status()
            if not os.path.exists('uploads'):
                os.mkdir('uploads')
            url = URL(response)
            content = Summarize(url.content)
            summarized_content = content.summarizeBySentence(5)
            return render_template('home.html', summary=summarized_content)
        except requests.RequestException as e:
            return render_template('home.html', error="Something went wrong !")

@app.route('/save-local', methods=['POST'])
def save_summary():
    data = request.get_json()
    summary = data.get('summary')
    if not os.path.exists('localsaves'):
        os.mkdir('localsaves')
    with open(os.path.join('localsaves','summary.txt'), 'w') as f:
        f.write(summary)
    return jsonify({'status': 'success', 'summary_received': summary})

if __name__ == '__main__':
    app.run(debug=True)