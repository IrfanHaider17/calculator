# app.py
import streamlit as st

# Custom CSS for styling and background image
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1533134486753-c833f0ed4866?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80");
        background-size: cover;
        background-position: center;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        padding: 10px 24px;
        border-radius: 8px;
        border: none;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .stSelectbox div {
        font-size: 18px;
    }
    .stNumberInput input {
        font-size: 18px;
    }
    .stMarkdown h1 {
        text-align: center;
        color: #4CAF50;
    }
    .stSuccess {
        font-size: 20px;
        text-align: center;
        padding: 10px;
        border-radius: 8px;
        background-color: #d4edda;
        color: #155724;
    }
    .main {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 20px;
        border-radius: 10px;
        margin: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main container for the app
st.markdown("<div class='main'>", unsafe_allow_html=True)

# Title of the application
st.markdown("<h1>✨ Simple Arithmetic Calculator ✨</h1>", unsafe_allow_html=True)

# Layout with columns for better UI
col1, col2 = st.columns(2)

# Input fields for numbers
with col1:
    num1 = st.number_input("Enter the first number", value=0.0, step=1.0)

with col2:
    num2 = st.number_input("Enter the second number", value=0.0, step=1.0)

# Dropdown to select the operation
operation = st.selectbox(
    "Select an operation",
    ["Addition", "Subtraction", "Multiplication", "Division"],
    index=0,
    help="Choose the arithmetic operation you want to perform.",
)

# Function to perform calculations
def calculate(num1, num2, operation):
    if operation == "Addition":
        return num1 + num2
    elif operation == "Subtraction":
        return num1 - num2
    elif operation == "Multiplication":
        return num1 * num2
    elif operation == "Division":
        if num2 == 0:
            return "Error: Division by zero!"
        return num1 / num2
    else:
        return "Invalid operation"

# Button to perform calculation
if st.button("Calculate 🚀", key="calculate_button"):
    result = calculate(num1, num2, operation)
    st.markdown(f"<div class='stSuccess'>Result: {result}</div>", unsafe_allow_html=True)

# Close the main container
st.markdown("</div>", unsafe_allow_html=True)
