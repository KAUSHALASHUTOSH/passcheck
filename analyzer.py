import re

def analyze_password(password):
    score = 0

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"[0-9]", password):
        score += 1

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if re.search(r"(.)\1{2,}", password):
        score -= 1

    if "password" in password.lower():
        score -= 2

    if len(set(password)) <= 4:
        score -= 1

    if score <= 1:
        verdict = "Very Weak"
    elif score == 2:
        verdict = "Weak"
    elif score == 3:
        verdict = "Moderate"
    elif score == 4:
        verdict = "Strong"
    else:
        verdict = "Very Strong"

    return verdict, score

def generate_suggestions(password):
    suggestions = []

    if len(password) < 12:
        suggestions.append("Make it at least 12 characters.")
    if not re.search(r"[A-Z]", password):
        suggestions.append("Add uppercase letters.")
    if not re.search(r"[a-z]", password):
        suggestions.append("Include lowercase letters.")
    if not re.search(r"[0-9]", password):
        suggestions.append("Include numbers.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        suggestions.append("Add special characters (!@# etc).")
    if "password" in password.lower():
        suggestions.append("Avoid using common words like 'password'.")
    if len(set(password)) <= 4:
        suggestions.append("Use a mix of unique characters.")

    suggestions.append("Update passwords every few months.")
    suggestions.append("Avoid repeating characters too much.")
    suggestions.append("Try passphrases like: 'Blue$Fish@Sun12'.")

    return suggestions
