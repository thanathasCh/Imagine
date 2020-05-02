from wtforms import Form 
import messages

class RegistrationForm:
    firstName = TextField('First Name', [validators.Required()])
    lastName = TextField('Last Name', [validators.Required()])
    userName = TextField('Username', [validators.Required()])
    password = PasswordField('Password', [validators.Required(),
                                          validators.EqualTo('confirmPassword', message=messages.passwordNotMatch)])
    confirmPassword = PasswordField('Confirm Password', [validators.Required(),
                                                         validators.EqualTo('')])

    def __init__(self):
        super().__init__()