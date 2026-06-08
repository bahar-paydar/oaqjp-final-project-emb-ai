import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(URL, json=data, headers=headers)
    emotions = json.loads(response.text)['emotionPredictions'][0]['emotion']
    emotions['dominant_emotion'] = max(emotions, key=emotions.get)

    return emotions