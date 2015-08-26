import flask
import functools
from rate_limiting import ClientRequestCounter, RateLimitReachedWarning

# How many requests a client can make before limiting out
RATE_LIMIT = 10

# The clients that have connected to the application
api_clients = {}


def ratelimit(view):
    @functools.wraps(view)
    def wrapped_func(*args, **kwargs):
        ip_addr = flask.request.remote_addr

        # The current client requesting a page
        client = api_clients.get(ip_addr)

        # Have we seen this client before? If not create a new naive "session" for them.
        if client is None:
            client = api_clients[ip_addr] = ClientRequestCounter(RATE_LIMIT, reset=5)

        try:
            # Register a hit for the client
            client.hit()
        except RateLimitReachedWarning:
            # This client is over the limit of requests before a counter reset
            resp = flask.json.jsonify(
                message='Rate Limit Exceeded'
            )
            resp.status_code = 403
        else:
            # This client still has requests remaining, call the function
            resp = view(*args, **kwargs)

        # Add helpful rate limit headers
        resp.headers['RateLimit-Limit'] = client.limit
        resp.headers['RateLimit-Remaining'] = client.remianing
        resp.headers['RateLimit-Resets'] = client.reset

        return resp

    return wrapped_func
