import pytest
import time
from modules.ui.page_objects.sign_in_page import SignInPage


@pytest.mark.signin
def test_github_login_wrong_username():

    usrnm = "username"
    psswrd = "password"

    sign_in = SignInPage()
    time.sleep(1)
    sign_in.go()
    assert sign_in.check_title() == "Sign in to GitHub · GitHub"
    time.sleep(1)
    sign_in.login_field.input_text(usrnm)
    time.sleep(1)
    sign_in.password_field.input_text(psswrd)
    time.sleep(1)
    sign_in.sign_in_btn.click()
    time.sleep(1)
    assert sign_in.login_failed_alert.text == "Incorrect username or password.  "
    # sign_in.close()


@pytest.mark.signin
def test_github_email_login_success():

    mail = "romchablack2@gmail.com"
    psswrd = "uBce7cAMRPdBAGs"

    # sign_in = SignInPage()
    # time.sleep(1)
    # sign_in.go()
    assert sign_in.check_title() == "Sign in to GitHub · GitHub"
    time.sleep(1)
    sign_in.login_field.input_text(mail)
    time.sleep(1)
    sign_in.password_field.input_text(psswrd)
    time.sleep(1)
    sign_in.sign_in_btn.click()
    time.sleep(1)
    assert sign_in.check_title() == "GitHub"
    sign_in.close()


@pytest.mark.signin
def test_github_usrnm_login_success():

    usrnm = "romchablack2"
    psswrd = "uBce7cAMRPdBAGs"

    sign_in = SignInPage()
    time.sleep(1)
    sign_in.go()
    assert sign_in.check_title() == "Sign in to GitHub · GitHub"
    time.sleep(1)
    sign_in.login_field.input_text(usrnm)
    time.sleep(1)
    sign_in.password_field.input_text(psswrd)
    time.sleep(1)
    sign_in.sign_in_btn.click()
    time.sleep(1)
    assert sign_in.check_title() == "GitHub"
    sign_in.close()
