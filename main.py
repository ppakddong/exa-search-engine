from src.search import search
from src.display import print_results

print("=" * 50)
print("AI Search Engine")
print("=" * 50)

query = input("검색어를 입력하세요 : ")

results = search(query)

print_results(results)