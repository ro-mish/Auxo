from flask import Blueprint, request, render_template
from .py import Query

views = Blueprint('views', __name__)

@views.route('/', methods =["GET", "POST"])
def home():
    
    first_name = None
    show = False
    
    token = None
    user_id = None
    seed_artist = None
    seed_track = None
    seed_genre = None
    
    url = ""
    
    if request.method == "POST":
        
        first_name = request.form.get("name")
        token = request.form.get("auth")
        user_id = request.form.get("prof_uri")
        seed_artist = request.form.get("artist_uri")
        seed_track = request.form.get("track")
        seed_genre = request.form.get("genre")
    
        print(token)
        print(user_id)
        
        q = Query.query(token=token,user_id=user_id,artist=seed_artist, track=seed_track)

        url = q.playlist_run()
        
    
    if first_name:
        return render_template("home.html", fname = first_name, url = url, show = True)
    
    else:
        return render_template("home.html")
