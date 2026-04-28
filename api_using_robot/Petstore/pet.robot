*** Settings ***
Library  RequestsLibrary
Library  Collections
Library  JSONLibrary

*** Variables ***
${BASE_URL}  https://petstore.swagger.io/v2

*** Test Cases ***
Add Pet
    [Documentation]  Add a new pet to the store
    Create Session    petapi    ${BASE_URL}  verify=True
    ${payload}=  Load Json From File    ${CURDIR}/../data/add_pet.json
    ${response}=  POST On Session   petapi    /pet    json=${payload}
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}

Updating existing Pet
    [Documentation]  update existing pet
    Create Session    petapi    ${BASE_URL}  verify=True
    ${payload}=  Load Json From File    ${CURDIR}/../data/update_pet.json
    ${response}=  PUT On Session   petapi    /pet    json=${payload}
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}

Find pet by status
    [Documentation]  find pet by status
    Create Session    petapi    ${BASE_URL}  verify=True
    ${qp}=  Create Dictionary    status=available


    ${response}=  GET On Session   petapi    /pet/findByStatus  params=${qp}
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}


Find pet by id
    [Documentation]  find pet by id

    Create Session    petapi    ${BASE_URL}  verify=True
    ${response}=  GET On Session   petapi    /pet/50
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}


Upload an image
    Create Session    petapi    ${BASE_URL}  verify=True
    ${form_data}=  Create Dictionary    additionalMetadata=googlie's img
    ${file_path}=  Set Variable    ${CURDIR}/../Data/cat_img.jpg
    ${file}=  Evaluate   {'file': open(r'${file_path}','rb')}

    ${response}=  POST On Session   petapi    /pet/50/uploadImage
    ...    data=${form_data}
    ...    files=${file}

    Should Be Equal As Integers    ${response.status_code}    200

Update pet with form date
    Create Session    petapi    ${BASE_URL}  verify=True
    ${form_data}=  Create Dictionary    name=googlie    status=sold

    ${response}=  POST On Session   petapi    /pet/50
    ...    data=${form_data}

    Should Be Equal As Integers    ${response.status_code}    200

Delete a pet
    Create Session    petapi    ${BASE_URL}  verify=True
    ${response}=  DELETE On Session   petapi    /pet/50
    Should Be Equal As Integers    ${response.status_code}    200

















