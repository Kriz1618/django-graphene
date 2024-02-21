from django.conf import settings
from django.http import JsonResponse
from requests.models import Request, Response


class TokenValidationMiddleware:
    def __init__(self: "TokenValidationMiddleware", get_response: Response) -> None:
        self.get_response = get_response

    def __call__(self: "TokenValidationMiddleware", request: Request) -> Response:
        if settings.VALIDATE_TOKEN:
            token = request.headers.get("Authorization")
            if not token or not self.is_valid_token(token):
                # If the token is not valid, return an error response
                return JsonResponse({"error": "Token not sent"}, status=401)

        return self.get_response(request)

    def is_valid_token(self: "TokenValidationMiddleware", token: str) -> bool:
        # Pending token validation
        return True
