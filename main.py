import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="AI Consultant - Abdullah Khan",
    page_icon=":robot_face:",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {background-color: #f0f2f6; padding-top: 1rem;}
    .stSidebar {background-color: #f0f0f0; color: white;}
    .st-sidebar .element-container { color: white; }
    .stSidebar > div { color: white; }
    .big-font {font-size:30px !important; font-weight: bold; color: #203864;}
    .section-title {font-size:24px; font-weight: bold; margin-top: 1rem; color: #1f77b4;}
    .testimonial {font-style: italic; color: #555; margin-bottom: 1rem;}
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar Navigation
st.sidebar.title("Navigation")
nav = st.sidebar.radio("", ["Home", "About Me", "Services", "Portfolio", "Testimonials", "Contact"])

# Home Section
if nav == "Home":
    st.markdown('<p class="big-font">Welcome to My AI Consultancy!</p>', unsafe_allow_html=True)
    st.write("Hello! I'm Abdullah Khan, an experienced AI Consultant specializing in providing AI-driven solutions to transform your business or research.")

    image = Image.open('your_image_path.jpg')  # Replace with your image path
    st.image(image, caption='Your Name', use_column_width=True)

    st.write("""
    As an AI Consultant, I help organizations and individuals leverage artificial intelligence to achieve their goals. From machine learning model development to AI strategy formulation, I offer comprehensive AI consultancy services to meet your specific needs.
    """)

# About Me Section
elif nav == "About Me":
    st.markdown('<p class="section-title">About Me</p>', unsafe_allow_html=True)
    st.write("""
    With a background in Artificial Intelligence and years of experience working in multiple companies in Artificial Intelligence, I've helped numerous organizations integrate AI technologies into their operations. My expertise spans across machine learning, deep learning, natural language processing, and AI strategy.
    """)

    # Collapsible section for detailed background
    with st.expander("Read more about my background"):
        st.write("""
        I started my journey in AI by Bachelor of Science in Artificial Intelligence from Ghulam Ishaq Khan Institute of Engineering Sciences and Technology, then I became Research Artificial Intelligence Engineer at Agile Loop. Over the years, I have worked with several top companies and startups, helping them harness the power of AI to solve complex problems and drive innovation.
        """)

# Services Section
elif nav == "Services":
    st.markdown('<p class="section-title">Services</p>', unsafe_allow_html=True)
    st.write("I offer a range of AI consultancy services to help you succeed in your AI journey:")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("AI Strategy Development")
        st.write("Helping organizations formulate a robust AI strategy that aligns with their business goals.")

        st.subheader("Machine Learning Solutions")
        st.write("Developing custom machine learning models tailored to solve specific business challenges.")

    with col2:
        st.subheader("Natural Language Processing")
        st.write("Implementing NLP solutions for text analysis, chatbots, sentiment analysis, and more.")

        st.subheader("AI Training & Workshops")
        st.write("Providing hands-on training sessions and workshops on AI and machine learning for your teams.")

# Portfolio Section
elif nav == "Portfolio":
    st.markdown('<p class="section-title">Portfolio</p>', unsafe_allow_html=True)
    st.write("Explore some of the AI projects I have worked on:")

    st.subheader("Client Projects")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.image("project_image1.jpg", caption="AI-driven E-commerce Personalization", use_column_width=True)
        st.write("Developed an AI model that improved product recommendations and increased conversion rates by 20%.")
    
    with col2:
        st.image("project_image2.jpg", caption="Healthcare Predictive Analytics", use_column_width=True)
        st.write("Implemented predictive analytics solutions for patient readmission and personalized treatment plans.")

    st.subheader("Research and Open Source Contributions")
    st.write("""
    - **AI Ethics Research**: Published a paper on ethical considerations in AI model deployment.
    - **Open Source NLP Tool**: Developed an open-source tool for natural language processing tasks, widely adopted in the community.
    """)

# Testimonials Section
elif nav == "Testimonials":
    st.markdown('<p class="section-title">Testimonials</p>', unsafe_allow_html=True)
    st.write("""
    Hear from some of my clients and colleagues:
    """)

    st.markdown('<p class="testimonial">"An exceptional AI consultant who helped us streamline our operations using advanced AI techniques. Highly recommend!" - Client A</p>', unsafe_allow_html=True)
    st.markdown('<p class="testimonial">"Transformed our data analytics strategy with custom AI models. A great professional to work with!" - Client B</p>', unsafe_allow_html=True)

# Contact Section
elif nav == "Contact":
    st.markdown('<p class="section-title">Contact Me</p>', unsafe_allow_html=True)
    st.write("I'd love to hear from you! Fill out the form below to get in touch:")

    contact_form = """
    <form action="https://formsubmit.co/your-email@example.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <input type="text" name="subject" placeholder="Subject" required>
        <textarea name="message" placeholder="Your Message" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

# Footer
st.write("---")
st.markdown("© 2024 Your Name. All rights reserved. | Connect with me on [LinkedIn](https://www.linkedin.com/) | [Twitter](https://twitter.com/) | [GitHub](https://github.com/)", unsafe_allow_html=True)
