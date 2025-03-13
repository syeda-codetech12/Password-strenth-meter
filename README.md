# 🔒 Password Strength Meter

A modern, user-friendly password strength meter built with Streamlit that provides real-time feedback on password strength and suggestions for improvement.

## Features

- Real-time password strength evaluation
- Visual strength indicator with progress bar
- Detailed criteria checking
- Specific improvement suggestions
- Modern and responsive UI
- Secure password input (hidden characters)

## Password Strength Criteria

The meter evaluates passwords based on the following criteria:
- Minimum length (8 characters)
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters
- No spaces
- Not a common password

## Installation

1. Clone this repository
2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

Run the application using:
```bash
streamlit run app.py
```

The application will open in your default web browser. Enter your password in the input field to see:
- A visual strength indicator
- Your password's strength score
- Which criteria your password meets
- Specific suggestions for improvement
- A final verdict on your password's strength

## Security Note

This application runs locally on your machine and does not store or transmit any passwords. All password evaluation is done in real-time on your local device.

## Made with ❤️

Built using Python and Streamlit for a modern, responsive user experience. 