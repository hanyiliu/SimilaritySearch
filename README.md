# SimilaritySearch
 Search for related occurrences of a specified word in a text file.

## Setup
  1. Install required dependencies in Terminal (macOS), Command Prompt (Windows), or equivalent:
  ```
  pip install spacy
  python -m spacy download en_core_web_lg
  ```
  If console returns "command not found," try adding your python version after first keyword (ex: 'pip install' -> 'pip3.9 install')

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
  
  4. After it has finished, this will be the expected output:
  ```
  Finished processing. Identified words with threshold 0.5:
  100.00%. bird: "Poor bird! thou'ldst never fear the net nor lime," (2357)
  100.00%. bird: "New hatch'd to the woeful time: the obscure bird" (1082)
  100.00%. bird: "Buttress, nor coign of vantage, but this bird" (577)
  84.43%. birds: "Why should I, mother? Poor birds they are not set for." (2360)
  84.43%. birds: "The most diminutive of birds, will fight," (2319)
  84.43%. birds: "As birds do, mother." (2351)
  65.02%. owl: "Was by a mousing owl hawk'd at and kill'd." (1265)
  65.02%. owl: "It was the owl that shriek'd, the fatal bellman," (838)
  65.02%. owl: "I heard the owl scream and the crickets cry." (859)
  65.02%. owl: "Her young ones in her nest, against the owl." (2320)
  64.74%. crow: "Which keeps me pale! Light thickens; and the crow" (1609)
  62.93%. sparrows: "As sparrows eagles, or the hare the lion." (82)
  61.71%. falcon: "A falcon, towering in her pride of place," (1264)
  60.70%. eagles: "As sparrows eagles, or the hare the lion." (82)
  ...
  50.17%. goose: "Where got'st thou that goose look?" (2996)
  ```
  
## Credits
  Included text file of Macbeth taken from http://shakespeare.mit.edu/macbeth/full.html.
 

  
