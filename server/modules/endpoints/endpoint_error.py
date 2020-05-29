#todo: rewrite all errors to custom exceptions
class EndpointError:
    
    MISSING_REQUIRED_PARAM = 1
    METHOD_NOT_ALLOWED = 2
    WRONG_PARAM = 3

    @classmethod
    def json(self, error_id, message, custom_data = {}):
        
        return {
            "error_id": error_id,
            "error_message": message,
            "error_data": custom_data
        }
