from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str)
        self.parser.add_argument('age', type=str)

    def get(self):
        data = self.parser.parse_args()
        name = data.get("name")
        age = data.get("age")
        return {
            "method": "get",
            "name": name,
            "age": age
        }

    def post(self):
        data = self.parser.parse_args()
        name = data.get("name")
        age = data.get("age")
        return {
            "method": "post",
            "name": name,
            "age": age
        }


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
