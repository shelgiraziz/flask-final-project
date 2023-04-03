from flask import Flask, jsonify
from pymongo import MongoClient
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


client = MongoClient("mongodb+srv://200543203:1234@programmingfinalproject.hojfgf1.mongodb.net/WorldCupDatabase?retryWrites=true&w=majority")
db = client["WorldCupDatabase"]
matches_col = db['matches']

@app.route('/', methods=['GET'])
def teams_goals():
    teams = {}
    matches = matches_col.find({})
    for match in matches:
        home_team = match['home_team']
        away_team = match['away_team']
        home_goals = match['home_score']
        away_goals = match['away_score']
        if home_team not in teams:
            teams[home_team] = 0
        if away_team not in teams:
            teams[away_team] = 0
        teams[home_team] += home_goals
        teams[away_team] += away_goals
    return jsonify(teams)
    
if __name__ == '__main__':
    app.run(debug=True)
