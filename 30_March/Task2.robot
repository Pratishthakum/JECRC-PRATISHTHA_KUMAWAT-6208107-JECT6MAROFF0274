#navigate to the website and handle alerts , also perform assertion

#Navigate to website
#scroll to popup windw
#click on it
#switch to the window and return title
#switch back to parent window and assert heading of the page

*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Simple alert
    Open Browser  ${url}  chrome
    Maximize Browser Window

    Click Element    id=alertBtn
    Handle Alert
    #will by default it will wait for alert to pop up and accept it

    Sleep    5s
    Close Browser

Confirmation alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Scroll Element Into View    xpath=//h2[text()="Alerts & Popups"]

    Sleep  2s


    Click Element    id=confirmBtn
    Handle Alert
    Page Should Contain    You pressed OK!


    Click Element    id=confirmBtn
    Handle Alert  action=DISMISS
    Sleep    2s
    Page Should Contain    You pressed Cancel!

    Sleep  2s

    Close Browser

Prompt Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep  2s


    Click Element    id=promptBtn
    Input Text Into Alert    PratishthaKumawat
    Sleep  2s
    Page Should Contain    Hello PratishthaKumawat! How are you today?


    Click Element    id=promptBtn
    Input Text Into Alert  Hello  action=DISMISS
    Page Should Contain    User cancelled the prompt.
    Sleep    2s
