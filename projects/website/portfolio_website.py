import streamlit as st
import base64

def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://images.unsplash.com/photo-1557683316-973673baf926?ixlib=rb-4.0.3");
            background-attachment: fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def main():
    # Page configuration
    st.set_page_config(
        page_title="My Portfolio",
        page_icon="👨‍💻",
        layout="wide"
    )

    # Add background
    add_bg_from_url()

    # Custom CSS
    st.markdown("""
        <style>
        .main {
            padding: 2rem;
        }
        .title-text {
            font-size: 3rem;
            font-weight: bold;
            color: #ffffff;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }
        .section-header {
            font-size: 2rem;
            color: #ffffff;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
        }
        .content-box {
            background-color: rgba(255, 255, 255, 0.9);
            padding: 2rem;
            border-radius: 10px;
            margin: 1rem 0;
        }
        </style>
    """, unsafe_allow_html=True)

    # Navigation
    st.markdown("""
        <div style="text-align: center; padding: 1rem;">
            <a href="#about" style="margin: 0 1rem; color: white; text-decoration: none;">About</a>
            <a href="#projects" style="margin: 0 1rem; color: white; text-decoration: none;">Projects</a>
            <a href="#skills" style="margin: 0 1rem; color: white; text-decoration: none;">Skills</a>
            <a href="#contact" style="margin: 0 1rem; color: white; text-decoration: none;">Contact</a>
        </div>
    """, unsafe_allow_html=True)

    # Hero Section
    st.markdown('<h1 class="title-text">Welcome to My Portfolio</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color: white; font-size: 1.2rem;">Python Developer | Data Scientist | Web Developer</p>', unsafe_allow_html=True)

    # About Section
    st.markdown('<h2 id="about" class="section-header">About Me</h2>', unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.write("""
            I am a passionate Python developer with expertise in web development, data science, and machine learning.
            I love creating elegant solutions to complex problems and am always eager to learn new technologies.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    # Projects Section
    st.markdown('<h2 id="projects" class="section-header">Projects</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.subheader("BMI Calculator")
        st.write("A web application that calculates Body Mass Index and provides health recommendations.")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.subheader("Password Generator")
        st.write("A secure password generator with customizable options for different security levels.")
        st.markdown('</div>', unsafe_allow_html=True)

    # Skills Section
    st.markdown('<h2 id="skills" class="section-header">Skills</h2>', unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
                **Programming Languages**
                - Python
                - JavaScript
                - HTML/CSS
            """)
        
        with col2:
            st.markdown("""
                **Frameworks & Libraries**
                - Streamlit
                - Flask
                - Pandas
                - NumPy
            """)
        
        with col3:
            st.markdown("""
                **Tools & Technologies**
                - Git
                - Docker
                - AWS
                - SQL
            """)
        st.markdown('</div>', unsafe_allow_html=True)

    # Contact Section
    st.markdown('<h2 id="contact" class="section-header">Contact Me</h2>', unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
                **Email:** example@email.com
                **Phone:** +1 234 567 890
                **Location:** New York, USA
            """)
        
        with col2:
            st.markdown("""
                **Social Media:**
                - [LinkedIn](https://linkedin.com)
                - [GitHub](https://github.com)
                - [Twitter](https://twitter.com)
            """)
        st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown("""
        <div style="text-align: center; padding: 2rem; color: white;">
            <p>© 2024 My Portfolio. All rights reserved.</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 