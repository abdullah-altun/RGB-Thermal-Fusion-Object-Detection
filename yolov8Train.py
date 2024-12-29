from ultralytics import YOLO

model = YOLO('yolov8x.yaml') 

model.train(
    data='config/RGB_dataset.yaml', 
    epochs=100,
    batch=28,
    imgsz=640, 
    device=0, 
    name='RGB_yolov8x',  
    optimizer='Adam',
    verbose=True 
)