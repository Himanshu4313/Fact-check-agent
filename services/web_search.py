from tavily import TavilyClient
import os

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_claim(claim):

    result = client.search(
        query=claim,
        max_results=5
    )

    return result["results"]