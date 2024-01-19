from demoqa_tests.pages.registration_page import RegistrationPage
import allure


@allure.title('Success student registration')
def test_registration():
    registration_page = RegistrationPage()

    with allure.step('Open registration page'):
        registration_page.open_registration_page()

    # WHEN
    with allure.step('Fill the form'):
        registration_page.fill_first_name('Diana')
        registration_page.fill_last_name('Sagaeva')
        registration_page.fill_user_email('d_sagaeva@mail.ru')
        registration_page.gender_selection('Female')
        registration_page.fill_user_phone_number('1234567890')
        registration_page.fill_date_of_birth('2001', 'June', '12')
        registration_page.select_user_subject('English')
        registration_page.user_hobby_checkbox('Sports')
        registration_page.user_picture('tony.jpg')
        registration_page.user_current_adress('Leningradskoe shosse ')
        registration_page.user_state('Uttar Pradesh')
        registration_page.user_city('Agra')

    with allure.step('Submit form'):
        registration_page.submit_the_form()

        # THEN
    with allure.step('Check results'):
        registration_page.should_registered_user_with(
            'Diana Sagaeva',
            'd_sagaeva@mail.ru',
            'Female',
            '1234567890',
            '12 June,2001',
            'English',
            'Sports',
            'tony.jpg',
            'Leningradskoe shosse',
            'Uttar Pradesh Agra',
        )

    with allure.step('Close the form'):
        registration_page.close_the_form()
