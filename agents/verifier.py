from llm.llm_client import GeminiClient

class VerifierAgent:
    def __init__(self):
        self.llm = GeminiClient()

    def verify_and_summarize(self, user_query, execution_results):
        prompt = f"""
        You are a Verifier Agent. 
        User Request: {user_query}
        
        Execution Results from tools:
        {execution_results}
        
        Please formulate a final, comprehensive answer based on the results. 
        If data is missing, admit it politely.
        """
        return self.llm.generate(prompt)