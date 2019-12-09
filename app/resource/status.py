from flask_restful import Resource

class Status(Resource):
    def get(self):
        result = {"status": "OK"}
        result_code = 200
        return result, result_code
