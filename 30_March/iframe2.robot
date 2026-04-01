#Navigate to website
#scroll to popup windw
#click on it
#switch to the window and return title
#switch back to parent window and assert heading of the page

*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://demo.automationtesting.in/Frames.html

*** Test Cases ***
Handling iframes
    Open Browser  ${url}  chrome
    Maximize Browser Window

    Click Element  xpath=//a[text()="Iframe with in an Iframe"]

    Select Frame    xpath=//div[@id="Multiple"]/iframe

    Select Frame  xpath=//iframe[@src="SingleFrame.html"]
    Input Text  xpath=//input[@type="text"]  Pratishtha

    Unselect Frame
    Page should contain  Automation Demo Site
    Sleep  3s

    Close Browser