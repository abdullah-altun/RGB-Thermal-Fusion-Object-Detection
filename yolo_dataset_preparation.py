import os
import shutil

# Paths for RGB and thermal images
rgb_image_dir = 'dataset/M3FD_Detection/Vis'  # RGB images directory
thermal_image_dir = 'dataset/M3FD_Detection/Ir'  # Thermal images directory

# Labels directories
rgb_label_dir = 'dataset/M3FD_Detection/labels'  # RGB labels directory
thermal_label_dir = 'dataset/M3FD_Detection/labels'  # Thermal labels directory

# Output dataset directories
output_rgb_dir = 'dataset/M3FD_Detection/RGB'
output_thermal_dir = 'dataset/M3FD_Detection/Thermal'

# Text files containing image names
train_file = 'dataset/M3FD_Detection/meta/train.txt'
val_file = 'dataset/M3FD_Detection/meta/val.txt'
pred_file = 'dataset/M3FD_Detection/meta/pred.txt'

# YOLOv8 dataset structure
subdirs = ['train', 'val', 'test']
subfolders = ['images', 'labels']

# Ensure YOLOv8 directory structure exists
def create_yolo_structure(base_dir):
    for subdir in subdirs:
        for folder in subfolders:
            os.makedirs(os.path.join(base_dir, subdir, folder), exist_ok=True)

create_yolo_structure(output_rgb_dir)
create_yolo_structure(output_thermal_dir)

# Function to copy images and labels
def prepare_dataset(image_list_file, source_image_dir, source_label_dir, output_dir, split):
    with open(image_list_file, 'r') as f:
        image_names = [line.strip() for line in f.readlines()]
        for image_name in image_names:
            # Copy images
            src_image_path = os.path.join(source_image_dir, image_name)
            dest_image_path = os.path.join(output_dir, split, 'images', image_name)

            # Copy labels
            label_name = os.path.splitext(image_name)[0] + '.txt'
            src_label_path = os.path.join(source_label_dir, label_name)
            dest_label_path = os.path.join(output_dir, split, 'labels', label_name)

            if os.path.exists(src_image_path):
                shutil.copy(src_image_path, dest_image_path)
            else:
                print(f"Warning: {src_image_path} does not exist and will be skipped.")

            if os.path.exists(src_label_path):
                shutil.copy(src_label_path, dest_label_path)
            else:
                print(f"Warning: {src_label_path} does not exist and will be skipped.")

# Prepare RGB dataset
prepare_dataset(train_file, rgb_image_dir, rgb_label_dir, output_rgb_dir, 'train')
prepare_dataset(val_file, rgb_image_dir, rgb_label_dir, output_rgb_dir, 'val')
prepare_dataset(pred_file, rgb_image_dir, rgb_label_dir, output_rgb_dir, 'test')

# Prepare Thermal dataset
prepare_dataset(train_file, thermal_image_dir, thermal_label_dir, output_thermal_dir, 'train')
prepare_dataset(val_file, thermal_image_dir, thermal_label_dir, output_thermal_dir, 'val')
prepare_dataset(pred_file, thermal_image_dir, thermal_label_dir, output_thermal_dir, 'test')

# Create YAML file for YOLOv8
yaml_content_rgb = f"""train: {os.path.join(output_rgb_dir, 'train', 'images')}
val: {os.path.join(output_rgb_dir, 'val', 'images')}
test: {os.path.join(output_rgb_dir, 'test', 'images')}

nc: 2
names: [Person,Car]
"""

yaml_content_thermal = f"""train: {os.path.join(output_thermal_dir, 'train', 'images')}
val: {os.path.join(output_thermal_dir, 'val', 'images')}
test: {os.path.join(output_thermal_dir, 'test', 'images')}

nc: 2
names: [Person,Car]
"""

with open(os.path.join('config/RGB_dataset.yaml'), 'w') as f:
    f.write(yaml_content_rgb)

with open(os.path.join('config/Thermal_dataset.yaml'), 'w') as f:
    f.write(yaml_content_thermal)

print("YOLOv8 dataset preparation complete.")
