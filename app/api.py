from flask import Flask
from flask_restful import Api

from resource.status import Status
from resource.email_validation import EmailValidation

app = Flask(__name__)
api = Api(app)

# Since we have only two endpoints, let's keep the routing here
api.add_resource(Status, '/status')
api.add_resource(EmailValidation, '/email/validate')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
