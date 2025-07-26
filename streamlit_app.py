import streamlit as st
import random

st.set_page_config(page_title="Math Challenge Game", layout="centered")

st.title("🧠 Math Challenge Game")
st.write("Can you solve these quick math problems?")

# Initialize score and question counter
if "score" not in st.session_state:
    st.session_state.score = 0
if "question_count" not in st.session_state:
    st.session_state.question_count = 0

# Generate a new question
def generate_question():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    operator = random.choice(["+", "-", "*"])
    question = f"{a} {operator} {b}"
    answer = eval(question)
    return question, answer

if "question" not in st.session_state:
    st.session_state.question, st.session_state.answer = generate_question()

st.subheader(f"Question {st.session_state.question_count + 1}")
st.markdown(f"**{st.session_state.question} = ?**")

# Input from user
user_answer = st.text_input("Your Answer", "")

if st.button("Submit Answer"):
    if user_answer.strip() != "":
        try:
            if int(user_answer) == st.session_state.answer:
                st.success("✅ Correct!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Incorrect. The correct answer was {st.session_state.answer}.")
            st.session_state.question_count += 1
            st.session_state.question, st.session_state.answer = generate_question()
            st.experimental_rerun()  # 🔁 This forces the app to refresh and display the next question
        except:
            st.warning("⚠️ Please enter a valid number.")
