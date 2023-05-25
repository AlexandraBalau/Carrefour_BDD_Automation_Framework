Feature: Check the Forgot password functionality

  Background:

    Given login: I am a user on the login page
    When  login: I click on the forgot password link
    When  base: Close cookies popup

  @invalid_mail
  Scenario: Check validation error message when email is invalid format
    When forgot_pass: I fill in my email "my_email@"
    When forgot_pass: I click on the new password button
    Then forgot_pass: I verify the notification message "Ne pare rau, nu am putut trimite e-mail-ul/mesajul pentru resetarea parolei."

  @empty_mail
  Scenario: Check validation error message when email is empty
    When forgot_pass: I make sure that email input is cleared
    When forgot_pass: I click on the new password button
    Then forgot_pass: I verify the email error message "Acesta este un camp obligatoriu."

  @multiple_value_email
  Scenario Outline: Check various email validation
    When forgot_pass: I fill in my email "<email>"
    When forgot_pass: I click on the new password button
    Then forgot_pass: I verify the email error message "<expected_error>"
    Then forgot_pass: I verify the notification message "<expected_notification>"

  Examples:
    |email        |expected_notification                                                          |expected_error                                       |
    |test         |Ne pare rau, nu am putut trimite e-mail-ul/mesajul pentru resetarea parolei.   |None                                                 |
    |test@        |Ne pare rau, nu am putut trimite e-mail-ul/mesajul pentru resetarea parolei.   |None                                                 |
    |test.com     |Ne pare rau, nu am putut trimite e-mail-ul/mesajul pentru resetarea parolei.   |None                                                 |
    |test@mail.com|Daca exista un cont asociat adresei de email/telefon test@mail.com vei primi un email/mesaj cu link-ul pentru resetarea parolei.|None|