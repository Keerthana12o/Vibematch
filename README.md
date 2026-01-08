# VibeMatch 👩‍🤝‍👩

An AI-powered personalized roommate matching system for women's co-living spaces. VibeMatch moves beyond simple surveys to understand user *personality* and *vibe*, creating happier and more compatible living arrangements.

AI-Powered Personalized Roommate Matching for Women's Co-Living Spaces

---

## ✨ Key Features

*   **Survey:** A friendly, multi-step "Vibe Check" survey that feels like a conversation, not a form. This captures user preferences in a natural and engaging way.
*   **🧠 AI-Powered "Vibe Check" Algorithm:** A smart matching logic that scores compatibility based on key lifestyle attributes like sleep schedule, cleanliness, and social habits, with a unique "vibe" score boost for matching personalities.
*   **🗺️ Interactive Map Dashboard:** An interactive map built with Pydeck that displays available PGs (co-living spaces). Users can hover over locations to see names and use a dropdown to get instant compatibility scores for residents in each building.
*   **📊 Clean, Multi-Page Interface:** A polished and intuitive user interface built with Streamlit, featuring a dedicated survey page, a dynamic results page, and a simple admin view.
*   **🔒 Secure API Key Management:** Uses Streamlit's built-in secrets management for handling the Mapbox API key safely.

---


---

## 🛠️ Tech Stack

*   **Language:** Python 3.9
*   **Framework:** Streamlit
*   **Data Handling:** Pandas
*   **Mapping & Visualization:** Pydeck

---

## 📂 Project Structure

```
VibeMatch/
├── .streamlit/
│   └── secrets.toml        # For storing the Mapbox API Key
├── assets/
│   └── avatar.png          # Local image assets
├── data/
│   └── mock_data.py        # Mock data for users and PGs
├── modules/
│   └── matching_logic.py   # The core matching algorithm
├── pages/
│   └── 1_🎤_Voice_Survey.py # The multi-step survey page
├── app.py                  # Main application file (welcome/results page)
└── requirements.txt        # Python dependencies
```

---

## ⚙️ Setup and Installation

Follow these steps to run the project locally.

### Prerequisites

*   Python 3.9 or higher
*   An IDE like VS Code
*   A Mapbox Account (for the interactive map)

### 1. Clone the Repository

```bash
git clone https://github.com/Keerthana12o/Vibematch.git
cd VibeMatch
```

### 2. Create and Activate a Virtual Environment

*   **Windows:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```


### 3. Install Dependencies

All required libraries are listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```



### 4. Run the Streamlit App

Once the setup is complete, run the following command in your terminal:

```bash
streamlit run app.py
```

browser should automatically open to the VibeMatch application!

---

## 🚀 How to Use the App

1.  **Welcome Page:** The app opens with a welcome message.
2.  **Take the Survey:** Navigate to the **"Survey"** page from the sidebar.
3.  **Answer the Questions:** Complete the four-step survey by selecting your preferences.
4.  **View Your Match:** After the final question, you will be automatically redirected to the main page, which will now display your best roommate match and a detailed compatibility breakdown.
5.  **Explore PGs:** Use the interactive map on the main page to hover over different co-living spaces or use the dropdown to see your compatibility with potential roommates in other buildings.
