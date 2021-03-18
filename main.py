from flask import Flask, render_template, request
from source import Minesweeper

app = Flask(__name__)
app.secret_key = 'this is a secret key'


game = Minesweeper('medium')


@app.route('/')
def index():
    game.change_difficulty('medium')
    rows = columns = game.play_field()
    game.set_indicators()
    return render_template('index.html',
                           rows=rows, columns=columns,
                           difficulty='medium',
                           num_of_flags=game.mines,
                           mine_locations=game.mine_locations,
                           ind_locations=game.ind_location,
                           ind_number=game.ind_number,
                           revealed_tiles=game.revealed_tiles)


@app.route('/', methods=['POST', 'GET'])
def form_post():
    # TODO: render template partially
    if request.method == 'POST':
        keys = []
        for key in request.form.keys():
            keys.append(key)
        if 'difficulty' in keys:
            game.change_difficulty(request.form['difficulty'])
            rows = columns = game.play_field()
            game.set_indicators()
            return render_template('index.html',
                                   rows=rows,
                                   columns=columns,
                                   difficulty=game.difficulty,
                                   num_of_flags=game.flags,
                                   mine_locations=game.mine_locations,
                                   ind_locations=game.ind_location,
                                   ind_number=game.ind_number,
                                   revealed_tiles=game.revealed_tiles)
        if 'tile' in keys:
            tile = request.form['tile']
            location = [int(x) for x in tile.split()]
            # print(location)
            game.reveal_tiles(location[0], location[1])
            return render_template('index.html',
                                   rows=game.play_field(),
                                   columns=game.play_field(),
                                   difficulty=game.difficulty,
                                   num_of_flags=game.flags,
                                   mine_locations=game.mine_locations,
                                   ind_locations=game.ind_location,
                                   ind_number=game.ind_number,
                                   revealed_tiles=game.revealed_tiles)
            # return '', 204  # HTTP empty response
