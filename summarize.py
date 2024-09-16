import spacy
from collections import Counter
from support import preprocess_text

def score_sentence(sentence : str, word_freq : dict) -> int:
    """
    Calculate the score of a sentence based on word frequencies.

    The score is computed by summing the frequency values of each word in the sentence.
    The frequency values are obtained from the `word_freq` dictionary, which maps words to their respective frequencies.

    Parameters:
        sentence (str): The input sentence to be scored. It is assumed to be tokenized as a list of words.
        word_freq (dict): A dictionary where the keys are words and the values are their frequencies.

    Returns:
        int: The total score of the sentence based on word frequencies.

    Example:
        >>> word_freq = {'hello': 5, 'world': 3}
        >>> score_sentence('Hello world', word_freq)
        8
    """
    score = 0
    for token in sentence:
        if token.text.lower() in word_freq:
            score += word_freq[token.text.lower()]
    return score

class Summarize:
    def __init__(self, text : str) -> None:
        """
        Initialize the summarize object with the given text and prepare necessary data for summarization.

        This method processes the input text using spaCy to perform various tasks:
            - Loads the spaCy language model and processes the text to create a document object.
            - Splits the text into sentences.
            - Extracts important keywords (nouns, verbs, adjectives) from the text while ignoring stop words.
            - Computes the frequency of each keyword.

        Parameters:
            text (str): The input text to be processed and summarized.

        Attributes:
            text (str): The original input text.
            doc (spacy.tokens.Doc): The spaCy document object created from the input text.
            sentences (list): A list of spaCy sentence objects derived from the document.
            keywords (list): A list of important keywords extracted from the text.
            word_freq (Counter): A Counter object mapping each keyword to its frequency in the text.

        Example:
            >>> summarizer = Summarize("This is an example text. It includes several sentences.")
            >>> summarizer.sentences
            [This is an example text., It includes several sentences.]
            >>> summarizer.keywords
            ['example', 'text', 'includes', 'several', 'sentences']
            >>> summarizer.word_freq
            Counter({'example': 1, 'text': 1, 'includes': 1, 'several': 1, 'sentences': 1})
        """
        self.text = preprocess_text(text)
        self.doc = spacy.load('en_core_web_sm')(self.text)
        self.sentences = list(self.doc.sents)
        # Take the important keywords which appear in the text.
        self.keywords = [token.text.lower() for token in self.doc if token.pos_ in ('NOUN', 'VERB', 'ADJ') and not token.is_stop]
        # Take the frequency of each important keyword.
        self.word_freq = Counter(self.keywords)

    def summarizeBySentence(self, num_sentence : int = 3) -> str:
        """
        Summarize the text by selecting the top `num_sentence` most important sentences.

        The importance of each sentence is determined based on its score, which is calculated
        using word frequencies from the `self.word_freq` dictionary. The sentences are first
        scored, then sorted in descending order of their scores. The top `num_sentence` sentences
        are selected and sorted back to their original order before being joined into a summary.

        Parameters:
            num_sentence (int): The number of top sentences to include in the summary. Default is 3.

        Returns:
            str: A summary consisting of the top `num_sentence` sentences, joined into a single string.

        Example:
            >>> self.sentences = ["This is the first sentence.", "Here is another sentence.", "The final sentence is here."]
            >>> self.word_freq = {'sentence': 5, 'is': 3, 'the': 2}
            >>> self.summarizeBySentence(num_sentence=2)
            'This is the first sentence. Here is another sentence.'
        """
        sentence_scores = [(sent, score_sentence(sent, self.word_freq)) for sent in self.sentences]
        sorted_sentences = sorted(sentence_scores, key=lambda x: x[1], reverse=True)
        top_sentences = sorted_sentences[:num_sentence]
        top_sentences = sorted(top_sentences, key=lambda x: self.sentences.index(x[0]))
        summary = ' '.join(str(sent[0]) for sent in top_sentences)
        return summary