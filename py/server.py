import json
import requests
import query as ep
 
class server(ep):

  global endpoint_url
  endpoint_url = f"https://api.spotify.com/v1/users/{ep.user_id}/playlists"
    

  def request_generator(self,name = "unnamed", desc = "unnamed", is_public = False):
    
    request_body = json.dumps({
      "name": name,
      "description": desc,
      "public": is_public
      })

    return request_body

  def playlist_id_generator(self, request_body):
    
    response = requests.post(url = server.endpoint_url, data = request_body, headers={
      "Content-Type":"application/json", 
      "Authorization":f"Bearer {ep.token}"})

    if response.status_code != 201:
      return "HTTP Error"

    url = response.json()['external_urls']['spotify']
    
    return (response.json()['id'], url)

  def playlist_run(self):
    req  = self.request_generator("demop_playlist","playlist created with python",False)
    playlist_id, playlist_url = self.playlist_id_generator(req)
    playist_endpoint_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

    request_body = json.dumps({
          "uris" : ep.uris
        })
    response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {ep.token}"})

    if response.status_code != 201:
          print("HTTP Error")
    return playlist_url
    
