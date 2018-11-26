# Flask Validator

This is a validation library for flask app or api

## Installation

`pip install flask-validator`

## Example (Usage)
```
from flask import Flask, jsonify
from flask_validator import ValidatorEngine

app = Flask(__name__)
validator = ValidatorEngine(app)

@app.route('/index', methods=['POST'])
@validator('json', {
    'name': ['required', 'maxa:10']
})
def index():
    return jsonify(
        status=True
    ),200


@app.route('/users/<name>', methods=['POST'])
@validator('query_string', {
    'name': ['required', 'max:10', 'min:3']
})
def test_exp(name):
    return jsonify(
        status=True
    ),200
```

This library uses function decorator pattern, which means the incomming request data is validated before 
the request hit the route function 

### On Error
When there is a validation error, library return a 422 http response status code and a json data containing the error messages.
```
    {
        status: false,
        errors: {
            name: ["This field is required"]
        }
    }
```

### instantiating  ValidatorEngine Class
`validator = ValidatorEngine(app)`

or when use using flask factory function pattern

```
    validator = ValidatorEngine()
    validator.init_app(app)
```

###  Using the validator object
Decorate your route function with the validator object like this..
````
    @validator(<where-to-check-for-data>, <validation-logic>)
```

so you have 
```
    @validator('json', {
        name: ['required, 'min:23']
    })
```

The first argument to the validator decorator is the place where you want the validator to check for incoming data
"json <Data coming from post request>", "query_sting<Data coming from the route url>", "headers <Incoming headers>".

The second arguement is a dictionary holding the validation rules 
```
    { <Field to validate >: [<Rules: A list if the validtion rules to check on the field sepcified> ]}
```

## List of Built in validation rules
...

## Contributions
....

## 





### Author
Created by [Adewumi Ogunbiyi](https://github.com/adekoder)