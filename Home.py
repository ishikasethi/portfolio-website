import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Ishika Sethi")

    content = """Hi, I am Ishika, a software engineer. I have 1.5 years of experience in developing websites and applications. 
    I'm currently looking for a job opportunity and my primary objective to seek and maintain a full-time position that 
    offers professional challenges utilizing interpersonal skills, excellent time management, and problem-solving skills
    . Also, I'm organized and dependable at managing multiple priorities with a positive attitude.  
    \nIf my profile interests you, please do reach out to me at isethi721@gmail.com"""
    st.info(content)

content2 = """
Below you can find some of the basic apps I have built in Python. 
Feel feel to contact me!"""

st.write(content2)


col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

data = pandas.read_csv("data.csv", sep=';')

with col3:
    for index, row in data[:5].iterrows():
        st.header(row['title'])
        st.write(row["description"])
        st.image("images/" + row['image'], width=300)
        if row['url'] != "not available":
            st.write(f"[Visit App]({row['url']})")
        if row['download'] == "not available":
            continue
        else:
            st.write("This is a downloadable .exe file of this app.")
            with open(f"../portfolio-app/exe_files/{row['download']}", "rb") as fp:
                btn = st.download_button(
                    label="Download Application",
                    data=fp,
                    file_name=row['download'],
                    mime="application/zip"
                )
with col4:
    for index, row in data[5:].iterrows():
        st.header(row['title'])
        st.write(row["description"])
        st.image("images/" + row['image'])
        if row['url'] != "not available":
            st.write(f"[Visit App]({row['url']})")
        if row['download'] == "not available":
            continue
        else:
            st.write("This is a downloadable .exe file of this app.")
            with open(f"../portfolio-app/exe_files/{row['download']}", "rb") as fp:
                btn = st.download_button(
                    label="Download Application",
                    data=fp,
                    file_name=row['download'],
                    mime="application/zip"
                )
