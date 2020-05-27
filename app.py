from flask import Flask, render_template, session
from Logic.Band import Band


app = Flask(__name__)
app.secret_key = 'This-is-a-real-secret-key'
b = Band()
tuneBand = b.tuneBand()
playBand = b.playBand()


@app.route('/Mariachi')
def index():
    assignedBandL = session['Band']
    tuneBandL = tuneBand
    return render_template('Mariachi.htm', assignedBand=assignedBandL, tuneBand=tuneBandL)


@app.route('/')
def prueba():
    session['Band'] = b.assignBand()
    return render_template('Index.htm')


@app.route('/Play')
def play():
    assignedBandL = session['Band']
    playBandL = playBand
    return render_template('playBand.htm', assignedBand=assignedBandL, playBand=playBandL)


if __name__ == "__main__":
    app.run(debug=True)
