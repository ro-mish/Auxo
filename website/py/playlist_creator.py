import json
import requests
import query as ep
import server as pe


req = pe.server.request("playlist1","playlist created python",False)
playlist_id = pe.server.response(req)

endpoint_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

request_body = json.dumps({
          "uris" : ep.uris
        })
response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {ep.token}"})

if response.status_code != 201:
      print("HTTP Error")