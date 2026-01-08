# pages/1_🎤_Voice_Survey.py (Final Corrected Version)

# --- 1. IMPORTS ---
import streamlit as st
import time
from data.mock_data import get_existing_residents_data
from modules.matching_logic import find_best_match

# --- 2. PAGE CONFIGURATION ---
st.set_page_config(page_title="Voice Survey", page_icon="🎤")

# --- 3. ROBUST SESSION STATE INITIALIZATION ---
# This block is the key fix. It ensures all required session state
# variables exist before any other code tries to use them.

if 'stage' not in st.session_state:
    st.session_state.stage = 0
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = {}
if 'match_found' not in st.session_state:
    st.session_state.match_found = False

# This part handles the "Start Over" logic.
# If a user comes back to this page after a match was found, reset everything.
if st.session_state.match_found:
    st.toast("Starting a new Vibe Check!")
    st.session_state.stage = 0
    st.session_state.user_profile = {}
    st.session_state.match_found = False

# --- 4. PAGE UI AND LOGIC ---

st.title("🎤 The Vibe Check Survey")
st.write("Let's get to know you. Answer a few quick questions.")

# --- QUESTION 1: Schedule ---
if st.session_state.stage == 0:
    st.header("Question 1: Your Daily Rhythm")
    st.write("Are you more of an early bird or a night owl?")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("I'm an Early Bird ☀️", use_container_width=True):
            st.session_state.user_profile['schedule'] = 'early_bird'
            st.session_state.stage = 1
            st.rerun()
    with col2:
        if st.button("I'm a Night Owl 🌙", use_container_width=True):
            st.session_state.user_profile['schedule'] = 'night_owl'
            st.session_state.stage = 1
            st.rerun()

# --- QUESTION 2: Cleanliness ---
if st.session_state.stage == 1:
    st.header("Question 2: Your Space")
    st.write("How do you prefer your shared living space?")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Super Tidy and Organized ✨", use_container_width=True):
            st.session_state.user_profile['cleanliness'] = 'tidy'
            st.session_state.stage = 2
            st.rerun()
    with col2:
        if st.button("Relaxed and Lived-in 😌", use_container_width=True):
            st.session_state.user_profile['cleanliness'] = 'relaxed'
            st.session_state.stage = 2
            st.rerun()

# --- QUESTION 3: Social Style ---
if st.session_state.stage == 2:
    st.header("Question 3: Social Energy")
    st.write("What's your social style at home?")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("I love having friends over 🎉", use_container_width=True):
            st.session_state.user_profile['social_style'] = 'social'
            st.session_state.stage = 3
            st.rerun()
    with col2:
        if st.button("I prefer a quiet sanctuary 📚", use_container_width=True):
            st.session_state.user_profile['social_style'] = 'quiet'
            st.session_state.stage = 3
            st.rerun()
        
# --- QUESTION 4: The "Vibe" ---
if st.session_state.stage == 3:
    st.header("Question 4: The Vibe Check")
    st.write("This is where the AI would analyze your tone. For now, what's your general outlook?")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Positive and Community-Focused 😊", use_container_width=True):
            st.session_state.user_profile['vibe'] = 'positive'
            st.session_state.stage = 4
            st.rerun()
    with col2:
        if st.button("Just looking for a quiet, neutral space 🙂", use_container_width=True):
            st.session_state.user_profile['vibe'] = 'neutral'
            st.session_state.stage = 4
            st.rerun()

# --- FINAL STAGE: PROCESSING AND MATCHING ---
if st.session_state.stage == 4:
    st.header("Amazing! Thank you.")
    st.write("We've gathered your preferences. Now, let's find your VibeMatch!")

    if len(st.session_state.user_profile) == 4:
        with st.spinner("Analyzing your profile and finding the best match..."):
            time.sleep(2)
            
            existing_residents = get_existing_residents_data()
            best_match, score, explanation = find_best_match(st.session_state.user_profile, existing_residents)
            
            st.session_state.match_found = True
            st.session_state.best_match = best_match
            st.session_state.score = score
            st.session_state.explanation = explanation
            
            st.success("Match Found! Redirecting to your results...")
            time.sleep(1)
        
        st.switch_page("app.py")
    else:
        st.error("It looks like the survey is incomplete. Please start over.")
        if st.button("Start Over"):
            st.session_state.stage = 0
            st.rerun()

# Show a summary of answers in the sidebar for better UX
if st.session_state.user_profile:
    st.sidebar.write("Your Answers So Far:")
    st.sidebar.json(st.session_state.user_profile)