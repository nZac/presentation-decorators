import time


class RateLimitReachedWarning(Warning):
    """A warning for when a rate limit is exceeded"""
    pass


class ClientRequestCounter(object):
    """A simple client session tracker for naive rate limiting"""

    def __init__(self, limit=10000, reset=(60*60)):
        """Setup a new Client Reset Counter

        :param limit: the number of requests allowed before current time + reset has passed
        :param reset: the number of seconds before the limit should be refreshed
        """
        self.limit = limit
        self.reset_span = reset
        self.reset = self.current_time + reset
        self.hits = 0

    @property
    def remianing(self):
        """The number of hits a client can make before reaching their limit."""
        return self.limit - self.hits

    @property
    def current_time(self):
        """The current time in seconds"""
        return int(time.time())

    @property
    def reset_expired(self):
        """The status of the current rate limit timer"""
        return self.reset < self.current_time

    def hit(self):
        """Register a hit on this client"""

        # Check if the limit should be reset
        if self.reset_expired:
            self.reset_hits()

        # Verify the client has not overstepped their limit
        if (self.hits + 1) > self.limit:
            raise RateLimitReachedWarning()

        # Register the hit
        self.hits += 1

    def reset_hits(self):
        """Reset the hit count and reassign the reset time"""
        self.hits = 0
        self.reset = self.current_time + self.reset_span
