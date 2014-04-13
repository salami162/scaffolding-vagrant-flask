from flask.ext.restful import reqparse, Resource

class UserList(Resource):
    def get(self): 
        return {
            'hello': 'welcome to scaffolding',
            'users': len(User.objects())
        }

class User(Resource):
    def get(self): 
        return {
            'hello': 'Thanks for requesting User GET API',
            'user' : 'user1'
        }

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('first_name', type=str, required=True)
        parser.add_argument('last_name', type=str, required=True)
        parser.add_argument('email', type=str, required=True)

        args = parser.parse_args()
        print (args)
        return args