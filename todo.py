from flask import request, jsonify
from flask_restx import Resource, Api, Namespace, fields


todos = {}
count = 1


Todo = Namespace(
    name="Todos",
    description="RECOMMANDATION APP에서 사용할 추천 모델 API.",
)

todo_fields = Todo.model('Todo', {  # Model 객체 생성
    'data': fields.String(description='a Todo', required=True, example="what to do")
})

todo_recommand = Todo.inherit('Todo recommand', todo_fields, {
    'todo_id': fields.Integer(description='a Todo ID')
})

@Todo.route('')
class TodoPost(Resource):
    @Todo.expect(todo_fields)
    @Todo.response(201, 'Success', todo_recommand)
    def post(self):
        """Todo 리스트에 할 일을 등록 합니다."""
        global count
        global todos
        
        idx = count
        count += 1
        todos[idx] = request.json.get('data')
        
        return {
            'todo_id': idx,
            'data': todos[idx]
        }, 201

@Todo.route('/<int:todo_id>')
@Todo.doc(params={'todo_id': 'An ID'})
class TodoSimple(Resource):
    @Todo.response(200, 'Success', todo_recommand)
    @Todo.response(500, 'Failed')
    def get(self, todo_id):
        """Todo 리스트에 todo_id와 일치하는 ID를 가진 할 일을 가져옵니다."""
        return {
            'todo_id': todo_id,
            'data': todos[todo_id]
        }
    
    @Todo.response(202, 'Success', todo_recommand)
    @Todo.response(500, 'Failed')
    def put(self, todo_id):
        """Todo 리스트에 todo_id와 일치하는 ID를 가진 할 일을 수정합니다."""
        todos[todo_id] = request.json.get('data')
        return {
            'todo_id': todo_id,
            'data': todos[todo_id]
        }, 202
    
    @Todo.doc(responses={202: 'Success'})
    @Todo.doc(responses={500: 'Failed'})
    def delete(self, todo_id):
        """Todo 리스트에 todo_id와 일치하는 ID를 가진 할 일을 삭제합니다."""
        del todos[todo_id]
        return {
            "delete" : "success"
        }, 202