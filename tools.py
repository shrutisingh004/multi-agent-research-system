import requests
from langchain.tools import tool
from bs4 import BeautifulSoup
from ddgs import DDGS

# Tool 1: Web Search using DuckDuckGo
@tool
def web_search(query: str) -> str:
    """Search the web for recent and reliable information on a topic. Returns Titles, URLs and snippets."""
    results_list = []
    
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=5)
        
        for r in results:
            results_list.append(
                f"Title: {r.get('title')}\n"
                f"URL: {r.get('href')}\n"
                f"Snippet: {r.get('body')}\n"
            )

    if not results_list:
        return "No results found."
    
    return "\n\n".join(results_list)

# print(web_search.invoke("What is the recent news of war?"))

# Tool 2: Web Scraping using BeautifulSoup
@tool
def scrape_url(url: str) -> str:
    """Scrape the content of a given URL and return the main text."""
    try:
        response = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})    
        soup = BeautifulSoup(response.text, "html.parser")

        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()

        return soup.get_text(separator=" ", strip=True)[:3000]
    
    except Exception as e:
        return f"Error scraping URL: {str(e)}"
    
# print(scrape_url.invoke("https://www.bbc.com/news/live/c3w378e6dnlt?page=3"))
