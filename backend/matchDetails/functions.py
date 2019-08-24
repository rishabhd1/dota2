import json
import requests

from .models import MatchDetails

WEB_API_KEY = '9EE62B263EE3E1770821BDD84524004B'


def insertIntoDatabase(matchId, response):
    """
    Insert the response from DOTA 2 API to database
    """
    invalidResponse = response.get('result').get('error')
    matchDetail = MatchDetails(matchId=matchId)

    if not (matchDetail and invalidResponse):
        MatchDetails.objects.create(matchId=matchId, response=response)

def retrieveApiResponse(matchId):
    """
    Fetch and insert the response from DOTA 2 API to database
    :matchId: Match ID of the game
    """
    params = {'match_id' : matchId, 'key' : WEB_API_KEY}
    api_url = 'http://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/v1'
    response = requests.get(url=api_url, params=params)
    response = response.json()

    if response:
        insertIntoDatabase(matchId, response)
        return response

    return {
        'code' : 404,
        'response' : {
            'Message' : 'Something went wrong',
        }
    }
