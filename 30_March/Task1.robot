Task1
navigate to the website
scroll to the popup windows
click on it
switch to the window and return me the title switch to the window and return me the title
switch back to the parent window and assert the heading of both current and previous page




*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handling multiple window handles
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Scroll Element Into View    xpath=//button[@id="PopUp"]

    Click Element    //button[@id="PopUp"]
    Sleep  1s

    @{windows}  Get Window Handles
    @{titles}  Get Window Titles
    Log To Console    ${titles}

    Switch Window  ${windows}[1]
    Sleep  3s
    Page Should Contain Element    xpath=//h1[text()="Selenium automates browsers. That's it!"]
    Log to Console  @titles[-1]

    Switch Window  ${windows}[0]
    Sleep  2s
    Page Should Contain Element    xpath=//h1[contains(text(),'Automation')]

    Switch Window  ${windows}[-1]
    Page Should Contain Element    xpath=//span[text()="Playwright"]

    Sleep  1s

    Close Browser