class SpotSearch:
    
    sp = spotipy.Spotify(auth_manager = SpotifyClientCredentials(
    client_id = "",
    client_secret = ""))
    
    def __init__(self,name,genre,artist):
        
        assert type(name) == str
        assert type(genre) == str
        
        self.name = name
        self.genre = genre
        self.artist = artist
        
    
        
        
    def artist_genre(artist):
        assert type(artist) == str
        
        results = sp.search(q = f'{artist}', type = 'artist',limit = 40)
        
        rec_list = results['artists']['items'][0]['genres']

        for i in range(len(rec_list)):
            rec_list[i] = rec_list[i].replace(' ','-')

        genre = (g_rec & set(rec_list))
        
        return genre
    
        
    def artist_genre_playlist(artist):
        
        genres = artist_genre(self,artist)
        
        recs = sp.recommendations(seed_genres = genres, limit = 20)

        for count, i in enumerate(recs['tracks']):
            album_dict[count+1] = i['album']['name']
        return album_dict
    
    def playlist():
        
        album_dict = {}
        
        genres = sp.recommendation_genre_seeds()['genres']
        
        rec_list = [genres[np.random.randint(len(g_rec))] for i in range(4)]
        
        recs = sp.recommendations(seed_genres = rec_list, limit = 20)

        for count, i in enumerate(recs['tracks']):
            album_dict[count+1] = i['album']['name']
        
        return album_dict
    