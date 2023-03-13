import pytest
import time
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from modules.ui.page_objects.sign_up_page import SignUpPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of

random_input = str(random.randint(101, 999))

@pytest.mark.ui5
def test_signup_wrong():
    random_input = str(random.randint(101, 999))
    mail_invalid = "username"
    mail_valid = "username" + random_input + "@gmail.com"
    password_invalid = "password"
    password_valid = "password"
    username_invalid = "username"
    username_valid = username_invalid + random_input

    random_input = str(random.randint(101, 999))

    mail_invalid = "username"
    mail_valid = "username" + random_input + "@gmail.com"
    password_invalid = "password"
    password_valid = "password"
    username_invalid = "username"
    username_valid = username_invalid + random_input
    

    sign_up = SignUpPage()
    sign_up.go()
    time.sleep(1)

    # Try to find if the EMAIL field appears
    try:
        sign_up.email_field.find_element()
        print("Email field appears.")
    except NoSuchElementException:
        print("Email field is not displayed yet.")

    # Test INVALID EMAIL
    sign_up.email_field.input_text(mail_invalid)
    time.sleep(1)
    try:
        sign_up.email_error.find_element()
        assert sign_up.email_error.text == "Email is invalid or already taken"
        print(sign_up.email_error.text)
    except NoSuchElementException:
        print("Email Error message is not displayed.")
    time.sleep(1)

    # Clear EMAIL field
    sign_up.email_field.clear_text()
    time.sleep(1)
    # Test VALID EMAIL
    sign_up.email_field.input_text(mail_valid)
    time.sleep(1)
    sign_up.email_continue_button.click()

    try:
        sign_up.password_field.find_element()
    except NoSuchElementException:
        print("The Password field is not displayed.")
    time.sleep(1)

    assert sign_up.check_title() == "Join GitHub · GitHub", f"Test Failed: actual page is {sign_in.check_title()}."
    sign_up.close()


@pytest.mark.ui1
def test_signup_page_title():
    sign_up = SignUpPage()
    sign_up.go()
    time.sleep(1)
    assert sign_up.check_title() == "Join GitHub · GitHub", f"Test Failed: actual page is {sign_in.check_title()}."
    print("*** Test passed. The page title is correct.")
    sign_up.close()


@pytest.mark.ui1
def test_signup_email_taken():
    male_taken = "romchablack@gmail.com"
    sign_up = SignUpPage()
    sign_up.go()
    time.sleep(1)

    # Try to find if the EMAIL field appears
    try:
        sign_up.email_field.find_element()
    except NoSuchElementException:
        print("Email field is not displayed yet.")

    # Test TAKEN EMAIL
    sign_up.email_field.input_text(male_taken)
    time.sleep(1)
    try:
        sign_up.email_error.find_element()
        assert sign_up.email_error.text == "Email is invalid or already taken"
        print(sign_up.email_error.text)
    except NoSuchElementException:
        print("Email Error message is not displayed.")
    time.sleep(1)
    print("*** Test passed. It is impossible to register with taken email.")
    sign_up.close()


@pytest.mark.ui1
def test_signup_email_invalid():
    mail_invalid = "username"
    sign_up = SignUpPage()
    sign_up.go()
    time.sleep(1)

    # Try to find if the EMAIL field appears
    try:
        sign_up.email_field.find_element()
    except NoSuchElementException:
        print("Email field is not displayed yet.")

    # Test INVALID EMAIL
    sign_up.email_field.input_text(mail_invalid)
    time.sleep(1)
    try:
        sign_up.email_error.find_element()
        assert sign_up.email_error.text == "Email is invalid or already taken"
        print(sign_up.email_error.text)
    except NoSuchElementException:
        print("Email Error message is not displayed.")
    time.sleep(1)
    print("*** Test passed. It is impossible to register with invalid email.")
    sign_up.close()


@pytest.mark.ui5
def test_signup_password_field():
    mail_valid = "username" + random_input + "@gmail.com"
    sign_up = SignUpPage()
    sign_up.go()
    time.sleep(1)

    # Confirm the EMAIL is displayed
    try:
        sign_up.email_field.find_element()
    except NoSuchElementException:
        print("Email field is not displayed yet.")

    # Test INVALID EMAIL
    sign_up.email_field.input_text(mail_invalid)
    time.sleep(1)
    try:
        sign_up.email_error.find_element()
        assert sign_up.email_error.text == "Email is invalid or already taken"
        print(sign_up.email_error.text)
    except NoSuchElementException:
        print("Email Error message is not displayed.")
    time.sleep(1)
    print("*** Test passed. It is impossible to register with invalid email.")
    sign_up.close()