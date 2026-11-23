# UI
import streamlit as st
from models import gemini


# st.title(':red[Gemini] :blue[LLM] :orange[Project]:8ball:')

# st.header('Model: 3.8-Flash')

# st.subheader('Project Project')

st.title('GEMINI LLM PROJECT')
st.header('Using 3.8-Flash Model')

prompt = st.text_area(
    'Where should we begin?',
    placeholder='Eg: What is relativity of gravity?'
    )

if st.button("Search", type="secondary"):
    if prompt.strip() == "":
        st.toast(":red[Input field cannot be empty.]", duration="long")
    else:
        with st.spinner("Generating content..."):
           answer = gemini(prompt)
        st.success("Content Generated successfully.")
        st.write(answer)
        