emotions = {'anger': 0.041475996, 'disgust': 0.03486519, 'fear': 0.33066088, 'joy': 0.21811303, 'sadness': 0.117747515}
score = 0.0
dominant_emotion = "none"
for k, v in emotions.items():
    if v > score:
        score = v
        dominant_emotion = k
# print(score)
# print(dominant_emotion)


emotions = {'anger': 0.041475996, 'disgust': 0.03486519, 'fear': 0.33066088, 'joy': 0.21811303, 'sadness': 0.117747515}
for k in emotions.keys():
    emotions[k] = None
print(emotions)