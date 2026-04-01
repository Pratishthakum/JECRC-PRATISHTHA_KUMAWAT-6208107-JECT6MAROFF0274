*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://practicetestautomation.com/practice-test-login/

*** Test Cases ***
Explicit wait
    Open Browser  ${url}  chrome

    Wait Until Element Is Visible    id=username
    Input Text    id=username    student

    Wait Until Element Is Visible    id=password
    Input Text    id=password    Password123

    Wait Until Element Is Enabled    id=submit
    Click Element    id=submit

    Wait Until Page Contains    Logged In Successfully
    Wait Until Location Is    https://practicetestautomation.com/logged-in-successfully/

    Close Browser



