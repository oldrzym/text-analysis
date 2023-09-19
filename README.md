# text-analysis

---

## **Text Analysis Project**

This project is a tool for analyzing text and finding the closest standard phrases to user-entered phrases.

### **Technologies Used:**

- **Python**: A high-level programming language chosen for its simplicity and powerful libraries for text processing.
- **Gensim**: A Python library for topic modeling and natural language processing. It's used for working with the Word2Vec model.
- **spaCy**: A Python library for natural language processing. Used for splitting the text into phrases.

### **Installation:**

1. Install Python if not already installed.
2. Clone this repository or download and unzip the archive.
3. Navigate to the project directory and install the required libraries:

```bash
pip install gensim spacy
python -m spacy download en_core_web_sm
```

4. Run the script:

```bash
python text_analysis.py
```

### **Design Justifications:**

- **Using Word2Vec**: This model was chosen because of its ability to effectively represent words as vectors, allowing for easy comparison of semantic similarity between words and phrases.
- **Text Splitting with spaCy**: spaCy is one of the most advanced libraries for natural language processing. It provides tools for deep parsing of the grammatical structure of the text, allowing for effective segmentation of text into individual phrases.
- **Text input via the command line**: This was done to simplify the interface and to make the project as portable and independent from third-party interface libraries as possible.

---

