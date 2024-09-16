from flask import Flask, render_template, request
from summarize import Summarize
from support import ReadFile
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/summarize-file', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return render_template('home.html')
    file = request.files['file']
    if file.filename == '':
        return render_template('home.html')
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        file_helper = ReadFile(file_path)
        print(file_helper.content)
    return render_template('home.html')

@app.route('/summarize-doc', methods=['POST'])
def summarize_text():
    if request.method == 'POST':
        text = request.form['text']
        content = Summarize(text)
        summarized_content = content.summarizeBySentence(5)
        return render_template('home.html', original_text=text, summary=summarized_content)

if __name__ == '__main__':
    app.run(debug=True)