class SubscriberNotFound(Exception):
    def __init__(self, subscriber_id=None):
        self.subscriber_id = subscriber_id
        self.message = "Subscriber not found"

    def __str__(self):
        return f"{self.subscriber_id} -> {self.message}"
