import fastjsonschema
import json
from flask_restful import reqparse, Resource
from pathlib import Path

parser = reqparse.RequestParser()


class BaseResource(Resource):
    SCHEMA_FOLDER = 'json-schema'
    SCHEMA_FILE = ''

    def __init__(self):
        self.parser = parser

    def get_json_schema(self):
        return Path.cwd() / self.SCHEMA_FOLDER / self.SCHEMA_FILE

    def validate(self, input_data):
        try:
            with open(self.get_json_schema(), 'r') as file:
                schema = json.load(file)
            return True, fastjsonschema.validate(schema, input_data)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            return False, {
                'json_schema': {
                    'valid': False,
                    'reason': str(e)
                }
            }
        except Exception as e:
            return False, {
                'input': {
                    'valid': False,
                    'reason': str(e)
                }
            }
