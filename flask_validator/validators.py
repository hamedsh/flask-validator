class Validators():

    @staticmethod
    def required(request_data, validation_arg=None):
        error_msg = 'This field is required'
        if isinstance(request_data, int):
            if request_data is None:
                return { 'status': False, 'message': error_msg}
        else:
            if request_data is None or len(request_data) == 0:
                return { 'status': False, 'message': error_msg}
        return { 'status': True}

    @staticmethod
    def max(request_data, validator_arg):
        error_msg = f'This field must not be greater than {validator_arg[0]}'
        if isinstance(request_data, int):
            if request_data > int(validator_arg[0]):
                return { 'status': False, 'message': error_msg}
        else:
            if len(request_data) > int(validator_arg[0]):
                return { 'status': False, 'message': error_msg}
        return { 'status': True}

    @staticmethod
    def min(request_data, validator_arg):
        error_msg = f'This field must not be less than {validator_arg[0]}'
        if isinstance(request_data, int):
            if request_data < int(validator_arg[0]):
                return { 'status': False, 'message': error_msg}
        else:
            if len(request_data) < int(validator_arg[0]):
                return { 'status': False, 'message': error_msg}
        return { 'status': True}

validators = {
    'required': Validators.required,
    'max': Validators.max
}