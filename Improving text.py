#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import gensim.downloader as api
import numpy as np
import spacy

model = api.load("word2vec-google-news-300")

standard_phrases = [
    'Optimal performance', 
    'Utilise resources',
    'Enhance productivity',
    'Conduct an analysis',
    'Maintain a high standard',
    'Implement best practices',
    'Ensure compliance',
    'Streamline operations',
    'Foster innovation',
    'Drive growth',
    'Leverage synergies',
    'Demonstrate leadership',
    'Exercise due diligence',
    'Maximize stakeholder value',
    'Prioritise tasks',
    'Facilitate collaboration',
    'Monitor performance metrics',
    'Execute strategies',
    'Gauge effectiveness',
    'Champion change'
]

def get_phrase_vector(phrase):
    words = phrase.split()
    vectors = [model[word] for word in words if word in model]
    if not vectors:
        return None
    return np.mean(vectors, axis=0)

def find_closest_standard_phrase(phrase):
    phrase_vector = get_phrase_vector(phrase)
    if phrase_vector is None:
        return None, 0
    
    max_similarity = -np.inf
    closest_phrase = None

    for std_phrase in standard_phrases:
        std_phrase_vector = get_phrase_vector(std_phrase)
        if std_phrase_vector is not None:
            similarity = np.dot(phrase_vector, std_phrase_vector) / (np.linalg.norm(phrase_vector) * np.linalg.norm(std_phrase_vector))
            if similarity > max_similarity:
                max_similarity = similarity
                closest_phrase = std_phrase

    return closest_phrase, max_similarity

nlp = spacy.load("en_core_web_sm")

def split_text_using_dependency_parsing(text):
    doc = nlp(text)
    
    phrase_bounds = [tok.i for tok in doc if tok.dep_ in ('cc', 'conj', 'prep', 'punct') or tok.pos_ == "VERB"]
    phrase_bounds = sorted(list(set(phrase_bounds)))

    phrases = []
    start = 0
    for end in phrase_bounds:
        if end > start:
            phrases.append(doc[start:end].text.strip())
            start = end
    phrases.append(doc[start:].text.strip())
    
    return [phrase for phrase in phrases if phrase]

def main():
    user_text = input("Please enter your text: ")

    phrases = split_text_using_dependency_parsing(user_text)

    results = []
    for phrase in phrases:
        closest_phrase, similarity_score = find_closest_standard_phrase(phrase)
        results.append((phrase, closest_phrase, similarity_score))

    sorted_results = sorted(results, key=lambda x: x[2], reverse=True)

    for original, standard, score in sorted_results:
        print(f"Original phrase: '{original}'")
        print(f"Closest standard phrase: '{standard}' with similarity score of {score:.2f}")
        print("-----------------------------------------------------------")

if __name__ == "__main__":
    main()

