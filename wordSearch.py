import spacy

##VALUES TO MANIPULATE

text_path = "FULL_MACBETH_PLAY.txt" #Path of text document to search through
word = "bird" #Word to search for
threshold = 0.5 #Range: [0,1], where 0 is completely unrelated and 1 is completely related

##################


nlp = spacy.load('en_core_web_lg')

def find_related_words(word, text_path, threshold):
    with open(text_path, 'r') as f:
        text = f.read()
    doc = nlp(text)
    related_words = []
    line_number = 0
    print(f"Beginning Processing. Searching for occurrences of words similar to {word} with threshold {threshold}")
    for line in text.split('\n'):
        line_number += 1
        if line_number % 100 == 0:
            print(f"Processing line number {line_number}")
        for token in nlp(line):
            if token.has_vector and token.is_alpha:
                similarity = token.similarity(nlp(word))
                if similarity > threshold:
                    output_string = f'{similarity*100:.2f}%. {token.text}: "{line}" ({line_number})'
                    related_words.append((similarity, output_string))
    related_words = sorted(related_words, reverse=True)
    return [output_string for _, output_string in related_words]

related_words = find_related_words(word, text_path, threshold)
print(f"\n\nFinished processing. Identified words with threshold {threshold}:")
for result in related_words:
    print(result)
