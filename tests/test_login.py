from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from helpers import SingInAndRegistartion, TestData, URLData, unique_email


class TestLogInLogOut:

    def test_login_with_existing_user(self, web_driver) -> None:
        wait = WebDriverWait(web_driver, 15)
        email = unique_email()
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
        # Заполнить Email
        wait.until(
            EC.visibility_of_element_located(SingInAndRegistartion.email_filed)
        ).send_keys(email)
        # Ввод пароля
        wait.until(
            EC.visibility_of_element_located(SingInAndRegistartion.password_field)
        ).send_keys(TestData.PASSWORD)
        # Подтверждение пароля
        wait.until(
            EC.visibility_of_element_located(
                SingInAndRegistartion.submit_password_field
            )
        ).send_keys(TestData.PASSWORD)
        # Нажать кнопку «Создать аккаунт»
        wait.until(
            EC.element_to_be_clickable(SingInAndRegistartion.create_account_button)
        ).click()
        # Нажать кнопку выход
        wait.until(
            EC.element_to_be_clickable(SingInAndRegistartion.exit_button)
        ).click()
        # Нажать кнопку «Вход и регистрация»
        wait.until(
            EC.element_to_be_clickable(
                SingInAndRegistartion.sing_in_and_registration_button
            )
        ).click()
        # Ввод email
        wait.until(
            EC.visibility_of_element_located(SingInAndRegistartion.email_filed)
        ).send_keys(email)
        # Ввод пароля
        wait.until(
            EC.visibility_of_element_located(SingInAndRegistartion.password_field)
        ).send_keys(TestData.PASSWORD)
        # Нажать кнопку войти
        wait.until(
            EC.element_to_be_clickable(SingInAndRegistartion.sing_in_button)
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

    def test_logout(self, web_driver) -> None:
        wait = WebDriverWait(web_driver, 15)
        email = unique_email()
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
        # Заполнить Email
        wait.until(
            EC.visibility_of_element_located(SingInAndRegistartion.email_filed)
        ).send_keys(email)
        # Ввод пароля
        wait.until(
            EC.visibility_of_element_located(SingInAndRegistartion.password_field)
        ).send_keys(TestData.PASSWORD)
        # Подтверждение пароля
        wait.until(
            EC.visibility_of_element_located(
                SingInAndRegistartion.submit_password_field
            )
        ).send_keys(TestData.PASSWORD)
        # Нажать кнопку «Создать аккаунт»
        wait.until(
            EC.element_to_be_clickable(SingInAndRegistartion.create_account_button)
        ).click()
        # Нажать кнопку выход
        wait.until(
            EC.element_to_be_clickable(SingInAndRegistartion.exit_button)
        ).click()
        # Нажать кнопку «Вход и регистрация»
        wait.until(
            EC.element_to_be_clickable(
                SingInAndRegistartion.sing_in_and_registration_button
            )
        ).click()
        # Ввод email
        wait.until(
            EC.visibility_of_element_located(SingInAndRegistartion.email_filed)
        ).send_keys(email)
        # Ввод пароля
        wait.until(
            EC.visibility_of_element_located(SingInAndRegistartion.password_field)
        ).send_keys(TestData.PASSWORD)
        # Нажать кнопку войти
        wait.until(
            EC.element_to_be_clickable(SingInAndRegistartion.sing_in_button)
        ).click()
        # Нажать кнопку выход
        wait.until(
            EC.element_to_be_clickable(SingInAndRegistartion.exit_button)
        ).click()
        assert (
            wait.until(
                EC.invisibility_of_element_located(SingInAndRegistartion.user_image)
            )
            and wait.until(
                EC.invisibility_of_element_located(SingInAndRegistartion.user_name)
            )
            and wait.until(
                EC.visibility_of_element_located(
                    SingInAndRegistartion.place_an_ad_button
                )
            ).is_displayed()
            and wait.until(
                EC.visibility_of_element_located(
                    SingInAndRegistartion.sing_in_and_registration_button
                )
            ).is_displayed()
            and web_driver.current_url == URLData.BASE_URL
        )
