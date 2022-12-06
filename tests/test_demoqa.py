from selene.support.shared import browser
from selene import have


def test_filled_form():
    browser.open('https://demoqa.com/automation-practice-form')
    #user name
    browser.element('#firstName').type('Aleksey')
    browser.element('#lastName').type('Yablonskiy')
    #personal data
    browser.element('#userEmail').type('alekseyablonskiy@gmail.com')
    browser.element('[for=gender-radio-1]').click()
    browser.element('#userNumber').type('123456789012345')
    #user birthday
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="10"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1996"]').click()
    browser.element('.react-datepicker__day--027').click()
    #subject and hobbies
    browser.element('#subjectsInput').type('English').press_enter()
    # User address
    browser.element('#currentAddress').type("Minsk")
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Noida').press_enter()

    #submitting form
    browser.element('#submit').click()
    #result
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table').should(have.text(
        'Aleksey Yablonskiy' and
        'alekseyablosnkiy@gmail.com' and
        'Male' and
        '123456789012345' and
        '27 October, 1996' and
        'English' and
        'Minsk' and
        'NCR Noida'
    ))


def test_unfilled_form():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#userForm').should(have.no.css_class('was-validated'))
    browser.element('#submit').click()
    browser.element('#userForm').should(have.css_class('was-validated'))
