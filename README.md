# Multi-Modal AI System for Industrial Quality Assurance

A Seasons of Code (SoC) project building toward a multi-modal AI system for industrial quality assurance. This repo tracks my weekly learning progress and the foundational work leading up to the core project.

---

## Progress Log

### Week 1 — Python Basics

- Set up a Python development environment (Google Colab / Kaggle)
- Practiced core Python syntax: variables, data types, lists, dictionaries, loops, and functions
- Wrote and ran my first scripts to get comfortable with the basics
- Covered the theory behind Machine Learning as a primer for the weeks ahead

### Week 2 — Machine Learning Basics

- Studied core ML concepts up through Bagging (ensemble methods)
- Learned data handling and manipulation using **Pandas**
- Built intuition for how ML models are trained and evaluated

### Week 3 — Deep Learning & CNNs

- Studied the fundamentals of Deep Learning
- Learned how Convolutional Neural Networks (CNNs) work and why they're suited for image-based tasks — directly relevant to the visual inspection side of this project
- Worked through a structured video series on the topic

### Week 4 — Intro to LLMs

- Learned the basics of Large Language Models (LLMs)
- Covered how LLMs are trained and used in practice
- Began connecting LLM concepts to the "multi-modal" angle of the project (combining vision + language for QA tasks)

### Week 5 & 6 — Object Detection & YOLOv8

- Learned the fundamentals of object detection and how it differs from classification
- Studied the YOLO (You Only Look Once) architecture and its evolution up to YOLOv8
- Trained a custom YOLOv8 model on a steel surface defect dataset to detect defects such as scratches, patches, pitted surface, crazing, inclusion, and rolled-in scale
- Evaluated model performance using metrics like precision, recall, and mAP across defect classes

### Week 7 & 8 — LLM Integration & Deployment

- Built a Streamlit web application to serve as the front end for the QA system
- Integrated the trained YOLOv8 model into the app for real-time defect detection on uploaded images
- Learned to set up and run a local LLM using Ollama (Llama 3.2)
- Connected detected defect data to the local LLM to generate professional, structured inspection reports
- Combined detection and report generation into a single end-to-end application: **AI-Powered Industrial Quality Assurance System**
  - Upload a steel surface image
  - Detect defects using the trained YOLOv8 model
  - Display detected defects with bounding boxes
  - Send detected defects to Llama 3.2 (via Ollama) to generate an inspection report
  - Display the image, detections, and report together in a clean Streamlit interface
- Project code available in the `SOC app` folder, including setup instructions in its own README

---

## Tech Stack

| Category             | Technologies                                                      |
| -------------------- | ----------------------------------------------------------------- |
| Programming Language | Python                                                            |
| Environment          | Google Colab / Kaggle Notebooks                                   |
| Data Processing      | Pandas, NumPy                                                     |
| Visualization        | Matplotlib, Seaborn                                               |
| Classical ML         | Scikit-learn (Logistic Regression, Decision Trees, Bagging, etc.) |
| Deep Learning        | TensorFlow / Keras (CNNs)                                         |
| Object Detection     | YOLOv8 (Ultralytics)                                               |
| LLM / Local Inference | Ollama, Llama 3.2                                                 |
| Web App Framework    | Streamlit                                                          |
| Version Control      | Git & GitHub                                                      |
| Future Modalities    | Image data + Sensor/Tabular data fusion                           |

---

## Notes

This repo is updated weekly as part of an ongoing SoC mentorship project. Weeks 1-4 focus on foundational skills (Python, ML, DL, LLMs); Weeks 5 onward build toward the actual multi-modal AI system for industrial quality assurance, culminating in a working end-to-end application in Weeks 7 & 8.
