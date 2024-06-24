from fastapi import FastAPI
from trie import WordTraversal
app = FastAPI()
WORD_TRAVERSAL = WordTraversal()
    
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/search_meaning/{word}')
async def search_word(word):
    print(word)
    return WORD_TRAVERSAL.search_in_trie(word)