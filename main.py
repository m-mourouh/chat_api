import os
import json
from flask import Flask ,request , jsonify
from bardapi import Bard
from dotenv import load_dotenv, dotenv_values
load_dotenv()
os.environ['_BARD_API_KEY']= os.getenv('BARD_API_KEY')

app = Flask(__name__) 

@app.route("/chat",methods=['POST'])
def chat():
    data = {}
    input_text = request.json.get("input_text")
    if input_text:
        response = Bard().get_answer(str(input_text))
        if(response):
            for key, value in response.items():
                data.update({key: value})
            print(data)
        return jsonify({
            'content' : response['content'],
            'conversation_id': response['conversation_id'],
            'response_id': response['response_id'],
            'factualityQueries': response['factualityQueries'],
            'textQuery': response['textQuery'],
            'choices': response['choices'],
            'links': response['links'],
            'code': response['code'],
             })

    return jsonify({'error' : "Something went wrong"})

if __name__ == "__main__":
    app.run(debug = True)
