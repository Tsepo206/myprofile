import streamlit as st
# Title of the app
st.title("Carrear Profile Page")
st.divider()
# Collect basic information
name = "Tsepo Sekhaosha"
field = "Astrophysics"
institution = "University of KwaZulu-Natal (UKZN)"

# Display basic profile information
st.header("Basic information")

col1, col2 = st.columns(2)

with col1:
   st.write(f"**Name:** {name}")
   st.write(f"**Field of Research:** {field}")
   st.write(f"**Institution:** {institution}") 

with col2:
    st.image("Tsepo_Pic.jpg", width=200, channels="RGB", output_format="auto")

# Add a section for publications
st.header("About Me")
st.write("It is a long established fact that a reader will be distracted by the \n readable content of a page when looking at its layout. The point of using \n Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).")
st.header("My Carrear CV")

st.image("TsepoCV.PNG", width=500, channels="RGB", output_format="auto")

# Add a contact section
st.header("Contact Information")
email = "tseposekhoasha@gmail.com"
contact = "0678055963"
st.write(f"You can reach {name} via email: {email} or on call at: {contact}")
