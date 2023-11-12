from flask import Flask, render_template

app = Flask(__name__)

# Sample movie data with poster URLs
movies = [
    {"title": "PK", "link": "https://www.sonyliv.com/movies/pk-1000041836?utm_source=Google&utm_medium=WatchNow&utm_campaign=1000041836", "poster": "static/images/pk.jpg"},
    {"title": "Queen", "link": "https://www.netflix.com/in/title/80032081?source=35", "poster": "static/images/queen.jpg"},
    {"title": "Mr. Bean's Holiday", "link": "https://www.netflix.com/in/title/70060002?source=35", "poster": "static/images/bean.jpg"},
    {"title": "3 Idiots", "link": "https://www.primevideo.com/dp/amzn1.dv.gti.6ab5ef5d-dd32-c5ab-3a8f-0aff6123c065?autoplay=0&ref_=atv_cf_strg_wb", "poster": "static/images/3idiots.jpg"},
    {"title": "Yeh Jawaani Hai Deewani", "link": "https://www.netflix.com/in/title/70276515?source=35", "poster": "static/images/yjhd.jpg"},
    {"title": "Rab Ne Bana Di Jodi", "link": "https://www.primevideo.com/dp/amzn1.dv.gti.34abea88-67e0-3261-7599-645cb107e723?autoplay=0&ref_=atv_cf_strg_wb", "poster": "static/images/rabne.jpg"},
    {"title": "Baby's day out", "link": "https://www.primevideo.com/dp/amzn1.dv.gti.3ab984a4-cb87-3c08-c00d-5cb0c423c3c5?autoplay=0&ref_=atv_cf_strg_wb", "poster": "static/images/baby.jpg"},
    {"title": "Home Alone", "link": "https://www.primevideo.com/dp/amzn1.dv.gti.22b56962-c47f-9cbd-32d6-5f0b5265da51?autoplay=0&ref_=atv_cf_strg_wb", "poster": "static/images/home.jpg"}

]

@app.route('/')
def index():
    return render_template('movie.html', movies=movies)

if __name__ == '__main__':
    app.run(debug=True)
