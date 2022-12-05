from selene.support.shared import browser
from selene import be, have


def test_filled_form():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').should(be.blank).set_value('Aleksey')
    browser.element('#lastName').should(be.blank).set_value('Yablonskiy')
    browser.element('#userEmail').should(be.blank).set_value('alekseyablonskiy@gmail.com')
    browser.element('[for=gender-radio-1]').click()
    browser.element('#userNumber').should(be.blank).set_value('123456789012345')
    browser.element('#subjectsInput').should(be.blank).set_value('About my friends')
    browser.element('[for=hobbies-checkbox-3]').click()
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))


def test_unfilled_form():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#userForm').should(have.no.css_class('was-validated'))
    browser.element('#submit').click()
    browser.element('#userForm').should(have.css_class('was-validated'))
