<div align="justify">

## Introduction

This project provides a text summarization tool using Natural Language Processing (NLP) with the spaCy library. It helps users extract important sentences from long texts to create a concise summary while retaining the main ideas.

## Features

- Summarizes text by selecting the most important sentences.
- Computes keyword frequency to assess the significance of sentences.
- Allows users to upload text files or input video URLs for summarization.
- Customizable number of sentences in the summary or the percentage ratio of sentences to extract.
- User-friendly local website interface for easy interaction.

## Idea implementation

This project implements **Extractive Summarization** using Natural Language Processing (NLP) techniques. The goal is to identify and extract the most important sentences from a given text based on the frequency of key terms (keywords) such as nouns, verbs, and adjectives.

### Overview

Extractive summarization is a method where important sentences are selected directly from the original text to create a summary. This approach contrasts with **abstractive summarization**, which generates new sentences. In this implementation, the focus is on **extracting** the most relevant sentences based on word frequencies.

### Key Concepts

- **Keywords**: Important words are identified as **nouns (NOUN)**, **verbs (VERB)**, and **adjectives (ADJ)**, while common stop words are excluded.
- **Sentence Scoring**: Each sentence in the text is assigned a score based on the total frequency of important words it contains. Sentences with the highest scores are considered the most relevant and included in the summary.
- **Summarization Methods**:
  - `summarizeBySentence`: Summarizes the text by selecting a fixed number of top sentences.
  - `summarizeByRatio`: Summarizes the text by selecting a percentage of the total sentences based on their importance.

### How It Works

1. **Preprocessing**: The text is processed using the spaCy NLP library. We tokenize the text, split it into sentences, and identify important keywords (nouns, verbs, adjectives).
2. **Frequency Analysis**: The frequency of each keyword is calculated, and these frequencies are used to determine the importance of each sentence.
3. **Sentence Selection**: Sentences are ranked by their score (based on keyword frequency), and the top-ranked sentences are selected to form the summary.

## Setup

```batch
pip install -r requirements.txt
```

## Local Website Interface

To launch the local website, run the following command:

```bash
python app.py
```

Open your web browser and go to http://127.0.0.1:5000 to access the interface. Users can interact with the application, upload files, and enter video URLs for summarization.

## Conclusion

This extractive summarization technique offers a simple yet powerful way to extract key information from large texts. It’s especially useful in applications like document summarization, news analysis, and content extraction, where extracting core sentences from a large corpus of text is required.

## License

This project is licensed under the BSD 3-Clause License. See the <a href='https://github.com/NhanPhamThanh-IT/Text-Summarization-Tool/blob/main/LICENSE'>LICENSE file</a> for more details.

## Contact

If you have any questions, please reach out via email: [ptnhanit230104@gmail.com]

## References

<strong>

spacy module documents

- <a href='https://spacy.io/'>Industrial-Strength Natural Language Processing in Python</a>
- <a href='https://github.com/explosion/spaCy'>explosion - 
spaCy - Industrial-strength Natural Language Processing (NLP) in Python</a>

Flask module documents

- <a href='https://flask.palletsprojects.com/en/3.0.x/'>Welcome to Flask — Flask Documentation (3.0.x)</a>
- <a href='https://pypi.org/project/Flask/'>Flask</a>
- <a href='https://github.com/pallets/flask'>pallets - flask - The Python micro framework for building web applications</a>

youtube-transcript-api module documents

- <a href='https://pypi.org/project/youtube-transcript-api/'>youtube-transcript-api 0.6.2</a>

PyMuPDF module documents

- <a href='https://pymupdf.readthedocs.io/en/latest/'>PyMuPDF 1.24.10 documentation</a>
- <a href='https://github.com/pymupdf/PyMuPDF'>pymupdf - PyMuPDF</a>
- <a href='https://pypi.org/project/PyMuPDF/'>PyMuPDF 1.24.10</a>

python-docx module documents

- <a href='https://python-docx.readthedocs.io/en/latest/'>python-docx — python-docx 1.1.2 documentation</a>
- <a href='https://pypi.org/project/python-docx/'>python-docx 1.1.2</a>

</strong>

</div>