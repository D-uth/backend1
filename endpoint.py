from flask import Flask, request, jsonify
import datetime
import pytz
import os
from collections import OrderedDict

app = Flask(__name__)

@app.route('/get_info', methods=['GET'])
def get_info():
    #query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    #github_file_url = request.args.get('github_file_url')
    #github_source_url = request.args.get('github_source_url')

    # Validate parameters
    if not slack_name or not track:
        return jsonify({"error": "All parameters (slack_name, track) are required."}), 400

    # Get current day of the week
    current_day = datetime.datetime.now(pytz.UTC).strftime('%A')

    # Get current UTC time with validation of +/-2 minutes
    allowed_time_difference_minutes = 2
    utc_time = datetime.datetime.now(pytz.UTC)
    current_utc_time = datetime.datetime.now(pytz.UTC)
    time_difference_minutes = (current_utc_time - utc_time).total_seconds() / 60
    if abs(time_difference_minutes)> allowed_time_difference_minutes:
        return jsonify({"error": "Invalid UTC time, outside the allowed time difference."}), 400

    #Format the UTC_time in ISO 8601 format with 'Z' for UTC
    #formatted_utc_time = current_utc_time.strftime('%Y-%m-%dT%H:%M:%SZ')

    # Construct the response JSON
    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_utc_time.strftime('%Y-%m-%dT%H:%M:%SZ'),
        "track": track,
        "github_file_url": "https://github.com/D-uth/backend1/blob/main/endpoint.py",
        "github_repo_url": "https://github.com/D-uth/backend1",
        "status_code": "200"
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
