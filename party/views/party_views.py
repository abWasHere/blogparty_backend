from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from party.models import Party
from party.serializers import PartySerializer


@api_view(["GET", "POST"])
def get_post_parties(req):
    if req.method == "GET":
        all_parties = Party.objects.all()
        serializer = PartySerializer(
            all_parties, context={"request": req}, many=True
        )
        return Response(serializer.data)

    if req.method == "POST":
        serializer = PartySerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["PUT","DELETE"])
# def party_detail(req):
#     if req.method == "PUT":
        

#     if req.method == "DELETE":
#         pass