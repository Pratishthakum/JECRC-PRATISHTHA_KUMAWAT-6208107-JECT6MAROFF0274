

*** Settings ***
Library  SeleniumLibrary

*** Variables ***
#we cannot take input of variables but we can overwrite it
${colors_url}  https://testautomationpractice.blogspot.com/
${browser}  chrome

*** Test Cases ***
Handle dropdown on testautomation
    [Documentation]  handling colors dropdown
    Open Browser  ${colors_url}  ${browser}
    Maximize Browser Window

    Scroll Element Into View    id=colors

    Page Should Contain List    id=colors

    Select From List By Value    id=colors  white
    Select From List By Value    id=colors  blue

    @{selected_options}=  Get Selected List Values    id=colors
    Log To Console    ${selected_options}
    #log only takes single valued data

#    List Selection Should Be    id=colors  white
    List Selection Should Be    id=colors  White  Blue