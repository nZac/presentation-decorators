import flask
import datetime
from middleware import ratelimit

# Create a simple Flask application
app = flask.Flask(__name__)


@app.route('/users')
@ratelimit
def users():
    return flask.json.jsonify(**{
        'id': 1,
        'first_name': 'john',
        'last_name': 'smith'
    })


@app.route('/posts')
@ratelimit
def posts():
    return flask.json.jsonify(**{
        'id': 1,
        'title': 'Decorators for fun and profit!',
        'publish_date': datetime.date(2015, 7, 1)
    })

if __name__ == '__main__':
    app.run()
