import os
import random
import xml.etree.ElementTree as ET

# Directory paths
image_dir = 'dataset/M3FD_Detection/Vis'  # Directory containing images
xml_dir = 'dataset/M3FD_Detection/Annotation/'  # Directory containing XML files
output_dir = 'dataset/M3FD_Detection/yolo_labels/'  # Directory to save YOLO format files
outputPath = 'dataset/M3FD_Detection/meta/'  # Directory to save split meta files

# Ensure necessary directories exist
os.makedirs(output_dir, exist_ok=True)
os.makedirs(outputPath, exist_ok=True)

# Output files for splits
train_file = f'{outputPath}/train.txt'
val_file = f'{outputPath}/val.txt'
pred_file = f'{outputPath}/pred.txt'

# Split ratios
train_ratio = 0.7
val_ratio = 0.15
pred_ratio = 0.15

# Get all image filenames
all_images = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]

# Shuffle the images
random.shuffle(all_images)

# Calculate split indices
num_images = len(all_images)
train_end = int(num_images * train_ratio)
val_end = train_end + int(num_images * val_ratio)

# Split the images
train_images = all_images[:train_end]
val_images = all_images[train_end:val_end]
pred_images = all_images[val_end:]

# Function to write filenames to respective files
def write_to_file(file_path, images):
    with open(file_path, 'w') as f:
        for image in images:
            f.write(f"{image}\n")

write_to_file(train_file, train_images)
write_to_file(val_file, val_images)
write_to_file(pred_file, pred_images)

print(f"Train, validation, and prediction files created: {train_file}, {val_file}, {pred_file}")

# Function to convert bounding box to YOLO format
def convert_to_yolo_format(xmin, ymin, xmax, ymax, img_width, img_height):
    x_center = (xmin + xmax) / 2 / img_width
    y_center = (ymin + ymax) / 2 / img_height
    width = (xmax - xmin) / img_width
    height = (ymax - ymin) / img_height
    return x_center, y_center, width, height

# Label mapping (adjust as necessary)
label_mapping = {
    'People': 0,
    'Car': 1
}

# Process each XML file in the directory
for xml_file in os.listdir(xml_dir):
    if xml_file.endswith('.xml'):
        file_path = os.path.join(xml_dir, xml_file)
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Extract size information
        size = root.find('size')
        image_width = int(size.find('width').text)
        image_height = int(size.find('height').text)

        # Prepare YOLO format lines
        yolo_lines = []
        for obj in root.findall('object'):
            name = obj.find('name').text
            if name in label_mapping:
                class_id = label_mapping[name]
                bndbox = obj.find('bndbox')
                xmin = int(bndbox.find('xmin').text)
                ymin = int(bndbox.find('ymin').text)
                xmax = int(bndbox.find('xmax').text)
                ymax = int(bndbox.find('ymax').text)
                x_center, y_center, width, height = convert_to_yolo_format(xmin, ymin, xmax, ymax, image_width, image_height)
                yolo_lines.append(f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}")

        # Save to YOLO format text file
        output_file_name = os.path.splitext(xml_file)[0] + '.txt'
        output_file_path = os.path.join(output_dir, output_file_name)
        with open(output_file_path, 'w') as f:
            f.write("\n".join(yolo_lines))

        print(f"Processed {xml_file} and saved to {output_file_path}")
