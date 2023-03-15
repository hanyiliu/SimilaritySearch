# SimilaritySearch
 Search for related occurrences of a specified word in a text file.

## Setup
  1. Install required dependencies in Terminal (macOS), Command Prompt (Windows), or equivalent:
  ```
  pip install spacy
  python -m spacy download en_core_web_lg
  ```
    If console returns "command not found," try adding your python version after first keyword (ex: 'pip install'-> 'pip3.9 install')

  2. Open 'wordSearch.py', and change the variables inside:
  ```
  text_path = "FULL_MACBETH_PLAY.txt" #Path of text document to search through
  word = "bird" #Word to search for
  threshold = 0.5 #Range [0,1]. Minimum cutoff for word's match rate, with 0 being unrelated and 1 being completely related
  ```

  3. Run wordSearch in console while in its directory:
  ```
  python wordSearch.py
  ```

  
