'''
This is the backend server file for the final project
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    '''
    This function renders the index page of the app
    '''
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector_api():
    '''
    This function processes the input and returns the apropriate response
    '''
    text = request.args['textToAnalyze']
    result = emotion_detector(text)
    if not result['dominant_emotion']:
        return 'Invalid text! Please try again!'
    final_response = "For the given statement, the system response is 'anger': "
    final_response += result['anger']
    final_response += "'disgust': "
    final_response += result['disgust']
    final_response += "'fear': "
    final_response += result['fear']
    final_response += "'joy': "
    final_response += result['joy']
    final_response += "'sadness': "
    final_response += result['sadness']
    final_response += "The dominant emotion is "
    final_response += result['dominant_emotion']
    final_response += '.'
    return final_response

if __name__ == "__main__":
    app.run(debug=True)
