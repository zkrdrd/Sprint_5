from random import choice, choices, randint
from string import ascii_letters

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from helpers import (
    CreateProduct,
    Errors,
    Profile,
    SingInAndRegistartion,
    TestData,
    URLData,
    unique_email,
)


class TestCreateProductCard:

    def test_unautorizerd_user(self, web_driver) -> None:
        wait = WebDriverWait(web_driver, 15)
        # Нажать Разместить объявление
        wait.until(
            EC.element_to_be_clickable(SingInAndRegistartion.place_an_ad_button)
        ).click()
        assert wait.until(
            EC.visibility_of_element_located(Errors.place_an_ad_error)
        ).is_displayed()

    def test_autorized_user_condition_product_new(self, web_driver) -> None:
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
        wait.until(
            EC.visibility_of_element_located(SingInAndRegistartion.user_image)
        )  # .is_displayed()
        # Нажать Разместить объявление
        wait.until(
            EC.element_to_be_clickable(SingInAndRegistartion.place_an_ad_button)
        ).click()
        wait.until(
            EC.visibility_of_element_located(CreateProduct.name_field)
        ).send_keys("".join(choices(ascii_letters, k=10)))
        wait.until(
            EC.visibility_of_element_located(CreateProduct.product_description_field)
        ).send_keys("".join(choices(ascii_letters, k=50)))
        wait.until(
            EC.visibility_of_element_located(CreateProduct.price_field)
        ).send_keys(randint(1, 999999))
        # категория
        wait.until(
            EC.element_to_be_clickable(CreateProduct.categoties_dropdown)
        ).click()
        dropdown_category = web_driver.find_elements(
            *CreateProduct.categories_dropdown_elements
        )
        choice(dropdown_category).click()
        # город
        wait.until(EC.element_to_be_clickable(CreateProduct.city_dropdown)).click()
        drop_down_city = web_driver.find_elements(*CreateProduct.city_dropdown_elements)
        choice(drop_down_city).click()
        wait.until(EC.element_to_be_clickable(CreateProduct.publicate_button)).click()
        # в профиль пользователя
        web_driver.get(f"{URLData.BASE_URL}profile")
        wait.until(EC.visibility_of_element_located(Profile.my_ad))
        assert wait.until(
            EC.visibility_of_element_located(Profile.product_card)
        ).is_displayed()

    def test_autorized_user_condition_product_old(self, web_driver) -> None:
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
        wait.until(
            EC.visibility_of_element_located(SingInAndRegistartion.user_image)
        )  # .is_displayed()
        # Нажать Разместить объявление
        wait.until(
            EC.element_to_be_clickable(SingInAndRegistartion.place_an_ad_button)
        ).click()
        wait.until(
            EC.visibility_of_element_located(CreateProduct.name_field)
        ).send_keys("".join(choices(ascii_letters, k=10)))
        wait.until(
            EC.visibility_of_element_located(CreateProduct.product_description_field)
        ).send_keys("".join(choices(ascii_letters, k=50)))
        wait.until(
            EC.visibility_of_element_located(CreateProduct.price_field)
        ).send_keys(randint(1, 999999))
        # категория
        wait.until(
            EC.element_to_be_clickable(CreateProduct.categoties_dropdown)
        ).click()
        dropdown_category = web_driver.find_elements(
            *CreateProduct.categories_dropdown_elements
        )
        choice(dropdown_category).click()
        # город
        wait.until(EC.element_to_be_clickable(CreateProduct.city_dropdown)).click()
        drop_down_city = web_driver.find_elements(*CreateProduct.city_dropdown_elements)
        choice(drop_down_city).click()
        # Состояние товара
        wait.until(
            EC.element_to_be_clickable(
                (CreateProduct.condition_product_old_radiobutton)
            )
        ).click()
        wait.until(EC.element_to_be_clickable(CreateProduct.publicate_button)).click()
        # в профиль пользователя
        web_driver.get(f"{URLData.BASE_URL}profile")
        wait.until(EC.visibility_of_element_located(Profile.my_ad))
        assert wait.until(
            EC.visibility_of_element_located(Profile.product_card)
        ).is_displayed()
