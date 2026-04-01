*** Settings ***
#all the imports come here
Documentation  Opening of browsers
Library  SeleniumLibrary

*** variables ***
#store variables here
#types of variables - scalar ${}
#list, and
#dictionary
${url}  https://www.cricbuzz.com/
@{bikes}  ktm  kwasaki  honda  pulsar
&{cars}  nissan=gtr  honda=civic  bmw=m5
#when we call a dictionary variable, we call it using $symbol only, $ converts into scalar quantity

*** Test cases ***
#test scenarios are written here
#each test case runs seperately in robot framework

Opening Chrome Browser
    [Documentation]  Chrome browser navigating to https://www.cricbuzz.com/
    Open Browser  ${url}  chrome
    #takes two parameters, first the link and then the browser
    Maximize Browser Window

    Log  Navigated to cricbuzz using chrome
    #log is a register that stores a track of all test cases , log stores these in log files
    Log To Console  Navigated to cricbuzz using chrome
    Log To Console  ${bikes}[1]
    Log To Console  ${cars.nissan}
    Log To Console  ${cars}
    Log To Console  ${bikes}
    #log written to console
    Sleep  3s

    Close Browser
    #works like driver instance, if u open chrome , it will close all chrome instances

#    Close Window
#    #close current window
#    Close All Browsers
#    #closes all the instances in all the browsers

Opening Edge Browser
    Opening Edge Browser

Opening Firefox Browser
    [Documentation]  Firefox browser navigating to https://www.cricbuzz.com/
    [Tags]  first_tag
    Open Browser  https://www.cricbuzz.com/  firefox
    Maximize Browser Window

    Log  Navigated to cricbuzz using firefox
    Log To Console  Navigated to cricbuzz using firefox

    Close Browser

Opening chrome browser using headless mode
    [Documentation]  Chrome browser navigating to https://www.cricbuzz.com/
    [Tags]  first_tag
    Open Browser  https://www.cricbuzz.com/  headlesschrome
    #takes two parameters, first the link and then the browser
    Maximize Browser Window

    Log  Navigated to cricbuzz using chrome headless mode
    #log is a register that stores a track of all test cases , log stores these in log files
    Log To Console  Navigated to cricbuzz using chrome headless mode
    #log written to console
    Sleep  3s

    Close Browser

*** keywords ***
#user defined keywords are written in keywords section

Opening Edge Browser
    [documentation]  Edge browser navigating to https://www.cricbuzz.com/
    Open Browser  https://www.cricbuzz.com/  edge
    Maximize Browser Window

    Log  Navigated to cricbuzz using edge
    Log To Console  Navigated to cricbuzz using edge

    Close Browser

#robot -d reports -i "first_tag" .\open_browser.robot   : used to run test cases grouped under a tag, -i is used for included the group
#robot -d reports -t "Opening chrome browser using headless mode" .\open_browser.robot : used to run test case using test case name
