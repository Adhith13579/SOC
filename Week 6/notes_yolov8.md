# YOLOv8 Architecture and Concepts - Notes

## What is YOLO?
YOLO (You Only Look Once) is a family of real-time object detection models. Unlike two-stage detectors (like Faster R-CNN) that first propose regions and then classify them, YOLO processes the entire image in a single forward pass -- hence the name. This makes it significantly faster while remaining competitive in accuracy.

YOLOv8, released by Ultralytics in 2023, is currently one of the most widely used versions for real-world deployment.

## YOLOv8 Architecture Overview

### Backbone (Feature Extraction)
The backbone is responsible for extracting feature representations from the input image. YOLOv8 uses a modified CSPDarknet with C2f (Cross Stage Partial with 2 bottleneck blocks) modules. The backbone outputs feature maps at multiple scales, which is important for detecting objects of different sizes.

### Neck (Feature Pyramid Network)
The neck aggregates features from different backbone stages into a unified multi-scale representation. YOLOv8 uses a PAN-FPN (Path Aggregation Network - Feature Pyramid Network) structure, which combines:
- Top-down pathway: passes high-level semantic information to smaller-scale feature maps
- Bottom-up pathway: passes low-level spatial information back up

This helps the model detect both large and small objects effectively.

### Head (Detection)
YOLOv8 uses an anchor-free, decoupled head -- a shift from earlier YOLO versions which used anchor boxes. The head outputs:
- Bounding box coordinates (x, y, w, h)
- Objectness/class probability scores

Decoupling the classification and regression branches (separate sub-heads for each) generally improves accuracy.

## Model Scale Variants
All four variants share the same architecture but differ in depth and width (number of layers and channels):

| Model   | Depth mult. | Width mult. | Params (M) | Use case |
|---------|-------------|-------------|------------|----------|
| YOLOv8n | 0.33        | 0.25        | 3.0        | Edge/mobile deployment |
| YOLOv8s | 0.33        | 0.50        | 11.2       | Balanced speed/accuracy |
| YOLOv8m | 0.67        | 0.75        | 25.9       | Higher accuracy, moderate speed |
| YOLOv8l | 1.00        | 1.00        | 43.6       | Best accuracy, slower inference |

## Key Metrics

### mAP@0.5
Mean Average Precision at an IoU (Intersection over Union) threshold of 0.5. A predicted box is counted as correct if it overlaps with the ground truth box by at least 50%. This is the most commonly reported metric for object detection.

### mAP@0.5:0.95
The same metric averaged across IoU thresholds from 0.5 to 0.95 in steps of 0.05. This is a stricter metric that rewards better localisation, not just rough overlap. It is the primary metric used in COCO benchmarks.

### Precision
Of all the bounding boxes the model predicted, what fraction were actually correct? High precision = few false positives.

### Recall
Of all the actual defects in the images, what fraction did the model successfully find? High recall = few false negatives (missed defects).

### IoU (Intersection over Union)
A measure of how well a predicted bounding box overlaps with the ground truth box:
IoU = (area of overlap) / (area of union)
IoU of 1.0 means a perfect match; 0 means no overlap at all.

## Training Details Used This Week
- Pre-trained weights: COCO-pretrained YOLOv8 checkpoints (transfer learning)
- Image size: 640x640 (upscaled from the original 200x200 NEU images)
- Epochs: 50
- Batch size: 16
- Early stopping: patience of 15 epochs
- Hardware: Google Colab T4 GPU

## Why Transfer Learning?
The YOLOv8 weights pre-trained on COCO are a strong starting point -- the backbone has already learned general visual features (edges, textures, shapes) that are useful for any detection task. Fine-tuning on NEU-YOLO allows the model to adapt those general features specifically to steel surface defect patterns in far fewer epochs than training from scratch would require.

## Key Takeaway for This Dataset
The NEU-DET dataset is relatively small (1,800 images, 6 classes, 300 images per class) and the images are low resolution (200x200 px). In this regime, model capacity is not the bottleneck -- even the nano model has more than enough capacity to fit the data. The more meaningful challenge is the visual similarity between some defect classes (particularly Crazing vs. Patches) and the ambiguity of bounding box localisation for diffuse surface patterns like Crazing.
