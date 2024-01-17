from ultralytics import settings

# Update a setting
settings.update({
    'datasets_dir': 'C:/Users/USER/yolov8/train_exd_yolo',
    'runs_dir': 'C:/Users/USER/yolov8/yolov8-seg/runs',
    'tensorboard': True,
})

# Reset settings to default values
# settings.reset()