import json
from llm.llm_client import GeminiClient

class PlannerAgent:
    def __init__(self):
        self.llm = GeminiClient()

    def create_plan(self, user_query):
        prompt = f"""
        You are an AI Planner. Given a user request, break it down into logical steps.
        You have access to two tools:
        1. 'github_search': Use this to find code repositories. 
           IMPORTANT: For the 'query' field, output ONLY the topic keywords (e.g., "react libraries"). 
           DO NOT include technical flags like "sort:stars", "per_page", or "stars:>1000".
           The tool handles sorting automatically.
           
        2. 'web_search': Use this to find general information, documentation, or news.
        
        Return a valid JSON object strictly following this structure:
        {{
            "steps": [
                {{
                    "step_id": 1,
                    "description": "What to do",
                    "tool": "tool_name_or_null",
                    "query": "simple_search_topic_only"
                }}
            ]
        }}
        
        User Request: {user_query}
        Provide ONLY JSON. No markdown formatting.
        """
        response = self.llm.generate(prompt)
        cleaned_response = response.replace("```json", "").replace("```", "").strip()
        try:
            return json.loads(cleaned_response)
        except json.JSONDecodeError:
            return {"error": "Failed to parse plan", "raw": response}