# Saucedemo
This is a demo e-commerce app 
<img width="1660" alt="Screenshot 2024-03-14 at 1 33 36 PM" src="https://github.com/niyogv/Saucedemo/assets/77136963/44dee009-de0e-41ae-a408-6a01b280a3d7">
<img width="1657" alt="Screenshot 2024-03-14 at 1 33 56 PM" src="https://github.com/niyogv/Saucedemo/assets/77136963/ba043655-a6a8-43ef-8208-9b60f858fac7">

# Introduction
This project contains an automated test scenario for the SauceDemo website using Selenium and Python.

# Prerequest
- Python 3.x installed
- Selenium WebDriver library installed (pip install selenium)
- Pytest
- Chrome WebDriver

# Test scenario
Here there are two scenarios

- Login test
- Buying test

# Login test cases
- Submitting empty form
- Submitting with only username
- Submitting with only password
- Submitting with invalid cred
- Submitting with valid cred

# Running the test
pytest test_login.py

# Buying test
Here user login with valid cred and buy the product

# Running the test
pytest test_buy.py

# CI health pipeline
Here whenever commit done to this repo to main branch the CI pipeline will trigger and perform health check on the login test



