# VALIDATORS

## HTML
Following errors found and not solved due to lack of time:
> - `<li>` element outside the scope No li element in scope but a li end tag seen.
> - `<div class="card mt-4" id="Custom offer">↩` easy fixed but I havn't found this pece of code  
<br>
No futher erros detected

## CSS
Following warnings found and not solved due to lack of time:
> webkit-background-size is an unknown vendor extension
> -moz-background-size is an unknown vendor extension
> -o-background-size is an unknown vendor extension
<br>
No futher erros detected

## PYTHON

Validating through [PEP8](http://pep8online.com/checkresult)
- App agile_app: clean
- App checkout:
        - models: 38	80	line too long (96 > 79 characters)
        - test_forms - line 11 too long 
        - test_models: unexpected spaces around keyword / parameter equals
        - test_views: continuation line unaligned for hanging indent
- App packages: 
        - unexpected spaces around keyword / parameter equals
- App profiles: no issues.


## JAVASCRIPT

Validating through [JSHINT](https://jshint.com/)

- No errors detected.

# MANUAL TESTING

The webpage is fully responsive.

## TESTING USER STOREIS
All user stories been tested. There are couple of issues to fix in the future.

## Main page

1. As a user I want to get to know what is the website about to define is the content relevant for me
2. As a user I want to be able to easily navigate across the website
3. As a user I want to be able to contact the owner of the website
4. As a user I want to be able to click on the button to get to know the offer
5. As a user I want to be able to send a message via contact form
    - but: the user can click on the button send and the popover will display a message of the *message sent* althought it has been sent yet.
    - please note: emails come through to the owner of the site 

## Registration

1. As a new user I want to register to discover more content so I can purchase package
2. As a user I want to get confirmation about being registrated

## Login 

1. As a user I want to be able to login to see more content
2. As a user I want to be able to pay for the selected service
2. As a user I want to be able to use contact form to discuss date/details

## Checkout

1. As a user I want to be able to select the package 
2. As a user I want to be able to pay for selected package
3. As a user I want to add another package to the shopping cart
4. As a user I want to be able to view the selected package in the shopping cart
5. As a user I want to enter my payment infomation
6. As a user I want to enter my card number to be able to pay for the package
7. As a user I want to be redirected to the order confirmation 
8. As a user I want to be able to be allowed to buy another package

## Profile

1. As a user I want to be able to update address details
    - bug easy to fix: field country has to be change to default instead of drop down
2. As a user I want to see the the order history

## Package management

1. As a superuser I want to be able to add a packacge to the offer
2. As a superuser I want to be able to edit the packacge which is alreday in the offer
3. As a superuser I want to be able to delete the package 

### MANUAL TESTING ON AWS

Please note adding a packing does work but attaching the image does not!




# AUTOMATED TESTING

Covarage report: between 50-80%.
Some tests are failing.
In one case while testing models in profile app. I wrote tests but they are not actually run.

