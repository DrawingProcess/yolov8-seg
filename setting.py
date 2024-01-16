from ultralytics import settings

# Update a setting
settings.update({
    'datasets_dir': '/home/avs/dataset',
    'runs_dir': '/home/avs/yolov8/runs',
    'tensorboard': True,
})

# Reset settings to default values
# settings.reset()