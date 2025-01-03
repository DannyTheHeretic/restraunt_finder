import logging

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logging.info(f"Request: {request.method} {request.path}")
        response = self.get_response(request)
        logger.info(f"Response: {response.status_code}")
        return response

class ServerCleanerMiddleware:
    """Clean the Server From Middleware."""

    def __init__(self, get_response: any) -> None:
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request: any):  # noqa: ANN204
        """Call that is made."""
        response = self.get_response(request)
        response.__setitem__("Server", "Nginx")
        return response