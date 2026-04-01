#Task 3
#
#Navigate to amazon
#Click on electronic in tab
#Check on 'boat' checkbox
#click on any product before clicking store the name of product
#switch to new window
#assert the product name is present in the new window
#print the actual price, discounted price and the percentage
#scroll to add to cart and click on the button
#click on cart icon on top right corner
#check if same product has been added


*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://www.amazon.in/

*** Test Cases ***
Amazon E2E Automation

    Open Browser  ${url}  chrome
    Maximize Browser Window
    Wait Until Location Is    https://www.amazon.in/


    Wait Until Element Is Visible    xpath=//a[text()=" Electronics "]
    Click Element    xpath=//a[text()=" Electronics "]
    Wait Until Element Is Enabled    xpath=//input[@aria-labelledby="boAt"]/following-sibling::i
    Click Element    xpath=//input[@aria-labelledby="boAt"]/following-sibling::i


    ${product_name}  Get Text    xpath=(//div[@role="listitem"])[3]/descendant::div[@data-cy="title-recipe"]/descendant::h2/span

    Click Element    (//div[@role="listitem"])[3]/descendant::div[@data-cy="title-recipe"]/a

    Switch Window  NEW


    Sleep  4s
    Page Should Contain    ${product_name}


    ${actual_price}  Get Text    xpath=(//div[@class="a-section a-spacing-small aok-align-center"]/descendant::span[@aria-hidden="true"])[2]
    ${discount}  Get Text    xpath=//span[@class="apex-savings-container"]/span
    ${discounted_price}  Get Text    xpath=(//span[@aria-hidden="true"]/descendant::span[@class="a-price-whole"])[6]
    Log To Console    ${actual_price} ${discount} ${discounted_price}


    Scroll Element Into View    id=add-to-cart-button
    Click Button    id=add-to-cart-button


    Sleep  2s
    Scroll Element Into View    id=nav-cart
    Click Element    id=nav-cart


    Sleep    3s
    Page Should Contain    ${product_name}

    Sleep  3s
    Close Browser


