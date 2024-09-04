from registration_page import RegistrationPage


def test_user_registration(driver):
    registration_page = RegistrationPage(driver)
    registration_page.load()

    registration_page.click_sign_up()
    registration_page.enter_first_name("Test")
    registration_page.enter_last_name("User")
    registration_page.enter_email("testuser@example.com")
    registration_page.enter_password("Password123!")
    registration_page.confirm_password("Password123!")
    registration_page.click_signup_button()
