# database.py
from pymongo import MongoClient
from dotenv import load_dotenv
from progress.bar import ChargingBar
import os

load_dotenv()

client = MongoClient(os.environ.get("MONGODB_CONNECTION_STRING"))

# database: tracker
# collection: weight


def saveRecords(records):
    bar = ChargingBar('Saving records', max=len(records))
    for record in records:
        client.tracker.weight.update_one({"_id": record['date']},
                                         {"$set":
                                          {
                                              "date": record["date"],
                                              "weight": record["weight"]
                                          }
                                          }, upsert=True)
        bar.next()
    bar.finish()
    return {'message': 'Records saved correctly.', 'data': records}


def newRecord(record):
    client.tracker.weight.update_one({"_id": record['date']},
                                     {"$set":
                                      {
                                          "date": record["date"],
                                          "weight": record["weight"]
                                      }
                                      }, upsert=True)
    return {'message': 'Record saved correctly.', 'data': record}


def getRecords():
    records = []
    for r in client.tracker.weight.find():
        records.append(r)
    return {'records': records}


if __name__ == "__main__":
    # record = {
    #     "date": "26/02/2021",
    #     "weight": 76.2
    # }
    # print(newRecord(record))
    for r in getRecords()['records']:
        print(r)
