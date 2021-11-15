import random
import json
import torch
import csv

from flask import flash

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
from datetime import timedelta, datetime

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as f:
    intents = json.load(f)
FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state= data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

# Implementing Bot Response Function


def bot(msg):
    sentence = msg

    sentence = tokenize(sentence)
    x = bag_of_words(sentence, all_words)
    x = x.reshape(1, x.shape[0])
    x = torch.from_numpy(x)

    output = model(x)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > .75:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                x = random.choice(intent["responses"])
                return x
    else:
        default = 'I do not understand your question?'
        data2 = msg
        with open('unanswered_questions.json', 'a', encoding='utf-8') as f:
            f.write(json.dumps(data2))
            f.write(",\n")
            f.close()
        return default



