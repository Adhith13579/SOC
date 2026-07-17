# results_analysis.py
# Compares YOLOv8 n / s / m / l results on the NEU-YOLO dataset.
# Prints a summary table and highlights the efficiency vs. accuracy trade-off.

# Results recorded after 50-epoch training runs on Google Colab T4 GPU.
# mAP figures are from the best.pt checkpoint evaluated on the validation split.

RESULTS = {
    "YOLOv8n": {
        "params_M":        3.0,
        "map50":           0.736,
        "map50_95":        0.401,
        "precision":       0.691,
        "recall":          0.694,
        "inference_ms":    2.1,
    },
    "YOLOv8s": {
        "params_M":        11.2,
        "map50":           0.733,
        "map50_95":        0.391,
        "precision":       0.685,
        "recall":          0.653,
        "inference_ms":    4.0,
    },
    "YOLOv8m": {
        "params_M":        25.9,
        "map50":           0.732,
        "map50_95":        0.391,
        "precision":       0.699,
        "recall":          0.653,
        "inference_ms":    9.7,
    },
    "YOLOv8l": {
        "params_M":        43.6,
        "map50":           0.741,
        "map50_95":        0.402,
        "precision":       0.675,
        "recall":          0.672,
        "inference_ms":    15.8,
    },
}

# Per-class AP@0.5 for the selected best model (YOLOv8l, highest overall mAP)
PER_CLASS_AP = {
    "Crazing":        0.68,
    "Inclusion":      0.79,
    "Patches":        0.74,
    "Pitted Surface": 0.72,
    "Rolled-in Scale":0.76,
    "Scratches":      0.78,
}


def print_comparison_table():
    header = f"{'Model':<12} {'Params(M)':>10} {'mAP@0.5':>9} {'mAP@0.5:0.95':>14} {'Precision':>11} {'Recall':>8} {'Infer(ms)':>11}"
    print(header)
    print("-" * len(header))
    for model, r in RESULTS.items():
        print(
            f"{model:<12}"
            f"{r['params_M']:>10.1f}"
            f"{r['map50']*100:>9.1f}%"
            f"{r['map50_95']*100:>13.1f}%"
            f"{r['precision']*100:>10.1f}%"
            f"{r['recall']*100:>8.1f}%"
            f"{r['inference_ms']:>10.1f}"
        )


def find_best(metric, higher_is_better=True):
    fn = max if higher_is_better else min
    return fn(RESULTS, key=lambda m: RESULTS[m][metric])


def print_per_class_ap():
    print(f"\n{'Class':<20} {'AP@0.5':>8}")
    print("-" * 30)
    for cls, ap in sorted(PER_CLASS_AP.items(), key=lambda x: -x[1]):
        print(f"{cls:<20} {ap*100:>7.1f}%")


def print_analysis():
    maps  = {m: r["map50"] for m, r in RESULTS.items()}
    gap   = (max(maps.values()) - min(maps.values())) * 100
    best  = find_best("map50")
    fastest = find_best("inference_ms", higher_is_better=False)

    print("\nKey Findings")
    print("-" * 50)
    print(f"  mAP@0.5 range across all models : {gap:.1f} pp")
    print(f"  Best overall accuracy            : {best} ({RESULTS[best]['map50']*100:.1f}% mAP@0.5)")
    print(f"  Fastest inference                : {fastest} ({RESULTS[fastest]['inference_ms']:.1f} ms)")
    print(
        f"\n  The {gap:.1f} pp mAP gap confirms model capacity is not "
        f"the bottleneck for this dataset.\n"
        f"  YOLOv8n is recommended: near-identical accuracy at {RESULTS['YOLOv8l']['inference_ms'] / RESULTS['YOLOv8n']['inference_ms']:.0f}x "
        f"the inference speed of YOLOv8l."
    )
    print(
        f"\n  Hardest class to detect: "
        f"{min(PER_CLASS_AP, key=PER_CLASS_AP.get)} "
        f"({min(PER_CLASS_AP.values())*100:.0f}% AP)"
    )
    print(
        f"  Easiest class to detect: "
        f"{max(PER_CLASS_AP, key=PER_CLASS_AP.get)} "
        f"({max(PER_CLASS_AP.values())*100:.0f}% AP)"
    )


if __name__ == "__main__":
    print("NEU-YOLO: YOLOv8 Model Comparison (50 epochs, val split)")
    print("=" * 80)
    print_comparison_table()
    print_per_class_ap()
    print_analysis()
