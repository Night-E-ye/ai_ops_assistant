import streamlit as st
import os
from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent
from agents.verifier import VerifierAgent

# Page Config
st.set_page_config(page_title="AI Ops Assistant", page_icon="🤖")

st.title("🤖 AI Operations Assistant")
st.caption("Multi-Agent System: Planner -> Executor -> Verifier")

# --- I REMOVED THE BLOCKING API CHECK FROM HERE ---

query = st.text_input("Enter your request:", placeholder="Ex: Find top 3 React libraries on GitHub and check their latest docs.")

if st.button("Run Agent Workflow"):
    if not query:
        st.warning("Please enter a query.")
    else:
        # 1. PLANNER
        st.subheader("1. 🧠 Planner Agent")
        with st.spinner("Generating plan..."):
            planner = PlannerAgent()
            plan = planner.create_plan(query)
            st.json(plan)
        
        if "error" in plan:
            st.error("Planning failed.")
            st.stop()

        # 2. EXECUTOR
        st.subheader("2. ⚙️ Executor Agent")
        with st.spinner("Executing tools..."):
            executor = ExecutorAgent()
            results, logs = executor.execute_plan(plan)
            
            # Show execution logs
            with st.expander("See Execution Logs"):
                for log in logs:
                    st.write(log)
            
            st.write("Execution Results:", results)

        # 3. VERIFIER
        st.subheader("3. ✅ Verifier Agent")
        with st.spinner("Verifying and summarizing..."):
            verifier = VerifierAgent()
            final_response = verifier.verify_and_summarize(query, results)
            st.markdown("### Final Output")
            st.success(final_response)