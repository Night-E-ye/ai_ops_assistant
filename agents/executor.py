from tools.tool_registry import ToolRegistry

class ExecutorAgent:
    def __init__(self):
        self.tools = ToolRegistry()

    def execute_plan(self, plan):
        results = {}
        logs = []
        
        if "steps" not in plan:
            return {"error": "Invalid plan format"}, logs

        for step in plan['steps']:
            step_id = step['step_id']
            tool_name = step.get('tool')
            query = step.get('query')
            
            logs.append(f"Executing Step {step_id}: {step['description']}")
            
            if tool_name and tool_name != "null":
                tool_func = self.tools.get_tool(tool_name)
                if tool_func:
                    output = tool_func(query)
                    results[step_id] = output
                    logs.append(f"Tool Output ({tool_name}): {output[:100]}...") # Truncate for log
                else:
                    results[step_id] = "Tool not found."
            else:
                results[step_id] = "No tool required for this step."
                
        return results, logs