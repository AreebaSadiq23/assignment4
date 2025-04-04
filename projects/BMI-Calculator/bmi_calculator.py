import streamlit as st
import math

def calculate_bmi(weight, height):
    # Convert height from cm to meters
    height_m = height / 100
    # Calculate BMI
    bmi = weight / (height_m * height_m)
    return round(bmi, 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight", "You should consider gaining some weight."
    elif 18.5 <= bmi < 25:
        return "Normal weight", "Keep maintaining your healthy lifestyle!"
    elif 25 <= bmi < 30:
        return "Overweight", "Consider reducing your calorie intake and increasing physical activity."
    else:
        return "Obese", "Please consult a healthcare provider for personalized advice."

def main():
    # Set page config
    st.set_page_config(
        page_title="BMI Calculator",
        page_icon="⚖️",
        layout="centered"
    )

    # Add custom CSS
    st.markdown("""
        <style>
        .main {
            padding: 2rem;
        }
        .stButton>button {
            width: 100%;
            background-color: #4CAF50;
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 5px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        </style>
    """, unsafe_allow_html=True)

    # Title and description
    st.title("⚖️ BMI Calculator")
    st.markdown("""
        Calculate your Body Mass Index (BMI) to assess your body weight relative to your height.
        This calculator is for adults (20 years and older).
    """)

    # Create two columns for input
    col1, col2 = st.columns(2)

    with col1:
        weight = st.number_input(
            "Weight (kg)",
            min_value=20.0,
            max_value=300.0,
            value=70.0,
            step=0.1
        )

    with col2:
        height = st.number_input(
            "Height (cm)",
            min_value=100.0,
            max_value=250.0,
            value=170.0,
            step=0.1
        )

    # Calculate button
    if st.button("Calculate BMI"):
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        category, advice = get_bmi_category(bmi)

        # Display results
        st.markdown("---")
        st.markdown("### Results")
        
        # Create three columns for results
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("BMI", f"{bmi}")
        
        with col2:
            st.metric("Category", category)
        
        with col3:
            st.metric("Status", "⚠️" if category in ["Underweight", "Overweight", "Obese"] else "✅")

        # Display advice
        st.info(advice)

        # Add BMI scale visualization
        st.markdown("### BMI Scale")
        st.markdown("""
            <div style="background-color: #f0f0f0; padding: 10px; border-radius: 5px;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                    <span>Underweight</span>
                    <span>Normal</span>
                    <span>Overweight</span>
                    <span>Obese</span>
                </div>
                <div style="background: linear-gradient(to right, #3498db, #2ecc71, #f1c40f, #e74c3c); 
                            height: 20px; border-radius: 10px;"></div>
                <div style="display: flex; justify-content: space-between; margin-top: 5px;">
                    <span>&lt;18.5</span>
                    <span>18.5-24.9</span>
                    <span>25-29.9</span>
                    <span>≥30</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

    # Add footer
    st.markdown("---")
    st.markdown("""
        <div style="text-align: center; color: #666;">
            <p>Note: This calculator is for informational purposes only. 
            Please consult a healthcare provider for medical advice.</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 