from django.views.decorators.csrf import csrf_protect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

@extend_schema(
    responses={200: "Subscription payment successful.", 403: "Authentication required."}
)
@api_view(["POST"])
@permission_classes([IsAuthenticated])
@csrf_protect
def paySubscription(request):
    return Response({"msg": "Success"}, 200)


@extend_schema(
    responses={200: "List of subscriptions retrieved successfully.", 403: "Authentication required."}
)
@api_view(["POST"])
@permission_classes([IsAuthenticated])
@csrf_protect
def listSubscriptions(request):
    return Response({"msg": "Success"}, 200)
