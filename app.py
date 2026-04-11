# import streamlit as st
# import time

# # -------------------------------
# # Page Config
# # -------------------------------
# st.set_page_config(page_title="Graphic Era Smart Chatbot", page_icon="🎓", layout="wide")

# # -------------------------------
# # Custom CSS
# # -------------------------------
# st.markdown("""
# <style>
# .stApp {
#     background: linear-gradient(135deg, #0f172a, #1e293b);
#     color: white;
# }

# h1 {
#     text-align: center;
#     color: #4CAF50;
# }

# [data-testid="stChatMessage"] {
#     border-radius: 15px;
#     padding: 12px;
#     margin: 8px;
#     background-color: #1e293b;
# }

# section[data-testid="stSidebar"] {
#     background-color: #020617;
# }
# </style>
# """, unsafe_allow_html=True)

# # -------------------------------
# # Header
# # -------------------------------
# st.markdown("""
# <h1>🎓 Graphic Era Smart Assistant</h1>
# <p style='text-align:center;'>Your 24/7 College Help Partner 🤖</p>
# """, unsafe_allow_html=True)

# # -------------------------------
# # Welcome Message (only once)
# # -------------------------------
# if "welcome_shown" not in st.session_state:
#     st.session_state.welcome_shown = True
#     st.info("👋 Welcome! Ask me anything about Graphic Era University.")

# # -------------------------------
# # Data
# -------------------------------
# college_data = {
#     "about": """LOCATION" : Dehadun , uttrakhand \n
#      ESTABLISHED: 1997 \n
#      Founder: Prof.(Dr.)Kamal Ghanshala \n
#      Type: Private Deemed University \n
#      Accreditation: NAAC A+ Grade \n
#      Approved by: UGC, AICTE""",
    
#     "courses": "B.Tech, BCA, MBA, BBA, B.Com, MCA TOTAL 100+ course (UG + PG + PHD + Diploma)" ,
#     "fees": "B.Tech: ₹2.5–3.5 LPA \n BCA: ₹1.2–1.5 LPA PER YEAR",
#     "placement": "Highest: ₹65+ LPA  Avg: ₹5–8 LPA",
   
#     "hostel": """Name:\n
#     CHANDRA SHEKHER AZAD\n  
#     SARDAR PATEL HOSTEL\n  
#     NETAJI SUBHASH CHANDRA HOSTEL\n
#     SAI HOSTEL  \n
#     "hostel fees ": 160000 These fees may vary for different hostels """, 

#      "
#     # "mayank": "hello",
    
   
#     "faculty":"""Name: priyansh kumar \n
#                        mohit amoli 
#                        mayank
#     "600+ Faculty | PhD Holders"""
    
   
# }

# # -------------------------------
# # Sidebar
# # -------------------------------
# st.sidebar.title("📌 Quick Menu")
# option = st.sidebar.selectbox(
#     "Select Option",
#     ["Chat Mode", "About", "Courses", "Fees", "Placement", "Hostel", "Faculty"]
# )

# if st.sidebar.button("🗑 Clear Chat"):
#     st.session_state.messages = []
#     st.rerun()

# # -------------------------------
# # Session
# # -------------------------------
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # -------------------------------
# # Sidebar Output
# # -------------------------------
# if option != "Chat Mode":
#     st.success(college_data[option.lower()])

# # -------------------------------
# # Chat Input
# # -------------------------------
# user_input = st.chat_input("Ask something...")

# # -------------------------------
# # Chatbot Logic
# # -------------------------------
# def get_response(user_input):
#     user_input = user_input.lower()

#     if "fee" in user_input:
#         return college_data["fees"]
#     elif "course" in user_input:
#         return college_data["courses"]
#      # elif "mayank" in user_input:
#      #    return college_data["mayank"]
#     elif "hostel " in user_input:
#         return college_data["hostel "]
#     elif "hostel fees" in user_input:
#         return college_data["hostel fees"]
#     elif "placement" in user_input:
#         return college_data["placement"]
#     elif "faculty" in user_input:
#         return college_data["faculty"]
#     elif "about" in user_input or "college" in user_input:
#         return college_data["about"]
#     elif "hi" in user_input or "hello" in user_input or "namste bhai jii" in user_input:
#         return "AA GYA GANDU HIIIIIIIIII KESA LGA MERA MAJAK "
#     else:
#         return "❗  ARE BHOSDIKE IN QUESTION ME SE KUCH PUCH NA KYU APNI GAND MRA RAHA HAI BHOSDII Try asking about fees, courses, placement, hostel."

# # -------------------------------
# # Show old messages
# # -------------------------------
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(msg["content"])

# # -------------------------------
# # Typing Effect Function
# # -------------------------------
# def type_effect(text):
#     placeholder = st.empty()
#     typed = ""
#     for char in text:
#         typed += char
#         placeholder.markdown(typed)
#         time.sleep(0.01)

# # -------------------------------
# # New Message
# # -------------------------------
# if user_input:
#     st.session_state.messages.append({"role": "user", "content": user_input})

#     with st.chat_message("user"):
#         st.markdown(user_input)

#     response = get_response(user_input)

#     st.session_state.messages.append({"role": "assistant", "content": response})

#     with st.chat_message("assistant"):
#         type_effect(response)


import streamlit as st
import time

# Page Config
st.set_page_config(page_title="Graphic Era Smart Chatbot", page_icon="🎓", layout="wide")

# Header
st.title("🎓 Graphic Era Smart Assistant")
st.write("Your 24/7 College Help Partner 🤖")

# Data (FIXED)
college_data = {
    "about": {
        "established": 1997,
        "location": "Dehradun, Uttarakhand",
        "founder": "Prof. (Dr.) Kamal Ghanshala",
        "type": "Private Deemed University",
        "accreditation": "NAAC A+ Grade",
        "approved_by": "UGC, AICTE"
    },

    "courses": "B.Tech, BCA, MBA, BBA, B.Com, MCA (100+ Courses)",
    
    "fees": {
        "B.Tech": "₹2.5–3.5 LPA",
        "BCA": "₹1.2–1.5 LPA per year"
    },

    "placement": "Highest: ₹65+ LPA | Average: ₹5–8 LPA",

    "hostel": {
        "names": [
            "Chandra Shekhar Azad Hostel",
            "Sardar Patel Hostel",
            "Netaji Subhash Chandra Hostel",
            "Sai Hostel"
        ],
        "fees": "₹160000 (approx)"
    },

    "faculty": "600+ Faculty | PhD Holders"
}

# Sidebar
st.sidebar.title("📌 Quick Menu")
option = st.sidebar.selectbox(
    "Select Option",
    ["Chat Mode", "About", "Courses", "Fees", "Placement", "Hostel", "Faculty"]
)

# Sidebar Output
if option != "Chat Mode":
    st.write(college_data[option.lower()])

# Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Ask something...")

# Chatbot Logic
def get_response(user_input):
    user_input = user_input.lower()

    if "fee" in user_input:
        return str(college_data["fees"])
    elif "course" in user_input:
        return college_data["courses"]
    elif "hostel" in user_input:
        return str(college_data["hostel"])
    elif "placement" in user_input:
        return college_data["placement"]
    elif "faculty" in user_input:
        return college_data["faculty"]
    elif "about" in user_input or "college" in user_input:
        return str(college_data["about"])
    elif "hi" in user_input or "hello" in user_input:
        return "Hello! 👋 How can I help you?"
    else:
        return "❗ Please ask about fees, courses, placement, hostel, or faculty."

# Show Messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Typing Effect
def type_effect(text):
    placeholder = st.empty()
    typed = ""
    for char in text:
        typed += char
        placeholder.markdown(typed)
        time.sleep(0.01)

# New Message
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    response = get_response(user_input)

    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        type_effect(response)
