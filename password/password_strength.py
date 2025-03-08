import streamlit as st
import re

def check_password_strength(password):
    # Initialize score and feedback
    score = 0
    feedback = []
    
    # Check length
    if len(password) < 8:
        feedback.append("❌ Password should be at least 8 characters long")
    else:
        score += 1
        feedback.append("✅ Good length")
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
        feedback.append("✅ Contains uppercase letters")
    else:
        feedback.append("❌ Should contain uppercase letters")
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
        feedback.append("✅ Contains lowercase letters")
    else:
        feedback.append("❌ Should contain lowercase letters")
    
    # Check for numbers
    if re.search(r'\d', password):
        score += 1
        feedback.append("✅ Contains numbers")
    else:
        feedback.append("❌ Should contain numbers")
    
    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
        feedback.append("✅ Contains special characters")
    else:
        feedback.append("❌ Should contain special characters")
    
    return score, feedback

def main():
    st.title("🔐 Password Strength Checker")
    st.write("Check how strong your password is! 🔍 ")
    
    # Password input
    password = st.text_input("Enter your password", type="password")
    
    if password:
        score, feedback = check_password_strength(password)
        
        # Display strength score
        strength_text = {
            0: "Very Weak",
            1: "Weak",
            2: "Moderate",
            3: "Strong",
            4: "Very Strong",
            5: "Excellent"
        }
        
        # Create a progress bar for visual feedback
        st.progress(score / 5)
        st.write(f"Strength: {strength_text[score]}")
        
        # Display color-coded strength
        if score < 2:
            st.error(strength_text[score])
        elif score < 4:
            st.warning(strength_text[score])
        else:
            st.success(strength_text[score])
        
        # Display feedback
        st.write("### Password Criteria:")
        for item in feedback:
            st.write(item)
        
        # Security note
        st.info("Note: Never share your password with anyone!")

if __name__ == "__main__":
    main() 