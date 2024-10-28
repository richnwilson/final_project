import requests
import json

'''
Function to predict emotion using Watson NLP library
'''
def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": { "text" : text_to_analyze}}
    response = requests.post(url, json = myobj, headers=headers)
    # Error handling
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotions = formatted_response["emotionPredictions"][0]["emotion"]
        score = 0.0
        dominant_emotion = "none"
        for k, v in emotions.items():
            if v > score:
                score = v
                dominant_emotion = k
        emotions["dominant_emotion"] = dominant_emotion
        return emotions
    elif response.status_code == 400: 
        return { 'joy': None, 
                'anger': None, 
                'disgust': None, 
                'sadness': None, 
                'fear': None, 
                'dominant_emotion': None
                }
                