from config import get_llm
from tools import explain_tool, quiz_tool, evaluate_tool, calculator_tool
from agent import create_agent
from db import save_interaction


llm = get_llm()
USER_ID = "user_bikash"


if __name__ == '__main__':
    # LLM test
    question_1 ="Tell me a joke"
    response=llm.invoke(question_1)

    
    # ✅ SAVE FIRST QUESTION
    save_interaction(USER_ID, question_1, response.content)
    print("Saved Q1 ✅")

    print("\n--- TOOL TESTS ---")
    print(explain_tool.invoke("Neural Networks"))
    print(quiz_tool.invoke("Machine Learning"))
    print(evaluate_tool.invoke("ML is training models"))
    print(calculator_tool.invoke("10 / 2 + 3"))

    print("\n--- AGENT TEST ---")

    agent = create_agent()
    question_2="Explain AI and then give me a quiz"

    final_output = ""   # 👈 IMPORTANT (default value)

    # ✅ Save BEFORE processing (production pattern)
    save_interaction(USER_ID, question_2, "PROCESSING...")

    print("Saved initial state ✅")
    try:
        result = result = agent.invoke({
        "messages": [
            {"role": "user", "content": question_2}
        ]
    })

        print("\nFinal Output:")
        print(result["messages"])


        # ✅ SAFE extraction
        if isinstance(result, dict):
            final_output = result.get("output", "")
        else:
            final_output = str(result)

        # fallback if empty
        if not final_output:
            final_output = str(result)

        print("\nFinal Output:")
        print(final_output)

    except Exception as e:
        print("Agent failed ❌")
        print(e)
        final_output = f"ERROR: {str(e)}"

    finally:
        print("\nSaving FINAL output to DB...")
        save_interaction(USER_ID, question_2, final_output)
        print("Saved final output ✅")


# ---------------- DIRECT DB TEST ----------------
    print("\n--- DIRECT DB TEST ---")
    save_interaction(
        USER_ID,
        "user_bikash",
        "test_response_2"
    )
    print("Direct DB save worked ✅")
    
