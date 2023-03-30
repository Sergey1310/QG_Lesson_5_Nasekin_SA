from selene import browser, have, be


def test_setup_registration_form(setup_browser):
    browser.open('https://demoqa.com/automation-practice-form')
    browser.execute_script('document.querySelector("#fixedban").remove()')
    browser.element('#firstName').should(be.blank).type('Ivan')
    browser.element('#lastName').should(be.blank).type('Ivanov')
    browser.element('#userEmail').should(be.blank).type('IvanovI@qaguru.com')
    '''browser.element('#genterWrapper #gender-radio-1').execute_script('document.getElementById(''"gender-radio-1'
                                                                     '").checked=true')'''
    browser.element('[for=gender-radio-1]').should(be.clickable).click()
    browser.element('#userNumber').type('8888888888')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select>option[value="9"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select>option[value="2000"').click()
    browser.element('[aria-label="Choose Thursday, October 5th, 2000"]').click()
    #browser.element('.subjects-auto-complete__input').type('History')
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
