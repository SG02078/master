from langchain.tools import tool

@tool
def explain_tool(topic: str) -> str:
    """
    Explain a concept in simple terms for students.
    """
    return f"Here is a simple explanation of {topic}."
@tool
def quiz_tool(topic: str) -> str:
    """
    Generate 3 quiz questions for a given topic.
    """
    return f"Quiz on {topic}:\n1. Question 1\n2. Question 2\n3. Question 3"
@tool
def evaluate_tool(answer: str) -> str:
    """
    Evaluate a student's answer and give feedback.
    """
    return f"Feedback: Your answer '{answer}' needs improvement."
@tool
def calculator_tool(expression: str) -> str:
    """
    Solve math expressions.
    """
    try:
        return str(eval(expression))
    except Exception:
        return "Error in calculation"
