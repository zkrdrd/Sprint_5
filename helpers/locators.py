from selenium.webdriver.common.by import By


class SingInAndRegistartion:
    """Локаторы входа регистракции выхода"""

    sing_in_and_registration_button = (
        By.XPATH,
        "//*[contains(text(), 'Вход и регистрация')]",
    )
    account_not_exist_button = (By.XPATH, "//*[contains(text(), 'Нет аккаунта')]")
    email_filed = (By.NAME, "email")
    password_field = (By.NAME, "password")
    submit_password_field = (By.NAME, "submitPassword")
    create_account_button = (By.XPATH, "//*[contains(text(), 'Создать аккаунт')]")
    user_image = (
        By.XPATH,
        ".//*[contains(@class, 'header_flexRow__Xdqv1')]//*[contains(@class, 'svgSmall')]",
    )
    user_name = (
        By.XPATH,
        ".//*[contains(@class, 'header_flexRow__Xdqv1')]//h3[contains(text(), 'User.')]",
    )
    place_an_ad_button = (
        By.XPATH,
        ".//*[contains(@class, 'header_flexRow__Xdqv1')]//button[contains(text(), 'Разместить объявление')]",
    )
    exit_button = (By.XPATH, "//*[contains(text(), 'Выйти')]")
    sing_in_button = (By.XPATH, ".//button[contains(text(), 'Войти')]")


class Errors:
    """Локаторы ошибок"""

    place_an_ad_error = (
        By.XPATH,
        ".//*[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]",
    )
    password_field_error = (
        By.XPATH,
        ".//*[contains(@name, 'password')]/parent::div[contains(@class, 'input_inputError__fLUP9')]",
    )
    submit_password_field_error = (
        By.XPATH,
        ".//*[contains(@name, 'submitPassword')]/parent::div[contains(@class, 'input_inputError__fLUP9')]",
    )
    email_filed_error = (
        By.XPATH,
        ".//*[contains(@name, 'email')]/parent::div[contains(@class, 'input_inputError__fLUP9')]",
    )
    email_filed_error_message = (
        By.XPATH,
        "//*[contains(@class, 'input_span__yWPqB') and contains(text(),'Ошибка')]",
    )


class CreateProduct:
    """Локаторы страницы создания объявления"""

    name_field = (
        By.XPATH,
        ".//*[contains(@placeholder, 'Название')]",
    )
    product_description_field = (
        By.XPATH,
        ".//*[contains(@placeholder, 'Описание товара')]",
    )
    price_field = (
        By.XPATH,
        ".//*[contains(@placeholder, 'Стоимость')]",
    )
    categoties_dropdown = (
        By.XPATH,
        "//*[contains(@class, 'createListing_shell__A5EA7')]/div[contains(@class, 'createListing_inputRow__fmwXw')]/div[contains(@class, 'dropDownMenu_dropMenu__sBxhz')]//button[contains(@class, 'dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP')]",
    )
    categories_dropdown_elements = (
        By.XPATH,
        "//*[contains(@class, 'dropDownMenu_options__CmHmm')]/button",
    )
    city_dropdown = (
        By.XPATH,
        "//*[contains(@class, 'createListing_shell__A5EA7')]/div[contains(@class, 'dropDownMenu_dropMenu__sBxhz')]//button[contains(@class, 'dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP')]",
    )
    city_dropdown_elements = (
        By.XPATH,
        "//*[contains(@class, 'dropDownMenu_options__CmHmm')]/button",
    )

    condition_product_old_radiobutton = (
        By.XPATH,
        "//*[contains(@value, 'Б/У') and contains(@type, 'radio') and contains(@value, 'Б/У')]/following-sibling::div",
    )
    publicate_button = (By.XPATH, ".//button[contains(text(), 'Опубликовать')]")


class Profile:
    """Локаторы профиля"""

    my_ad = (
        By.XPATH,
        "//*[contains(@class, 'profilePage_listningBlock__Fi6E5')]/h1[contains(text(), 'Мои объявления')]",
    )
    product_card = (
        By.XPATH,
        "//*[contains(@class, 'profilePage_listningBlock__Fi6E5')]//*[contains(@class, 'card')]",
    )
