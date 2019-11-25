from flask import Flask, request
from flask_caching import Cache
from flask_jwt import jwt_required
from flask_cors import CORS

from settings import APP_SECRET_KEY, CACHE_DEFAULT_TIMEOUT
from demand.api import DemandApi
from auth.dummy import add_jwt


cache = Cache(config={
    'CACHE_TYPE': 'simple', 
    "CACHE_DEFAULT_TIMEOUT": CACHE_DEFAULT_TIMEOUT
})
app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = APP_SECRET_KEY
jwt = add_jwt(app)
cache.init_app(app)


@app.route('/countries')
@cache.cached(key_prefix="all_countries")
@jwt_required()
def get_countries():
    return DemandApi.countries()


@app.route('/attributes')
@cache.cached(key_prefix="all_attributes")
@jwt_required()
def get_attributes():
    return DemandApi.attributes()


@app.route('/surveys')
@cache.cached(key_prefix="all_surveys")
@jwt_required()
def get_surveys():
    return DemandApi.projects()


@app.route('/surveys/<ext_project_id>')
@cache.memoize()
@jwt_required()
def get_survey(ext_project_id):
    return DemandApi.project(ext_project_id)


@app.route('/new-surveys', methods=['PUT'])
@jwt_required()
def new_survey():
    cache.delete("all_surveys")
    return DemandApi.create_project(request.json)


if __name__ == '__main__':
    app.run()