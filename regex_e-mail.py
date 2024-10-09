import re

#validate email - validar e-mail

def validate_email(email):
    default = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(default, email)