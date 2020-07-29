"""Every Third Letter /test POST route
If you don’t have a current code sample you can share, please write a small web application 
in one of the above languages (Python/Ruby/Node). The application only needs to do the following:
Accept a POST request to the route “/test”, which accepts one argument “string_to_cut”
Return a JSON object with the key “return_string” and a string containing every third letter from the original string
(e.g.) If you POST {"string_to_cut": "iamyourlyftdriver"}, it will return: {"return_string": "muydv"}.
   
Note: To see expected behavior you can test against a current working example with the command: 
curl -X POST https://lyft-interview-test.glitch.me/test --data '{"string_to_cut": "iamyourlyftdriver"}' -H 'Content-Type: application/json'    
"""

from flask import (Flask, request, jsonify)
from every_third_ltr import make_every_third_str

app = Flask(__name__)

app.secret_key = "dsdfghdjfytrewqetyui8767564534qweasdf"


@app.route("/test", methods=['POST'])
def test():

    string_to_cut = request.get_json()

    return jsonify(make_every_third_str(string_to_cut))
  


if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0', port='5000')