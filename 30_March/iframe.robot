*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://demo.automationtesting.in/Frames.html

*** Test Cases ***
Handling single iframe
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep   2s

    Select Frame   id=singleframe

    Input Text    xpath=//input[@type="text"]    PRATI
    Sleep  3s
    Unselect Frame

    Close Window
