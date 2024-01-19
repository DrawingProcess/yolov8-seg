from ultralytics import YOLO
import os
import os.path
import cv2

model_path = 'C:/Users/USER/yolov8/yolov8-seg/runs/segment/train5/weights/best.pt' # modify here to your directory path
model = YOLO(model_path) # load an official model

data_path = "C:/Users/USER/yolov8/train_exd_yolo/EVT_20230716_144940_F_trim/" # modify here to your directory path
#result_path = "C:/Users/USER/yolov8/train_exd_yolo_inference/EVT_20230715_112856_F_trim/" # modify here to your directory path

# Create the folder to save results if it does not exist
# if not os.path.exists(result_path):
#     os.makedirs(result_path)

# Get a list of all jpg files in the data_path
image_files = [data_path + f for f in os.listdir(data_path) if f.endswith('.jpg')]

# image_files = data_path + image_files

#YOLO makes automatically 'predict' folder in segment
results = model(image_files, save=True)

# # Process each image with the model
# for image_file in image_files:
#     # Construct the full path to the image file
#     image_path = os.path.join(data_path, image_file)

#     # Read the image using OpenCV
#     image = cv2.imread(image_path)

#     # Predict images with the model
#     results = model.predict(image)

#     # Save the results
#     save_path = os.path.join(result_path, image_file)
#     model.save_path(results, save_path)