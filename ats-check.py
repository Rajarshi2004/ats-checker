import streamlit as st
import PyPDF2
import google.generativeai as genai

API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="ATS Resume Checker", page_icon="📄", layout="centered")

st.sidebar.title("👨‍💻 About Me")
st.sidebar.info(
    """
    Hi, I'm **Rajarshi Paul**, a CSE student passionate about  
    **AI, ML, and Full-Stack Projects** 🚀.  
    """
)
st.sidebar.markdown("### 🔗 Connect with Me")
st.sidebar.markdown("[🌐 LinkedIn](https://www.linkedin.com/in/your-profile)")
st.sidebar.markdown("[💻 GitHub](https://github.com/your-profile)")
st.sidebar.markdown("[📂 Other Project](https://mainpy-n3plcx755hrjwqkscxk2wi.streamlit.app/)")
st.sidebar.markdown("---")
st.sidebar.write("Made by Rajarshi Paul using Streamlit & Gemini AI")

st.title("📄 ATS Resume Checker")
st.write("Upload your resume and get an ATS-style analysis compared to job requirements.")

def file_upload(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def ask_gemini(file_text):
    prompt = f"""
    You are an ATS (Applicant Tracking System). Analyze the resume text below.
    Provide:
    1. ATS score out of 100
    2. List of matched keywords
    3. List of missing keywords
    4. 3 specific improvements to increase ATS score
    
    Resume:
    {file_text}
    """
    response = model.generate_content(prompt)
    return response.text if response.text else "⚠️ Gemini returned no answer."

uploaded_file = st.file_uploader("Upload Resume (PDF only)", type=["pdf"])

if uploaded_file:
    with st.spinner("Analyzing resume... ⏳"):
        resume_text = file_upload(uploaded_file)
        result = ask_gemini(resume_text)

    st.subheader("📊 ATS Analysis Result")
    st.markdown(result)




