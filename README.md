# ✨ Simple Arithmetic Calculator  

A lightweight and interactive **Streamlit web application** that performs basic arithmetic operations:  
➕ Addition | ➖ Subtraction | ✖️ Multiplication | ➗ Division  

The app features a clean **UI with custom styling** and a background image to enhance user experience.  
---

## 🚀 Features
- Enter two numbers and select an arithmetic operation.  
- Supports Addition, Subtraction, Multiplication, and Division.  
- Handles division by zero gracefully with error message.  
- Beautiful UI with **custom CSS styling**.  
- Runs directly in the browser via **Streamlit**.  

---

## 🔧 Tech Stack
- **Language:** Python 3  
- **Framework:** [Streamlit](https://streamlit.io/)  
- **UI:** Custom CSS  

---

## 📂 Project Structure
calculator-app/
│── .devcontainer/ # VS Code dev container setup
│ └── devcontainer.json
│── app.py # Main Streamlit app
│── requirements.txt # Project dependencies
│── README.md # Project documentation

yaml
Copy code

---

## ⚙️ Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/your-username/calculator-app.git
cd calculator-app
Create virtual environment (optional but recommended)

bash
Copy code
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
Install dependencies

bash
Copy code
pip install -r requirements.txt
Run the app

bash
Copy code
streamlit run app.py
Open in browser at:
👉 (https://calculator-irfan.streamlit.app/)
