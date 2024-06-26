from werkzeug.exceptions import HTTPException

class UnauthorizedException(HTTPException):
    code = 401
    description = 'Unauthorized'

    def __init__(self, message):
        self.description = message
        super().__init__(self.description)

class DuplicateEmailException(HTTPException):
    code = 409
    description = 'Email already exists.'

    def __init__(self, message=None):
        self.description = message
        super().__init__(self.description)
