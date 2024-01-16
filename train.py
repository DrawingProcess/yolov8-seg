from ultralytics import YOLO

# Load a model
# model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("yolov8n-seg.pt")  # load a pretrained model (recommended for training)

# Use the model
model.train(data="./data.yaml", epochs=2000)  # train the model
metrics = model.val()  # evaluate model performance on the validation set
# results = model("/home/avs/dataset/train_exd_yolo/EVT_20230715_112856_F_trim/00001.jpg")  # predict on an image
path = model.export(format="onnx")  # export the model to ONNX format