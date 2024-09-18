Homomorphic Encryption for Student Marks - Third Year Project

This project implements a system that uses Paillier Homomorphic Encryption to encrypt student marks, allowing for secure computations (such as addition) on encrypted data without decryption. The project is built with Streamlit to provide an interactive web interface, demonstrating the application of cryptography in educational data systems.
Table of Contents

    Introduction
    Features
    Technologies Used
    Installation
    Usage
    How Paillier Homomorphic Encryption Works
    Project Structure
    Contributing
    License

Introduction

This project is a third-year academic assignment that demonstrates how to secure student marks using Paillier Homomorphic Encryption. It ensures privacy by allowing operations on encrypted marks without needing to decrypt them. The system provides a user-friendly interface via Streamlit, allowing users to interact with the encryption system seamlessly.
Objectives:

    Securely encrypt student marks using Paillier Homomorphic Encryption.
    Perform addition on encrypted marks without decryption.
    Allow authorized personnel to decrypt and view the original marks.

Features

    Encryption: Secure student marks using Paillier encryption.
    Homomorphic Operations: Perform addition on encrypted marks without decrypting them.
    Decryption: Decrypt the marks to view the original values or computed results via the web interface.
    Streamlit Web Interface: Provides a simple UI for encrypting, operating on, and decrypting student marks.

Technologies Used

    Python: Main programming language used.
    Libraries:
        Streamlit: For creating an interactive web interface.
        Paillier Cryptosystem: Implements Paillier Homomorphic Encryption.
        Other libraries listed in the requirements.txt file.

Installation

    Clone the repository:

    bash

git clone https://github.com/Jay8590/Homomorphic-Encryption-for-Student-Marks-Third-Year-Project.git
cd Homomorphic-Encryption-for-Student-Marks-Third-Year-Project

Install dependencies: Ensure Python is installed, and then install the required libraries by running:

bash

pip install -r requirements.txt

Run the Streamlit app: After installing the dependencies, run the project using Streamlit:

bash

streamlit run main.py

Access the app: After running the above command, Streamlit will open the app in your default browser, where you can interact with the encryption system.
