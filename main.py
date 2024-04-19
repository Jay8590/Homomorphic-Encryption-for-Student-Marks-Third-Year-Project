# Import necessary libraries
import mysql.connector  # Database library
import pandas as pd  # Data manipulation library
import streamlit as st  # GUI library
from streamlit_option_menu import option_menu  # GUI utility library
from sklearn.linear_model import LinearRegression  # Machine Learning library
import base64  # Encoding library
from paillier import Paillier  # Homomorphic encryption library
from phe import paillier  # Alternative homomorphic encryption library


db = mysql.connector.connect(
    host="localhost", user="root", password="7f61QW#lyFU8"
)
# Create a new database if it doesn't exist
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
print("Database created successfully")

# Connect to the new database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="7f61QW#lyFU8",
    database="mydatabase",
)

cursor = db.cursor()
print("Database Connected")

# Set page configuration
st.set_page_config(
    page_title="Homepage",
    page_icon="🔐",
)

# Instantiate the Paillier cryptosystem
p = Paillier()

# Generate public and private keys
public_key, private_key = paillier.generate_paillier_keypair()


# Define a function to encrypt a number using the public key
def encrypt_number(n, pk):
    return pk.encrypt(n)


# Define a function to decrypt a number using the private key
def decrypt_number(c, sk):
    return sk.decrypt(c)


# Define a function to encode a string as base64
def encode_string(s):
    return base64.b64encode(s.encode()).decode()


# Define a function to decode a string from base64
def decode_string(s):
    return base64.b64decode(s.encode()).decode()


def IT():
    with st.form(key="it"):
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS Encrypted (
                id INT AUTO_INCREMENT PRIMARY KEY,
                Name VARCHAR(255),
                `Roll no` VARCHAR(255),
                Course VARCHAR(255),
                `Sem/Year` VARCHAR(255),
                DMBI VARCHAR(255),
                `Web-X` VARCHAR(255),
                WT VARCHAR(255),
                AI VARCHAR(255),
                GIT VARCHAR(255),
                Total VARCHAR(255),
                Average VARCHAR(255),
                `Percentage %` VARCHAR(255)
            )"""
        )

        cursor.execute(
            """CREATE TABLE IF NOT EXISTS Decrypted (
                id INT AUTO_INCREMENT PRIMARY KEY,
                Name VARCHAR(255),
                `Roll no` VARCHAR(255),
                Course VARCHAR(255),
                `Sem/Year` VARCHAR(255),
                DMBI VARCHAR(255),
                `Web-X` VARCHAR(255),
                WT VARCHAR(255),
                AI VARCHAR(255),
                GIT VARCHAR(255),
                Total VARCHAR(255),
                Average VARCHAR(255),
                `Percentage %` VARCHAR(255)
            )"""
        )
        print("IT Tables created successfully")

        marks = []
        DMBI = st.number_input(
            f"Enter marks for Data Mining & Business Intelligence (DMBI)",
            min_value=1,
            max_value=100,
        )
        marks.append(DMBI)
        WebX = st.number_input(f"Enter marks for Web X.0", min_value=1, max_value=80)
        marks.append(WebX)
        WT = st.number_input(
            f"Enter marks for Wireless Technology (WT)", min_value=1, max_value=80
        )
        marks.append(WT)
        AI = st.number_input(
            f"Enter marks for Artificial Intelligence (AI)", min_value=1, max_value=80
        )
        marks.append(AI)
        GIT = st.number_input(
            f"Enter marks for Green IT (GIT)", min_value=1, max_value=80
        )
        marks.append(GIT)

        # st.write(DMBI, WebX, WT, AI, GIT)

        submit_marks = st.form_submit_button(label="Submit Marks")

        if submit_marks:
            return marks


def encrypt_String(name, course, sem_year):
    name_enc = name.encode("iso-8859-1")
    course_enc = course.encode("iso-8859-1")
    sem_year_enc = sem_year.encode("iso-8859-1")

    encoded_bytes_name = base64.b64encode(name_enc)
    encoded_string_name = encoded_bytes_name.decode("utf-8")
    encoded_bytes_course = base64.b64encode(course_enc)
    encoded_string_course = encoded_bytes_course.decode("utf-8")
    encoded_bytes_sem = base64.b64encode(sem_year_enc)
    encoded_string_sem = encoded_bytes_sem.decode("utf-8")

    return encoded_string_name, encoded_string_course, encoded_string_sem


def addition(c1, c2, c3, c4, c5):
    maximum_marks = encrypt_number(80, public_key)
    cipher_add = c1 + c2 + c3 + c4 + c5
    total_marks_obtained = cipher_add
    # st.write("Addition", cipher_add)
    # st.write(decrypt_number(cipher_add, private_key))

    cipher_average = (c1 + c2 + c3 + c4 + c5) / 5

    cipher_percentage = cipher_add / 400 * 100
    #print(str(decrypt_number(percentage, private_key)) + "%")
    return cipher_add, cipher_average, cipher_percentage


def number_homomorphic():
    # Input numbers from user
    with st.form(key="my_form"):
        n1 = st.number_input(
            "First number", min_value=1, max_value=1000, value=5, step=1
        )
        n2 = st.number_input(
            "Second number", min_value=1, max_value=1000, value=5, step=1
        )
        operation = st.selectbox("Select an operation:", ["Addition", "Subtraction"])
        submit_button = st.form_submit_button(label="Submit")

        if submit_button:
            c1 = encrypt_number(n1, public_key)
            c2 = encrypt_number(n2, public_key)
            first_number = encode_string(str(c1))
            second_number = encode_string(str(c2))
            if operation == "Addition":
                # Perform addition and display results
                add = n1 + n2
                cipher_add = c1 + c2
                X = [[n1, n2]]
                y = [n1 + n2]
                # Create and train the linear regression model
                model = LinearRegression()
                model.fit(X, y)
                decrypt_add = decrypt_number(cipher_add, private_key)
                # Display the results
                st.write(
                    f'<p style ="font-size: 20px;"><b>The result of addition is: <span style="color: green;">{add}</span>',
                    unsafe_allow_html=True,
                )
                st.write(
                    f'<p style ="font-size: 20px;"><b>Addition of the encrypted numbers is: <span style="color:green;">{encode_string(str(cipher_add))}</span>',
                    unsafe_allow_html=True,
                )
                st.write(
                    f'<p style ="font-size: 20px;"><b>Addition of the decrypted numbers is: <span style="color: '
                    f'green;">{decrypt_add}</span>',
                    unsafe_allow_html=True,
                )
                # Predict the result using the trained model
                prediction = model.predict(X)
                st.write(
                    f'<p style ="font-size: 20px;"><b>Predicted result: <span style="color: '
                    f'green;">{prediction[0]}</span>',
                    unsafe_allow_html=True,
                )

            elif operation == "Subtraction":
                # Perform subtraction and display results
                sub = n1 - n2
                cipher_sub = c1 - c2
                X = [[n1, -n2]]
                y = [n1 - n2]
                # Create and train the linear regression model
                model = LinearRegression()
                model.fit(X, y)
                decrypt_sub = decrypt_number(cipher_sub, private_key)
                # Display the results
                st.write(
                    f'<p style ="font-size: 20px;"><b>The result of Subtraction is: <span style="color: green;">{sub}</span>',
                    unsafe_allow_html=True,
                )
                st.write(
                    f'<p style ="font-size: 20px;"><b>Addition of the encrypted numbers is: <span style="color:green;">{encode_string(str(cipher_sub))}</span>',
                    unsafe_allow_html=True,
                )
                st.write(
                    f'<p style ="font-size: 20px;"><b>Addition of the decrypted numbers is: <span style="color: '
                    f'green;">{decrypt_sub}</span>',
                    unsafe_allow_html=True,
                )
                # Predict the result using the trained model
                prediction = model.predict(X)
                st.write(
                    f'<p style ="font-size: 20px;"><b>Predicted result: <span style="color: '
                    f'green;">{prediction[0]}</span>',
                    unsafe_allow_html=True,
                )

            else:
                st.error("Pls Select an Operation!")


def marks_homomorphic():
    name = st.text_input("Name")
    roll_no = st.number_input("Roll number", min_value=1, max_value=1000)
    course = st.selectbox(
        "Select Course",
        ("Information Technology (IT)", "Computer Science (CS) ", "Electronics"),
    )
    sem_year = st.selectbox("Select Sem/Year", ("Semester-1", "Semester-2"))

    # Switch statement based on course and semester
    if course == "Information Technology (IT)" and sem_year == "Semester-1":
        # Perform some action for IT Semester 1
        print("Performing action for IT Semester 1")
        marks_list = IT()
        string_enc = encrypt_String(name, course, sem_year)
        if marks_list is not None:
            c1 = encrypt_number(roll_no, public_key)
            c2 = encrypt_number(marks_list[0], public_key)
            c3 = encrypt_number(marks_list[1], public_key)
            c4 = encrypt_number(marks_list[2], public_key)
            c5 = encrypt_number(marks_list[3], public_key)
            c6 = encrypt_number(marks_list[4], public_key)

            enc_roll_no = encode_string(str(c1))
            enc_dmbi = encode_string(str(c2))
            enc_webx = encode_string(str(c3))
            enc_wt = encode_string(str(c4))
            enc_ai = encode_string(str(c5))
            enc_git = encode_string(str(c6))

            total, average, percentage = addition(c2, c3, c4, c5, c6)
            enc_total = encode_string(str(total))
            enc_average = encode_string(str(average))
            enc_percentage = encode_string(str(percentage))

            sql = "INSERT INTO Encrypted (Name, `Roll no`, Course, `Sem/Year`, DMBI, `Web-X`, WT, AI, GIT, Total, Average, `Percentage %`)  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (
                string_enc[0],
                enc_roll_no,
                string_enc[1],
                string_enc[2],
                enc_dmbi,
                enc_webx,
                enc_wt,
                enc_ai,
                enc_git,
                enc_total,
                enc_average,
                enc_percentage,
            )
            cursor.execute(sql, val)
            db.commit()
            st.error("Encrypted")
            query = "SELECT * FROM Encrypted"
            df = pd.read_sql(query, db)
            st.dataframe(df)

            sql = "INSERT INTO Decrypted (Name, `Roll no`, Course, `Sem/Year`, DMBI, `Web-X`, WT, AI, GIT, Total, Average, `Percentage %`)  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (
                name,
                roll_no,
                course,
                sem_year,
                marks_list[0],
                marks_list[1],
                marks_list[2],
                marks_list[3],
                marks_list[4],
                decrypt_number(total, private_key),
                decrypt_number(average, private_key),
                decrypt_number(percentage, private_key),
            )
            cursor.execute(sql, val)
            db.commit()
            st.info("Decrypted")
            query = "SELECT * FROM Decrypted"
            df = pd.read_sql(query, db)
            st.dataframe(df)



    elif course == "Computer Science (CS)" and sem_year == "Semester-1":
        # Perform some action for CS Semester 1
        print("Performing action for CS Semester 1")
    elif course == "Electronics" and sem_year == "Semester-1":
        # Perform some action for Electronics Semester 1
        print("Performing action for Electronics Semester 1")
    else:
        # Handle invalid input
        print("Invalid input")


if __name__ == "__main__":

    # Set page title and header
    st.write(
        "<p style='font-size: 36px; font-family: Ethnocentric Rg; text-align:center;'> Implementation of various <br>"
        "Encryption technique 🔐</p>",
        unsafe_allow_html=True,
    )
    # Add horizontal line
    st.write(
        f'<hr style="background-color: red; margin-top: 0;'
        ' margin-bottom: 0; height: 3px; border: none; border-radius: 3px;">',
        unsafe_allow_html=True,
    )
    # Create option menu with icons
    selected = option_menu(
        menu_title=None,
        options=["Home", "Homomorphic", "Triple DES", "AES"],
        icons=["house", None, "file-lock", "lock"],
        default_index=0,
        orientation="horizontal",
    )
    # Handle menu item selection
    if selected == "Home":
        print(selected)
    elif selected == "Homomorphic":
        print(selected)
        homo_select = st.selectbox("Select", ("Number", "Students Marks"))
        if homo_select == "Number":
            print(homo_select)
            number_homomorphic()
        elif homo_select == "Students Marks":
            print(homo_select)
            marks_homomorphic()
    elif selected == "Triple DES":
        print(selected)
    elif selected == "AES":
        print(selected)
