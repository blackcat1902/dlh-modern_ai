#!/usr/bin/env python3
"""Computer Vision Applications.
This module provides tools and functions for object detection, image
segmentation, and dataset preprocessing using modern deep learning frameworks.
"""
from ultralytics import YOLO
from ultralytics.utils import YAML


def tune_hyperparameters():
    """Executes hyperparameter tuning and trains a
    final YOLO model from the best checkpoint."""

    data = "datasets/detection/data.yaml"
    tune_dir = "runs/detect/tune"
    total_epochs = 150

    # Phase 1: quick trials to find good hyperparameters.
    tuner_model = YOLO("yolov8n.pt")
    tuner_model.tune(data=data, iterations=15, epochs=10, plots=False)

    # tune_dir is a guess, not an order. YOLO decided this path on
    # its own.
    best_hyp = YAML.load(f"{tune_dir}/best_hyperparameters.yaml")
    best_checkpoint = f"{tune_dir}/weights/best.pt"

    # The tuner writes every value as a float, but close_mosaic must
    # be a whole int or model.train() rejects it.
    if "close_mosaic" in best_hyp:
        best_hyp["close_mosaic"] = int(best_hyp["close_mosaic"])

    # Phase 2: continue the winning trial with its own settings,
    final_model = YOLO(best_checkpoint)
    final_model.train(
        data=data,
        epochs=total_epochs - 10,
        patience=20,
        **best_hyp)

    final_model.save("best_model.pt")
    