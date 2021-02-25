# api.py
import flask
from flask_cors import CORS, cross_origin
from app.database import getRecords, newRecord

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['CORS_HEADERS'] = 'Content-Type'

CORS(app)


@app.route('/records', methods=['get'])
@cross_origin()
def GetRecords():
    return app.database.getRecords()


@app.route('/record/new', methods=['POST'])
@cross_origin()
def NewRecord():
    return app.database.newRecord()


if __name__ == "__main__":
    app.run()
