from flask import Flask
from flask_restx import Resource, Api
from model_ns import Recommend_Model

app = Flask(__name__)
api = Api(
    app,
    version='1.0',
    title="RMM API Server",
    description="RMM API Server!",
    # terms_url="/",
    contact="jinminer58@google.com",
    # license="MIT"
)

# api.add_namespace(Recommand_Model, '/RMM')
api.add_namespace(Recommend_Model, '')
# api.add_resource(Recommand_Model, '/RMM')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)