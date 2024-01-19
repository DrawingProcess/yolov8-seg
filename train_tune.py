from ultralytics import YOLO

# Load a model
# model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("yolov8n-seg.pt")  # load a pretrained model (recommended for training)

# Use the model
model.tune(data='./data.yaml', epochs=300,  iterations=1, plots=True, save=True, val=True)