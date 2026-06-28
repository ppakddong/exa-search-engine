from exa_py import Exa
from src.config import EXA_API_KEY

exa = Exa(EXA_API_KEY)


def search(query, num_results=5, domain=None):

    kwargs = {
        "query": query,
        "num_results": num_results,
    }

    if domain:
        kwargs["include_domains"] = [domain]

    response = exa.search(**kwargs)

    return response.results