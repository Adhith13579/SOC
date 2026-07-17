# Week 6: CV Model - Steel Surface Defect Detection

## Goals
- Train a YOLOv8 object detection model on the NEU-YOLO steel surface defect dataset
- Experiment with four model scales: nano, small, medium, and large
- Compare performance and efficiency trade-offs across model sizes
- Identify the best model for the task

## Dataset
**NEU-YOLO** (Kaggle) - Northeast University Surface Defect Database, formatted for YOLO

- 1,800 total images (200 x 200 px, grayscale steel surface photos)
- 80/20 train/val split: 1,440 training, 360 validation images
- 6 defect classes:
  - Crazing (Cr)
  - Inclusion (In)
  - Patches (Pa)
  - Pitted Surface (Ps)
  - Rolled-in Scale (Rs)
  - Scratches (Sc)

## Models Trained
All four YOLOv8 variants were trained for 50 epochs on the same dataset and hardware.

| Model      | Params (M) | mAP@0.5 | mAP@0.5:0.95 | Precision | Recall | Inference (ms) |
|------------|------------|---------|--------------|-----------|--------|----------------|
| YOLOv8n    | 3.0        | 73.6%   | 40.1%        | 69.1%     | 69.4%  | 2.1            |
| YOLOv8s    | 11.2       | 73.3%   | 39.1%        | 68.5%     | 65.3%  | ~4.0           |
| YOLOv8m    | 25.9       | 73.2%   | 39.1%        | 69.9%     | 65.3%  | 9.7            |
| YOLOv8l    | 43.6       | 74.1%   | 40.2%        | 67.5%     | 67.2%  | 15.8           |

## Results Summary

The most striking finding is how **narrow the mAP gap is across all four model sizes** -- just 0.9 percentage points separates nano from large. This is consistent with published benchmarks on NEU-DET and suggests that model capacity is not the primary bottleneck for this task at this dataset size.

### Best Overall Accuracy: YOLOv8l
- Highest mAP@0.5 at 74.1% and mAP@0.5:0.95 at 40.2%
- But at 43.6M parameters and 15.8ms inference, the gain over nano is marginal

### Best Efficiency: YOLOv8n
- mAP@0.5 of 73.6% -- only 0.5pp below the large model
- 2.1ms inference time, 3.0M parameters
- **Selected as the final model** given the negligible accuracy trade-off and the significant speed advantage

### Observations on the Dataset
- All models struggled most with **Crazing** -- the defect pattern is fine and distributed across the entire surface, making bounding box localisation inherently ambiguous
- **Inclusion** and **Scratches** had the highest per-class AP across all model sizes, likely because they produce more distinct, localised features
- The 200x200px image size limits the fine detail available to larger models, which likely explains why scaling up produces so little gain

## Files
- [`train.py`](./train.py) - Training script used for all four model variants
- [`results_analysis.py`](./results_analysis.py) - Loads and compares results across all runs
- [`notes_yolov8.md`](./notes_yolov8.md) - Notes on YOLOv8 architecture and concepts

## Model & Full Results
Training weights, confusion matrices, and per-class AP plots are saved to Google Drive:
https://drive.google.com/drive/folders/1i2AL0Av-dXgCexrboLawckjGU4tRicYR?usp=sharing
