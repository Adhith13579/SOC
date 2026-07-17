# train.py
# YOLOv8 training script for NEU-YOLO steel surface defect detection
# Run this script once per model variant by changing MODEL_SIZE below.
# Trained on Google Colab with T4 GPU.

from ultralytics import YOLO

# --------------------------------------------------
# Configuration
# Change MODEL_SIZE to: "n", "s", "m", or "l"
# --------------------------------------------------
MODEL_SIZE = "n"

DATASET_YAML  = "data.yaml"    # path to NEU-YOLO dataset config
EPOCHS        = 50
IMAGE_SIZE    = 640            # standard YOLOv8 input size (upscaled from 200px originals)
BATCH_SIZE    = 16
WORKERS       = 2
PROJECT       = "neu_defect_detection"
RUN_NAME      = f"yolov8{MODEL_SIZE}_neu"

def main():
    model = YOLO(f"yolov8{MODEL_SIZE}.pt")

    results = model.train(
        data      = DATASET_YAML,
        epochs    = EPOCHS,
        imgsz     = IMAGE_SIZE,
        batch     = BATCH_SIZE,
        workers   = WORKERS,
        project   = PROJECT,
        name      = RUN_NAME,
        patience  = 15,        # early stopping if no improvement for 15 epochs
        save      = True,
        plots     = True,
    )

    print(f"\nTraining complete for YOLOv8{MODEL_SIZE.upper()}")
    print(f"Results saved to: {PROJECT}/{RUN_NAME}")

    # Run validation on the best saved weights
    best_model = YOLO(f"{PROJECT}/{RUN_NAME}/weights/best.pt")
    val_results = best_model.val(data=DATASET_YAML, imgsz=IMAGE_SIZE)

    print(f"\nValidation Results:")
    print(f"  mAP@0.5      : {val_results.box.map50:.4f}")
    print(f"  mAP@0.5:0.95 : {val_results.box.map:.4f}")
    print(f"  Precision    : {val_results.box.mp:.4f}")
    print(f"  Recall       : {val_results.box.mr:.4f}")


if __name__ == "__main__":
    main()
