*** Settings ***
Library  SeleniumLibrary
Documentation  Action Chains

*** Variables ***
${url}  https://the-internet.herokuapp.com/

*** Test Cases ***
Handling Drag and drop action
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    1s

    Click Element    //a[text()="Drag and Drop"]
    Sleep    1s
    Drag And Drop    id="column-b"    id="column-a"
    Sleep    1s
    Close Browser

Handling mouse hover
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    1s

    Click Element    //a[text()="Hovers"]

    Mouse Over    (//div[@class="figure"])[1]
    Sleep    1s
    Mouse Over    //h5[text()="name: user2"]/ancestor::div[@class="figure"]
    Sleep    1s

Scroll to the Element
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep  1s

    Scroll Element Into View    //a[text()="Typose"]
    Sleep    3s
*** Keywords ***