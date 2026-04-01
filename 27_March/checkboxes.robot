*** Settings ***
Documentation  handling checkboxes
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/
${url2}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handling Checkboxes
    [Documentation]  herokuapp checkboxes
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep  1s

    Click Element  xpath=//a[text()="Checkboxes"]

    Page Should Contain Checkbox  xpath=(//input[@type="checkbox"])[1]

    Select Checkbox    xpath=(//input[@type="checkbox"])[1]
    Sleep    2s
    Unselect Checkbox    xpath=(//input[@type="checkbox"])[2]
    Sleep    2s

    Close Browser

Handling Checkboxes in test automation
    [Documentation]  test automation
    Open Browser  ${url2}  chrome
    Maximize Browser Window
    Sleep  1s

    Click Element    //input[@id="female"]

    Page Should Contain Checkbox    xpath=//input[@id="sunday"]

    Select Checkbox    xpath=//input[@id="sunday"]
    Sleep  1s

    Select Checkbox    xpath=//input[@id="monday"]
    Sleep  1s

    Select Checkbox    xpath=//input[@id="thursday"]
    Sleep  2s

    Unselect Checkbox    xpath=//input[@id="sunday"]

    Close Browser
