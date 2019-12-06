from flask import Flask
from flask_restful import reqparse, Api, Resource

from controller.email import EmailController

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()


class Status(Resource):
    def get(self):
        result = {"status": "OK"}
        result_code = 200
        return result, result_code


class EmailValidation(Resource):
    def post(self):
        parser.add_argument('email')
        args = parser.parse_args()
        return EmailController.validate(args['email'])


api.add_resource(Status, '/status')
api.add_resource(EmailValidation, '/email/validate')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
