class AuthorizationError(Exception):
    code = 401
    description = 'Authorization Error'

    def __init__(self, message):
        self.description = message
        super().__init__(self.description)

class RequestDataError(Exception):
    code = 400
    description = 'Request Data Error'

    def __init__(self, message):
        self.description = message
        super().__init__(self.description)

class InvalidTokenError(Exception):
    code = 401
    description = 'Invalid Token Error'

    def __init__(self, message):
        self.description = message
        super().__init__(self.description)