*** Settings ***
Library  SeleniumLibrary
Library  OperatingSystem


*** Variables ***
${url}   https://the-internet.herokuapp.com/
${check_downloaded}   C:\Users\Dell\Downloads\file.txt


*** Test Cases ***
Upload
    Open Browser  ${url}  chrome
    Maximize Browser Window
    
    Click Element    xpath=//a[@href="/upload"]
    Sleep   2s
    ${path}  Normalize Path    ${CURDIR}/abc.txt
    Choose File   xpath=//input[@id="file-upload"]  ${path}   
    Sleep  2s
    Click Button    id=file-submit

Download
    Open Browser  ${url}  chrome
    Maximize Browser Window

    Click Element    xpath=//a[@href="/download"]
    Sleep   2s
#  ${path}  Normalize Path    ${CURDIR}/abc.txt
    Click Element   xpath=//a[@href="download/file.txt"]
    Sleep  2s

    Wait Until Created    ${check_downloaded}
    Log To Console    it downloaded successfully
    Close Browser


