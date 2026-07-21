import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from helpers import Errors, SingInAndRegistartion, TestData, URLData, unique_email


class TestRegistration:

    def test_registration(self, web_driver) -> None:
        wait = WebDriverWait(web_driver, 15)
        # Нажать кнопку «Вход и регистрация»
        wait.until(
            EC.element_to_be_clickable(
                SingInAndRegistartion.sing_in_and_registration_button
            )
        ).click()
        # Нажать кнопку «Нет аккаунта»
        wait.until(
            EC.element_to_be_clickable(SingInAndRegistartion.account_not_exist_button)
        ).click()
        # Дождаться появления формы регистрации и заполнить все поля
        email_field = wait.until(
            EC.visibility_of_element_located(SingInAndRegistartion.email_filed)
        )
        email_field.send_keys(unique_email())
        password_field = wait.until(
            EC.visibility_of_element_located(SingInAndRegistartion.password_field)
        )
        password_field.send_keys(TestData.PASSWORD)
        confirm_password_field = wait.until(
            EC.visibility_of_element_located(
                SingInAndRegistartion.submit_password_field
            )
        )
        confirm_password_field.send_keys(TestData.PASSWORD)
        # Нажать кнопку «Создать аккаунт»
        wait.until(
            EC.element_to_be_clickable(SingInAndRegistartion.create_account_button)
        ).click()
        assert (
            wait.until(
                EC.visibility_of_element_located(SingInAndRegistartion.user_image)
            ).is_displayed()
            and wait.until(
                EC.visibility_of_element_located(SingInAndRegistartion.user_name)
            ).is_displayed()
            and wait.until(
                EC.visibility_of_element_located(
                    SingInAndRegistartion.place_an_ad_button
                )
            ).is_displayed()
            and web_driver.current_url == URLData.BASE_URL
        )

    @pytest.mark.parametrize(
        "email_test",
        ["test", "test@test", "test.test", "test.test@test", "test@test.t"],
    )
    def test_registation_with_invalid_email(self, web_driver, email_test: str) -> None:
        wait = WebDriverWait(web_driver, 15)
        # Нажать кнопку «Вход и регистрация»
        login_button = wait.until(
            EC.element_to_be_clickable(
                SingInAndRegistartion.sing_in_and_registration_button
            )
        )
        login_button.click()
        # Нажать кнопку «Нет аккаунта»
        no_account_button = wait.until(
            EC.element_to_be_clickable(SingInAndRegistartion.account_not_exist_button)
        )
        no_account_button.click()
        # Заполнить поле Email некорректным значением
        email_field = wait.until(
            EC.visibility_of_element_located(SingInAndRegistartion.email_filed)
        )
        email_field.clear()
        email_field.send_keys(email_test)
        # Нажать кнопку «Создать аккаунт»
        wait.until(
            EC.element_to_be_clickable(SingInAndRegistartion.create_account_button)
        ).click()
        assert (
            wait.until(
                EC.visibility_of_element_located(Errors.email_filed_error)
            ).is_displayed()
            and wait.until(
                EC.visibility_of_element_located(Errors.password_field_error)
            ).is_displayed()
            and wait.until(
                EC.visibility_of_element_located(Errors.submit_password_field_error)
            ).is_displayed()
            and wait.until(
                EC.visibility_of_element_located(Errors.email_filed_error_message)
            ).is_displayed()
        )

    def test_registration_with_existing_user(self, web_driver) -> None:
        wait = WebDriverWait(web_driver, 15)
        email = unique_email()
        for i in range(2):
            if i == 1:
                wait.until(
                    EC.element_to_be_clickable(SingInAndRegistartion.exit_button)
                ).click()
            # Нажать кнопку «Вход и регистрация»
            wait.until(
                EC.element_to_be_clickable(
                    SingInAndRegistartion.sing_in_and_registration_button
                )
            ).click()
            # Нажать кнопку «Нет аккаунта»
            wait.until(
                EC.element_to_be_clickable(
                    SingInAndRegistartion.account_not_exist_button
                )
            ).click()
            # Заполнить поле Email некорректным значением
            wait.until(
                EC.visibility_of_element_located(SingInAndRegistartion.email_filed)
            ).send_keys(email)
            wait.until(
                EC.visibility_of_element_located(SingInAndRegistartion.password_field)
            ).send_keys(TestData.PASSWORD)
            wait.until(
                EC.visibility_of_element_located(
                    SingInAndRegistartion.submit_password_field
                )
            ).send_keys(TestData.PASSWORD)
            # Нажать кнопку «Создать аккаунт»
            wait.until(
                EC.element_to_be_clickable(SingInAndRegistartion.create_account_button)
            ).click()
        assert (
            wait.until(
                EC.visibility_of_element_located(Errors.email_filed_error)
            ).is_displayed()
            and wait.until(
                EC.visibility_of_element_located(Errors.password_field_error)
            ).is_displayed()
            and wait.until(
                EC.visibility_of_element_located(Errors.submit_password_field_error)
            ).is_displayed()
            and wait.until(
                EC.visibility_of_element_located(Errors.email_filed_error_message)
            ).is_displayed()
        )
