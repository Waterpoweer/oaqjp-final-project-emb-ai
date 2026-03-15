from flask import Flask , render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/emotionDetector")
def Emotion_Detector():
    textToAnalyze = request.args.get("textToAnalyze")

    result = emotion_detector(textToAnalyze)
    
    dominant_emotion = result.pop("dominant_emotion")

    output = ", ".join([f'{e}: {s}' for e, s in result.items()])

    return f'For the given statement, the system response is  {output}. The dominant emotion is {dominant_emotion}.'

if __name__ == "__main__":
    app.run(debug= True, port=5000)

