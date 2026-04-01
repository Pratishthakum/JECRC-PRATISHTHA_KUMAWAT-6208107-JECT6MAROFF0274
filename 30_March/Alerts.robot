*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/javascript_alerts

*** Test Cases ***
Handling Alerts
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep   2s
    Click Button    xpath=//button[@onclick="jsAlert()"]
    Sleep  3s
    Handle Alert
    sleep  3s
    Close Browser


Confirmation Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep   2s
    Click Button    xpath=//button[@onclick="jsConfirm()"]
    Sleep  3s
#    Handle Alert   action=DISMISS
    Handle Alert   action=ACCEPT
    sleep  3s
    Close Browser

Prompt Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep   2s
    Click Button    xpath=//button[@onclick="jsPrompt()"]
    Sleep  3s

#    Input Text Into Alert    PRATI  action=DISMISS
    Input Text Into Alert    PRATI  action=ACCEPT

    sleep  3s
    Close Browser

    
    