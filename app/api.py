# api.py
import flask
from flask_cors import CORS, cross_origin
import app.database

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['CORS_HEADERS'] = 'Content-Type'

CORS(app)


@app.route('/records', methods=['get'])
@cross_origin()
def getRecords():
    return app.database.getRecords()


@app.route('/record/new', methods=['POST'])
@cross_origin()
def newRecord():
    return app.database.newRecord()


if __name__ == "__main__":
    app.run()
