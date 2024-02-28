from drf_yasg import openapi
from user.serializers import GetUserMeSerializer


user_register_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='User email'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='User password'),
        'kvkk': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='User kvkk'),
        'is_membership': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='User membership'),
        'is_electronic_commerce': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='User electronic commerce'),
    },
)

user_register_response_body = {
    500: 'Internal Server Error',
    404: 'Not Found',
    400: openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'error': openapi.Schema(type=openapi.TYPE_STRING, description='Error message for Bad Request'),
        }
    ),
    200: openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'status': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Success status of the request'),
            'message': openapi.Schema(type=openapi.TYPE_OBJECT, description='The created user data or error messages'),
        }
    ),
}

user_get_response_body = {
    500: 'Internal Server Error',
    404: 'Not Found',
    200: openapi.Response(
        description='Successful retrieval of the user details',
        schema=GetUserMeSerializer(),
    )
}