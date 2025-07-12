#1. imports

#imports fastapi class and httpexpection
from fastapi import FastAPI, HTTPException
#basemodel for data validation
from pydantic import BaseModel
#natual language toolkit
import nltk
#split test into individual words
from nltk.tokenize import word_tokenize
#list of common words - removed
from nltk.corpus import stopwords
#reduces words to their base
from nltk.stem import WordNetLemmatizer

#2. downloads

#pre-trained tokenizer model for splitting text into words
nltk.download('punkt')
nltk.download('punkt_tab')
#dataset containing stopwords
nltk.download('stopwords')
#lemmentization - from lexical database
nltk.download('wordnet')

#3. fastAPI application initialization
app = FastAPI()

#4. input model

#defines pydantic model - inherits from BaseModel
class TextInput(BaseModel):
    text: str
    
#5. NLTK tools initialization

#creates a set of stopwords of English stop words
stopWords = set(stopwords.words('english'))
#used to reduce words to their base forms
lemmatizer = WordNetLemmatizer()

#6. API endpoint

#defines api endpoint - accepts http POST request
@app.post("/preprocess")
#indicates function is asynchronous
async def preprocessText(input: TextInput):
    try:
        #accepts text field from TextInput - converts text to lower - splits ext into list of tokens
        tokens = word_tokenize(input.text.lower())
        #list comprehension to filter tokens
        tokens = [token for token in tokens if token.isalpha() and token not in stopWords]
        #return a JSON response
        return {"tokens" : tokens}
    except Exception as e:
        #catch any exceptions
        raise HTTPException(status_code = 500, detail = f"Error processing text {str(e)}")