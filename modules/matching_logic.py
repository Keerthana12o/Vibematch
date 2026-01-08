# modules/matching_logic.py

def calculate_match_score(profile1, profile2):
    """Calculates a compatibility score between two profiles."""
    score = 0
    explanation = []

    # 1. Schedule Sync (40 points) - Most important
    if profile1["schedule"] == profile2["schedule"]:
        score += 40
        explanation.append("✅ Great Lifestyle Sync: You are both " + profile1['schedule'].replace('_', ' ') + "s.")
    else:
        explanation.append("❌ Lifestyle Clash: One is an early bird, the other a night owl.")

    # 2. Cleanliness Vibe (30 points)
    if profile1["cleanliness"] == profile2["cleanliness"]:
        score += 30
        explanation.append("✅ Similar Cleanliness: You both prefer a " + profile1['cleanliness'] + " space.")
    else:
        explanation.append("⚠️ Different Views on Tidiness.")

    # 3. Social Energy (20 points)
    if profile1["social_style"] == profile2["social_style"]:
        score += 20
        explanation.append("✅ Social Harmony: You share a similar " + profile1['social_style'] + " approach.")
    
    # 4. The Vibe Boost (10 points) - Our secret sauce!
    if profile1["vibe"] == "positive" and profile2["vibe"] == "positive":
        score += 10
        explanation.append("✅ Positive Vibe Match: You both have a friendly and positive outlook!")

    return score, explanation

def find_best_match(new_user, residents_list):
    """Finds the best match for a new user from a list of residents."""
    best_score = -1
    best_match_profile = None
    best_match_explanation = []

    # Handle case where residents_list might be empty for a specific PG
    if not residents_list:
        return None, -1, []

    for resident in residents_list:
        score, explanation = calculate_match_score(new_user, resident)
        if score > best_score:
            best_score = score
            best_match_profile = resident
            best_match_explanation = explanation
            
    return best_match_profile, best_score, best_match_explanation