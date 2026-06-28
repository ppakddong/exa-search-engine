from exa_py import Exa
from .config import EXA_API_KEY

exa = Exa(EXA_API_KEY)


def search(query, num_results=5):
    response = exa.search(
        query,
        num_results=num_results,
    )
    return response.results