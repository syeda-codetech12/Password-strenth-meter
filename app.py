import streamlit as st
import re
import time
from typing import Dict, List, Tuple

# Set page config
st.set_page_config(
    page_title="Password Strength Meter",
    page_icon="🔒",
    layout="wide"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .stTextInput > div > div > input {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 10px;
        color: #1f1f1f !important;
    }
    .stProgress > div > div > div > div {
        background-color: #ff4b4b;
    }
    .stMarkdown {
        font-family: 'Segoe UI', sans-serif;
    }
    .main {
        background-color: #ffffff;
    }
    input[type="password"] {
        color: #1f1f1f !important;
    }
    </style>
    """, unsafe_allow_html=True)

def check_password_strength(password: str) -> Tuple[int, Dict[str, bool], List[str]]:
    """
    Check password strength and return score, criteria met, and feedback
    """
    score = 0
    feedback = []
    criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r'[A-Z]', password)),
        "lowercase": bool(re.search(r'[a-z]', password)),
        "numbers": bool(re.search(r'\d', password)),
        "special": bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)),
        "no_spaces": ' ' not in password,
        "no_common": password.lower() not in ['password', '123456', 'qwerty', 'admin']
    }
    
    # Calculate score
    score += 2 if criteria["length"] else 0
    score += 2 if criteria["uppercase"] else 0
    score += 2 if criteria["lowercase"] else 0
    score += 2 if criteria["numbers"] else 0
    score += 2 if criteria["special"] else 0
    score += 1 if criteria["no_spaces"] else 0
    score += 1 if criteria["no_common"] else 0
    
    # Generate feedback
    if not criteria["length"]:
        feedback.append("Password should be at least 8 characters long")
    if not criteria["uppercase"]:
        feedback.append("Add uppercase letters")
    if not criteria["lowercase"]:
        feedback.append("Add lowercase letters")
    if not criteria["numbers"]:
        feedback.append("Add numbers")
    if not criteria["special"]:
        feedback.append("Add special characters")
    if not criteria["no_spaces"]:
        feedback.append("Remove spaces")
    if not criteria["no_common"]:
        feedback.append("Avoid common passwords")
    
    return score, criteria, feedback

def get_strength_color(score: int) -> str:
    """Return color based on password strength"""
    if score <= 4:
        return "#ff4b4b"  # Red
    elif score <= 8:
        return "#ffa726"  # Orange
    elif score <= 12:
        return "#66bb6a"  # Green
    else:
        return "#42a5f5"  # Blue

def main():
    # Header
    st.title("🔒 Password Strength Meter")
    st.markdown("""
        <div style='background-color: #f0f2f6; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
            <h3 style='color: #1f1f1f;'>Check your password strength in real-time!</h3>
            <p style='color: #666666;'>Enter your password below to see how strong it is.</p>
        </div>
    """, unsafe_allow_html=True)

    # Password input
    password = st.text_input("Enter your password:", type="password", key="password_input")
    
    if password:
        # Calculate strength
        score, criteria, feedback = check_password_strength(password)
        
        # Display strength bar with correct proportion
        st.markdown("### Password Strength")
        strength_bar = st.progress(0)
        progress_percentage = score / 12  # Calculate percentage of max score (12)
        for i in range(int(progress_percentage * 100)):
            time.sleep(0.01)
            strength_bar.progress(i / 100)
        
        # Display score and color
        color = get_strength_color(score)
        st.markdown(f"""
            <div style='background-color: {color}; color: white; padding: 10px; border-radius: 5px; text-align: center; margin: 10px 0;'>
                <h3 style='margin: 0;'>Strength Score: {score}/12</h3>
            </div>
        """, unsafe_allow_html=True)
        
        # Display criteria
        st.markdown("### Password Criteria")
        col1, col2 = st.columns(2)
        
        with col1:
            for criterion, met in list(criteria.items())[:4]:
                status = "✅" if met else "❌"
                st.markdown(f"{status} {criterion.replace('_', ' ').title()}")
        
        with col2:
            for criterion, met in list(criteria.items())[4:]:
                status = "✅" if met else "❌"
                st.markdown(f"{status} {criterion.replace('_', ' ').title()}")
        
        # Display feedback
        if feedback:
            st.markdown("### Suggestions for Improvement")
            for suggestion in feedback:
                st.markdown(f"- {suggestion}")
        
        # Final verdict
        verdict = ""
        if score <= 4:
            verdict = "Weak - Please strengthen your password"
        elif score <= 8:
            verdict = "Moderate - Could be stronger"
        elif score <= 12:
            verdict = "Strong - Good job!"
        else:
            verdict = "Very Strong - Excellent password!"
            
        st.markdown(f"""
            <div style='background-color: #f8f9fa; padding: 15px; border-radius: 5px; margin-top: 20px;'>
                <h3 style='color: {color}; margin: 0;'>{verdict}</h3>
            </div>
        """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
        <div style='position: fixed; bottom: 0; width: 100%; background-color: #f0f2f6; padding: 10px; text-align: center;'>
            <p style='margin: 0; color: #666666;'>🔒 Secure Password Generator | Made with ❤️</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 
