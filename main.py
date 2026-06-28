import os

from dotenv import load_dotenv
from exa_py import Exa

load_dotenv()
print(os.getenv("EXA_API_KEY")) 
exa = Exa(os.getenv("EXA_API_KEY"))

query = input("Search here: ")

response = exa.search(
    query,
    num_results=5,
    type="keyword",
    include_domains=["https://www.tiktok.com"],
)

for result in response.results:
    print(f"Title: {result.title}")
    print(f"URL: {result.url}")
    print()