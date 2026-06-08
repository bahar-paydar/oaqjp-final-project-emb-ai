from flask import Flask, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector(request):
    text = request.args['textToAnalyze']
    result = emotion_detector(text)
    return f"For the given statement, the system response is 'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}. The dominant emotion is {result[dominant_emotion]}."
    
if __name__ == "__main__":
    app.run(debug=True)