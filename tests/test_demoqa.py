import os

from selene.support.shared import browser
from selene import have


def test_filled_form():
    browser.open('/automation-practice-form')
    # username
    browser.element('#firstName').type('Aleksey')
    browser.element('#lastName').type('Yablonskiy')
    # personal data
    browser.element('#userEmail').type('alekseyablonskiy@gmail.com')
    browser.element('[for=gender-radio-1]').click()
    browser.element('#userNumber').type('123456789012345')
    # user birthday
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="10"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1996"]').click()
    browser.element('.react-datepicker__day--027').click()
    # subject and hobbies
    browser.element('#subjectsInput').type('English').press_enter()
    browser.element('[for=hobbies-checkbox-3').click()
    # upload picture
    browser.element('#uploadPicture').set_value(
        os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'files/picture.jpg')))
    # user address
    browser.element('#currentAddress').type("Minsk")
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Noida').press_enter()

    # submitting form
    browser.element('#submit').click()
    # result
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table').should(have.text(
        'Aleksey Yablonskiy' and
        'alekseyablosnkiy@gmail.com' and
        'Male' and
        '123456789012345' and
        '27 October, 1996' and
        'English' and
        'Music' and
        'picture.jpg' and
        'Minsk' and
        'NCR Noida'
    ))


def test_unfilled_form():
    browser.open('/automation-practice-form')
    browser.element('#userForm').should(have.no.css_class('was-validated'))
    browser.element('#submit').click()
    browser.element('#userForm').should(have.css_class('was-validated'))
