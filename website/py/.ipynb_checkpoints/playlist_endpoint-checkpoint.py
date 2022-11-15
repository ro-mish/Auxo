import json
import requests
import endpoint_filters as ep
 
class server:

  endpoint_url = f"https://api.spotify.com/v1/users/{ep.user_id}/playlists"
    
  def request(self,name = "default", desc = "default", public = False):
    
    request_body = json.dumps({
      "name": name,
      "description": desc,
      "public": public
      })

    return request_body

  def response(request_body):
    response = requests.post(url = server.endpoint_url, data = request_body, headers={
      "Content-Type":"application/json", 
      "Authorization":f"Bearer {ep.token}"})

    if response.status_code != 201:
      return "HTTP Error"

    url = response.json()['external_urls']['spotify']
    return response.json()['id']


