import traceback

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import MatchDetails
from .functions import retrieveApiResponse
from .serializer import MatchDetailSerializer


class MatchDetailsView(APIView):
    def get(self, request):
        try:
            matchId = request.query_params.get('match_id')
            data = MatchDetails.objects.filter(matchId=matchId).last()

            if data:
                return Response(data.response)
            else:
                data = retrieveApiResponse(matchId)
                return Response(data)
        except Exception as e:
            print(e, traceback.format_exc())
            return Response({
                'code' : 404,
                'response' : {
                    'Message' : 'Something went wrong',
                }
            })
