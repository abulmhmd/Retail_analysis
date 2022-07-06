import streamlit as st
import pandas as pd
import sqlite3
import hashlib
import subprocess
from pathlib import Path




# Security
# passlib,hashlib,bcrypt,scrypt


def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()


def check_hashes(password, hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False


# DB Management


conn = sqlite3.connect('data.db')
c = conn.cursor()


# DB  Functions
def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username, password):
    c.execute('INSERT INTO userstable(username,password) VALUES (?,?)', (username, password))
    conn.commit()


def login_user(username, password):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?', (username, password))
    data = c.fetchall()
    return data


def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data


def main():

    st.title("RETAIL MANAGEMENT")

    menu = ["Home", "Login", "SignUp"]
    choice = st.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("welcome !!..")

        def read_markdown_file(markdown_file):
            return Path(markdown_file).read_text()

        intro_markdown = read_markdown_file("home.md")
        st.markdown(intro_markdown, unsafe_allow_html=True)

    elif choice == "Login":
        st.subheader("Login Section")

        username = st.text_input("User Name")
        password = st.text_input("Password", type='password')
        if st.checkbox("Login"):
            # if password == '12345':
            create_usertable()
            hashed_pswd = make_hashes(password)

            result = login_user(username, check_hashes(password, hashed_pswd))
            if result:

                st.success("Logged In as {}".format(username))
                op = ["None", "Analysis", "Profiles"]
                task = st.selectbox("Task", op)
                if task == "None":
                    st.write("Please select anyone from the list")

                elif task == "Analysis":
                    st.subheader("Analysis")
                    ch = ["None", "EDA AND Data Visualization", "Time series", "Machine Learning"]
                    connect = st.selectbox("select the analysis", ch)
                    if connect == "Time series":
                        subprocess.Popen(["streamlit", "run", "time_series.py"])
                    elif connect == "EDA AND Data Visualization":
                        subprocess.Popen(["streamlit", "run", "analysis.py"])
                    elif connect == "Machine Learning":
                        subprocess.Popen(["streamlit", "run", "apriori_algo.py"])
                    else:

                        st.info("Please select any Analysis")

                elif task == "Profiles":
                    st.subheader("User Profiles")
                    user_result = view_all_users()
                    clean_db = pd.DataFrame(user_result, columns=["Username", "Password"])
                    st.dataframe(clean_db)
            else:
                st.warning("Incorrect Username/Password")


    elif choice == "SignUp":
        st.title("Registration Form")

        col1, col2 = st.beta_columns(2)

        col1.text_input("First Name")

        col2.text_input("Second Name")

        col3, col4 = st.beta_columns([3, 1])

        col3.text_input("Email ID")

        col4.text_input("Mobile number")

        col5, col6 = st.beta_columns(2)

        new_user = col5.text_input("Username")

        new_password = col6.text_input("Password", type="password")

        but1, but2, but3 = st.beta_columns([1, 4, 1])

        agree = but1.checkbox("I Agree")

        if but3.button("Submit"):
            create_usertable()
            add_userdata(new_user, make_hashes(new_password))
            if agree:
                st.success("Done")
                st.info("Go to Login Menu to login")
            else:
                st.warning("Please Check the T&C box")



if __name__ == '__main__':
    main()
