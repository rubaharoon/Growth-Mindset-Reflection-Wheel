import streamlit as st
import random
import datetime

# Page settings
st.set_page_config(page_title="Reflection Wheel", layout="wide")

st.title("🎡 Growth Mindset Reflection Wheel")

# Initialize session state
if "xp" not in st.session_state:
    st.session_state.xp = 0
if "journal" not in st.session_state:
    st.session_state.journal = []
if "current_question" not in st.session_state:
    st.session_state.current_question = None

# List of reflection questions
questions = [
    "What was a challenge you faced recently, and how did you overcome it?",
    "What is something new you learned this week?",
    "Think of a past mistake. What did you learn from it?",
    "How do you handle failure, and how can you improve?",
    "Describe a time you stepped out of your comfort zone.",
    "What is a goal you're working towards, and what small step can you take today?",
    "Who inspires you the most, and why?",
    "What negative thought do you need to replace with a positive one?",
    "How do you deal with self-doubt?",
    "What advice would you give to your younger self?"
]

# Spin the wheel
if st.button("🎡 Spin the Reflection Wheel"):
    st.session_state.current_question = random.choice(questions)

# Show the selected question
if st.session_state.current_question:
    st.header("📝 Your Reflection Question:")
    st.success(st.session_state.current_question)

    # Journal input
    journal_entry = st.text_area("Write your response:")

    # Submit journal entry
    if st.button("Save Reflection"):
        if journal_entry:
            today = datetime.date.today()
            st.session_state.journal.append(f"{today}: {st.session_state.current_question}\nResponse: {journal_entry}")
            st.session_state.xp += 10
            st.success(f"✅ Reflection saved! You earned 10 XP. 🏆 Total XP: {st.session_state.xp}")
        else:
            st.warning("Please write your reflection before saving!")

# Show XP progress
st.sidebar.title("📊 Your Progress")
st.sidebar.write(f"🏆 XP: {st.session_state.xp}")

# Download Journal as a Text File
st.header("📥 Download Your Journal")

if st.button("Export Journal as Text File"):
    if st.session_state.journal:
        journal_text = "\n\n".join(st.session_state.journal)
        st.download_button(
            label="📥 Download Journal",
            data=journal_text.encode(),
            file_name="Mindset_Reflection_Journal.txt",
            mime="text/plain"
        )
    else:
        st.warning("No journal entries to export!")

# List of motivational quotes
quotes = [
    "🌱 *Success is not an accident, success is a choice.* – Stephen Curry",
    "🔥 *Your only limit is your mind.* – Unknown",
    "🚀 *Growth and comfort do not coexist.* – Ginni Rometty",
    "💡 *Every expert was once a beginner.* – Helen Hayes",
    "🏆 *The only way to do great work is to love what you do.* – Steve Jobs"
]

# Randomly select a quote
selected_quote = random.choice(quotes)

# Footer with random quote
st.markdown("---")
st.write(selected_quote)
st.write("Developed with ❤️ by Ruba Haroon")
