import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the pretrained model
model = models.mobilenet_v2(weights=None)
num_classes = 36  # Update with the number of classes in your model
model.classifier[1] = nn.Linear(model.last_channel, num_classes)
model.load_state_dict(torch.load('modelforclass.pth', map_location=torch.device('cpu')))
model.eval()