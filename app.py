from flask import Flask, render_template, request
from summarize import summarize

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/summarize', methods=['POST'])
def summarize_text():
    if request.method == 'POST':
        text = request.form['text']
        content = summarize(text)
        summarized_content = content.summarizeBySentence(5)
        return render_template('home.html', original_text=text, summary=summarized_content)

if __name__ == '__main__':
    app.run(debug=True)