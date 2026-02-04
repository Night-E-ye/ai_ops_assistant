import requests
from duckduckgo_search import DDGS

class ToolRegistry:
    def get_tool(self, tool_name):
        if tool_name == "github_search":
            return self.github_search
        elif tool_name == "web_search":
            return self.web_search
        else:
            return None

    def github_search(self, query):
        """Searches GitHub for repositories matching the query."""
        if not query: return "Error: No query provided"
        url = f"https://api.github.com/search/repositories?q={query}&sort=stars&order=desc"
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                items = data.get('items', [])[:3] # Get top 3
                if not items: return "No repositories found."
                results = []
                for item in items:
                    results.append(f"Repo: {item['full_name']} | Stars: {item['stargazers_count']} | Desc: {item['description']}")
                return "\n".join(results)
            return f"Error fetching from GitHub: {response.status_code}"
        except Exception as e:
            return f"GitHub Tool Error: {e}"

    def web_search(self, query):
        """Performs a web search using DuckDuckGo."""
        if not query: return "Error: No query provided"
        try:
            results = DDGS().text(query, max_results=3)
            if not results: return "No web results found."
            return "\n".join([f"Title: {r['title']} | Link: {r['href']} | Snippet: {r['body']}" for r in results])
        except Exception as e:
            return f"Search failed: {e}"