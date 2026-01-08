# app.py (Upgraded with Interactive Map)
import streamlit as st
import pandas as pd
import pydeck as pdk  # <-- Import Pydeck

# Import functions from our modules
from data.mock_data import get_existing_residents_data, get_pg_data_for_map
from modules.matching_logic import find_best_match

# --- STREAMLIT APP UI ---
st.set_page_config(page_title="VibeMatch", page_icon="👩‍🤝‍👩", layout="wide")

# --- Page Logic: Show results or welcome screen ---
if st.session_state.get('match_found', False):
    st.title("🎉 Here's Your VibeMatch!")
    
    best_match = st.session_state.best_match
    score = st.session_state.score
    explanation = st.session_state.explanation
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("https://static.vecteezy.com/system/resources/previews/009/749/642/original/woman-profile-mascot-illustration-female-avatar-character-icon-cartoon-girl-head-face-business-user-logo-free-vector.jpg", width=150)
        st.metric(label="Compatibility Score", value=f"{score}%", delta="Excellent Match")

    with col2:
        st.subheader(f"Your Recommended Roommate: **{best_match['name']}**")
        st.write(f"Lives at: **{best_match['pg_name']}**")
        
        with st.expander("**See why you're a great match!**"):
            for item in explanation:
                st.write(item)
    
    st.info("Want to start over? Go to the Voice Survey page to create a new profile.")
    st.divider()

else:
    st.title("👩‍🤝‍👩 Welcome to VibeMatch")
    st.header("Find your perfect roommate with the power of AI.")
    st.write("Instead of boring forms, have a quick chat with our AI to find someone who truly matches your lifestyle and vibe.")
    st.success("Click on **'🎤 Voice Survey'** in the sidebar to get started!", icon="👈")

# --- Interactive Dashboard Section ---
st.header("Explore PGs and See Your Matches")

# Load data needed for the dashboard
pg_df = get_pg_data_for_map()
existing_residents_data = get_existing_residents_data()
residents_df = pd.DataFrame(existing_residents_data)

# --- NEW: PYDECK INTERACTIVE MAP ---
st.write("Hover over the points on the map to see PG names!")

# 1. Set the initial view of the map
view_state = pdk.ViewState(
    latitude=pg_df["lat"].mean(), # Center the map on the average latitude
    longitude=pg_df["lon"].mean(),# Center the map on the average longitude
    zoom=12,
    pitch=50  # Gives a nice 3D perspective
)

# 2. Define the layer for our PGs
layer = pdk.Layer(
    "ScatterplotLayer",
    data=pg_df,
    get_position="[lon, lat]",
    get_color="[200, 30, 0, 160]",  # RGBA color
    get_radius=100,
    pickable=True,  # IMPORTANT: This makes the layer interactive
    auto_highlight=True
)

# 3. Define the tooltip content
tooltip = {
    "html": "<b>PG Name:</b> {pg_name}",
    "style": {
        "backgroundColor": "steelblue",
        "color": "white"
    }
}

# 4. Create the DeckGL object (the map itself)
r = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    #map_style="mapbox://styles/mapbox/light-v9", # You can change style: dark-v9, satellite-v9
    map_style=None,
    tooltip=tooltip
)

# 5. Render the map in Streamlit
st.pydeck_chart(r)
# --- END OF NEW MAP SECTION ---

# The dropdown logic remains the same
if st.session_state.get('user_profile'):
    selected_pg = st.selectbox("Or, select a PG from the list:", pg_df["pg_name"])
    
    if selected_pg:
        residents_in_pg = [res for res in existing_residents_data if res["pg_name"] == selected_pg]
        best_match_in_pg, score_in_pg, _ = find_best_match(st.session_state.user_profile, residents_in_pg)
        
        if best_match_in_pg:
            st.subheader(f"Your potential match at {selected_pg}:")
            st.metric(f"Compatibility with {best_match_in_pg['name']}", f"{score_in_pg}%")
        else:
            st.warning(f"No available roommates found at {selected_pg}.")
else:
    st.warning("Complete the Voice Survey to explore your PG matches!")

# --- Admin View in the Sidebar ---
st.sidebar.title("Admin Panel")
if st.sidebar.checkbox("Show Resident Data"):
    st.sidebar.subheader("All Resident Profiles")
    st.sidebar.dataframe(residents_df)