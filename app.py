from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://200543203:1234@programmingfinalproject.hojfgf1.mongodb.net/WorldCupDatabase?retryWrites=true&w=majority")
db = client["WorldCupDatabase"]
matches_col = db['matches']

@app.route('/', methods=['GET'])
def get_matches():
    # retrieve all matches from MongoDB
    data = matches_col.find({})
    
    # convert data to list of dictionaries with specified schema
    json_data = []
    for item in data:
        match_data = {
            '_id': str(item['_id']),
            'match_id': item['match_id'],
            'match_date': item['match_date'],
            'kick_off': item['kick_off'],
            'home_team': item['home_team'],
            'away_team': item['away_team'],
            'home_score': item['home_score'],
            'away_score': item['away_score'],
            'match_week': item['match_week'],
            'competition_stage': item['competition_stage'],
            'stadium': item['stadium'],
            'referee': item['referee'],
            'home_managers': item['home_managers'],
            'away_managers': item['away_managers']
        }
        json_data.append(match_data)
    
    # return data as JSON response
    return jsonify(json_data)


    
if __name__ == '__main__':
    app.run(debug=True)
