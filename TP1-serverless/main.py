from flask import Flask, render_template, redirect, url_for
from mysql import get_players_info, update_vote


app = Flask(__name__)


@app.route('/')
def root():
    candidats = dict()
    players_info = get_players_info()

    for p in players_info:
        candidats[p[1]] = p[2]

    sortedDictWithValues = dict(sorted(candidats.items(), key=lambda x: x[1], reverse=True))
 
    return render_template('index.html', liste_candidat=sortedDictWithValues)


@app.route('/vote/<selected_player>', methods=['POST'])
def vote(selected_player):

    players_info = get_players_info()

    for p in players_info:
        if p[1] == selected_player:
            update_vote(selected_player, p[2])
    
    return redirect(url_for('root'))


@app.route('/players', methods=['POST'])
def players():

    candidats = dict()
    players_info = get_players_info()

    for p in players_info:
        candidats[p[1]] = p[2]

    sortedDictWithValues = dict(sorted(candidats.items(), key=lambda x: x[1], reverse=True))

    return render_template('player.html', liste_candidat=sortedDictWithValues)


@app.route('/reset', methods=['POST'])
def reset():
    players_info = get_players_info()
    for p in players_info:
        update_vote(p[1], -1)

    return redirect(url_for('root'))


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.

    app.run(host='127.0.0.1', port=8080, debug=True)
