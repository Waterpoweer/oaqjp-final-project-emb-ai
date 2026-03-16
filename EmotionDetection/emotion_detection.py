import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    payload =  { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, headers= header, json = payload )

    if response.status_code == 400:
        return {
                "anger": None, 
                "disgust": None, 
                "fear": None, 
                "joy": None, 
                "sadness": None, 
                "dominant_emotion":None
                }
    else :
        dictionary = json.loads(response.text)

        dict_emotion = dictionary["emotionPredictions"][0]["emotion"]

        dict_dominant={"dominant_emotion": max(dict_emotion, key=dict_emotion.get)}

        dict_emotion.update(dict_dominant)    
        
        return dict_emotion

