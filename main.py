import os
import torch
from PIL import Image
from torchvision.datasets import ImageFolder
import torchvision.transforms as transforms
import cv2
import datetime
import pyfirmata
import time

port = 'COM3'
board = pyfirmata.Arduino(port)


def get_default_device():
    """Pick GPU if available, else CPU"""
    if torch.cuda.is_available():
        return torch.device('cuda')
    else:
        return torch.device('cpu')


device = get_default_device()

# Initialize optimizer

model = torch.jit.load('model_new.pt', map_location=device)
model.eval()

data_dir = './dataset-resized'

classes = os.listdir(data_dir)
transformations = transforms.Compose([transforms.Resize((256, 256)), transforms.ToTensor()])

dataset = ImageFolder(data_dir, transform=transformations)
func2_running = False


def to_device(data, device):
    """Move tensor(s) to chosen device"""
    if isinstance(data, (list, tuple)):
        return [to_device(x, device) for x in data]
    return data.to(device, non_blocking=True)


def predict_image(img, model):
    # Convert to a batch of 1
    xb = to_device(img.unsqueeze(0), device)
    # Get predictions from model
    yb = model(xb)
    # Pick index with highest probability
    prob, preds = torch.max(yb, dim=1)
    # Retrieve the class label
    return dataset.classes[preds[0].item()]


def predict_external_image(image_name):
    try:
        image = Image.fromarray(image_name)
    except AttributeError:
        image = Image.open(image_name)
    example_image = transformations(image)
    answer = predict_image(example_image, model)
    print("The image resembles", answer + ".")
    if answer == "glass":
        pin = 3
    elif answer == "metal":
        pin = 4
    else:
        pin = None
    if pin is not None:
        board.digital[pin].mode = pyfirmata.SERVO
        for i in range(0, 180):
            board.digital[pin].write(i)
            time.sleep(0.015)


cap = cv2.VideoCapture(0)
wait = 0

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_AREA)
    cv2.imshow('Result', frame)
    c = cv2.waitKey(1)
    wait = wait + 100
    if c == ord("q"):
        break
    if wait == 20000 and not func2_running:
        dd = datetime.datetime.now()
        predict_external_image(frame)
        wait = 0
cap.release()
cv2.destroyAllWindows()
