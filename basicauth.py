from rest_framework.response import Response
from django.contrib import auth
import base64


def authenticate_user(request):
	for key, value in request.headers.items():
		if key == "Authorization":
			value = value.replace("Basic ", "")
			base64_bytes = value.encode("ascii")
			try:
				decoded = base64.b64decode(base64_bytes)
			except base64.binascii.Error:
				return False
			decoded = decoded.decode("utf-8")
			try:
				username, password = decoded.split(":")
			except ValueError:
				return False
			user = auth.authenticate(username=username, password=password)
			if user is not None:
				return user
			else:
				return False
		

def basic_auth_required(func):
	def wrapper(self, request, **kwargs):
		user = authenticate_user(request)
		if not user:
			return Response({"message": "Unauthorized"}, status=401)
		return func(self, request, user, **kwargs)
	return wrapper
	