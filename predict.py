from ultralytics import YOLO

# Load a model
model = YOLO('./runs/segment/train4/weights/best.onnx')  # load an official model
# model = YOLO('path/to/best.pt')  # load a custom model

# Predict with the model
results = model("/home/avs/dataset/train_exd_yolo/EVT_20230715_112856_F_trim/00001.jpg", save=True)  # predict on an image