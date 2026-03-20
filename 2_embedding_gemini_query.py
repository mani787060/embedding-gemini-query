"""from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

result = embedding.embed_query("Delhi is the capital of India")

print(str(result))"""



import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

# Silence the PyTorch warning
os.environ["TRANSFORMERS_VERBOSITY"] = "error"

load_dotenv()

# The model name 'gemini-embedding-001' is the new stable standard for 2026
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001", 
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Test query
text = "Delhi is the capital of India"

try:
    # Google's embeddings usually return a 768-dimension vector
    vector = embeddings.embed_query(text)
    print(f"✅ Success! Connection established.")
    print(f"Vector length: {len(vector)}")
    print(f"First 32 values: {vector[:32]}")
except Exception as e:
    print(f"❌ Still failing? Check this error: {e}")