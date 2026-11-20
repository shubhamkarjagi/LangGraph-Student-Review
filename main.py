import os
from typing import TypedDict

from dotenv import load_dotenv
from langchain_groq import ChatGroq

from langgraph.graph import StateGraph, START, END

# Load environment variables
load_dotenv()

# Initialize Groq LLM
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.2,
    api_key=os.getenv("GROQ_API_KEY")
)

print("Groq LLM initialized successfully!")

# Define workflow state
class AssignmentState(TypedDict):
    assignment_text: str
    assignment_topic: str
    summary: str
    evaluation: str
    feedback: str

# Node 1: Summarize Assignment
def summarize_assignment(state: AssignmentState):

    print("\nGenerating Assignment Summary...")

    prompt = f"""
    You are an assignment summarization assistant.

    Summarize the following student assignment
    in simple and clear language.

    Assignment Topic:
    {state['assignment_topic']}

    Assignment Text:
    {state['assignment_text']}

    Provide a concise summary covering
    the main points and important concepts.
    """

    response = llm.invoke(prompt)

    return {
        "summary": response.content
    }

# Node 2: Evaluate Assignment
def evaluate_assignment(state: AssignmentState):

    print("\nEvaluating Assignment...")

    prompt = f"""
    You are an academic assignment evaluator.

    Evaluate the student's assignment summary.

    Assignment Topic:
    {state['assignment_topic']}

    Assignment Summary:
    {state['summary']}

    Evaluate using these marking criteria:

    1. Relevance to the topic
    2. Accuracy of information
    3. Completeness of important concepts
    4. Clarity and organization

    Give a score out of 100.

    Explain the strengths and weaknesses.
    """

    response = llm.invoke(prompt)

    return {
        "evaluation": response.content
    }

# Node 3: Generate Feedback
def generate_feedback(state: AssignmentState):

    print("\nGenerating Student Feedback...")

    prompt = f"""
    You are a helpful academic teacher.

    Generate constructive feedback for the student.

    Assignment Topic:
    {state['assignment_topic']}

    Assignment Summary:
    {state['summary']}

    Evaluation:
    {state['evaluation']}

    Provide:

    1. Positive points
    2. Areas for improvement
    3. Suggestions for improvement
    4. Final encouraging remarks

    Make the feedback clear and student-friendly.
    """

    response = llm.invoke(prompt)

    return {
        "feedback": response.content
    }

# Create StateGraph
workflow = StateGraph(AssignmentState)

# Add nodes
workflow.add_node("summarize", summarize_assignment)
workflow.add_node("evaluate", evaluate_assignment)
workflow.add_node("feedback", generate_feedback)

# Add sequential edges
workflow.add_edge(START, "summarize")
workflow.add_edge("summarize", "evaluate")
workflow.add_edge("evaluate", "feedback")
workflow.add_edge("feedback", END)

# Compile workflow
app = workflow.compile()

print("\nLangGraph Workflow Created Successfully!")

print("\nLangGraph Workflow Created Successfully!")

# Input data
assignment_text = """
Artificial Intelligence is transforming education.

It helps students learn through personalized learning,
automated assessments, virtual assistants and smart
learning platforms.

AI improves educational efficiency and provides
better learning experiences.

However, it also creates challenges such as data privacy,
bias and overdependence on technology.

Therefore, AI should be used responsibly in education.
"""

assignment_topic = "The Impact of Artificial Intelligence on Education"

# Run the workflow
result = app.invoke({
    "assignment_text": assignment_text,
    "assignment_topic": assignment_topic
})

# Display results
print("\n========== ASSIGNMENT SUMMARY ==========")
print(result["summary"])

print("\n========== ASSIGNMENT EVALUATION ==========")
print(result["evaluation"])

print("\n========== STUDENT FEEDBACK ==========")
print(result["feedback"])

result = app.invoke({
    "assignment_text": assignment_text,
    "assignment_topic": assignment_topic
})

# Input data
assignment_text = """
Artificial Intelligence is transforming education.

It helps students learn through personalized learning,
automated assessments, virtual assistants and smart
learning platforms.

AI improves educational efficiency and provides
better learning experiences.

However, it also creates challenges such as data privacy,
bias and overdependence on technology.

Therefore, AI should be used responsibly in education.
"""

assignment_topic = "The Impact of Artificial Intelligence on Education"


# Execute workflow only once
print("\nStarting Student Assignment Review Workflow...")

result = app.invoke({
    "assignment_text": assignment_text,
    "assignment_topic": assignment_topic
})


# Display final results
print("\n========== ASSIGNMENT SUMMARY ==========")
print(result["summary"])

print("\n========== ASSIGNMENT EVALUATION ==========")
print(result["evaluation"])

print("\n========== STUDENT FEEDBACK ==========")
print(result["feedback"])

print("\n========== WORKFLOW COMPLETED ==========")

assignment_text = """
Machine Learning is a branch of Artificial Intelligence
that enables computers to learn from data.

It uses algorithms to identify patterns and make
predictions without being explicitly programmed.

Machine Learning is used in healthcare, banking,
education, recommendation systems and self-driving cars.

However, it also faces challenges such as data quality,
overfitting and model bias.
"""

assignment_topic = "Applications and Challenges of Machine Learning"