import jwt
from datetime import timedelta, datetime
from django.conf import settings


def create_jwt_token(user):
    payload = {
        'user': user.id,
        'exp': datetime.now() + timedelta(days=1, minutes=0),
        'iat': datetime.now()
    }

    access_token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return access_token