# 💊 CNN-Based Medicine Classification Web App

## 🧠 Project Overview

This project introduces a **CNN-driven image classification system** for medicine recognition based on packaging or pill images. It is integrated with **voice guidance**, ensuring accessibility for visually impaired or non-literate users.

The system enables quick and accurate medicine identification using **Convolutional Neural Networks (CNNs)** and speaks out the medicine's name and details, enhancing healthcare accessibility and user-friendliness.

> 🎉 **Published in Springer!**  
> 📘 *CNN–Driven Voice Guidance: Image Based Medicine Recognition*  
> 🗓️ *Conference Paper, Business Intelligence and Data Analytics (BIDA 2024)*  
> 🔗 [Springer Link](https://link.springer.com/chapter/10.1007/978-981-97-7717-4_27)  
> 📅 First Online: 25 February 2025  
> 📖 Series: *Smart Innovation, Systems and Technologies (SIST, Volume 413)*  
> 📊 Accuracy Achieved: **96.22%**

---

## ⚙️ Features

- 📸 Upload an image of a medicine
- 🧠 CNN-based model processes the image
- 🔊 Audio output describing the identified medicine
- 👤 Accessible to users with low literacy or visual impairments

---

## 🧰 Tech Stack

| Layer        | Technology         |
|--------------|--------------------|
| Backend      | Flask (Python)     |
| Frontend     | HTML, CSS          |
| Deep Learning| TensorFlow / Keras |
| Model Type   | Convolutional Neural Network (CNN) |
| Voice Output | gTTS (Google Text-to-Speech) |
| Database     | Local Filesystem   |

---

## 📁 Folder Structure

```bash
├── app.py                          # Main Flask application
├── dataset/                        # Image dataset used for training
├── model/                          # Saved trained CNN model
├── medicine_classification_doc.pdf# Project documentation
├── epics_poster[1].docx           # Conference poster
└── README.md                      # This file
```
## 📊 Results

- ✅ **Accuracy**: 96.22%
- 📉 **Error Rate**: Very low misclassification observed
- ⚡ **Speed**: Image classification completed in under 1 second
- 🔍 **Robustness**: Tested against varied lighting and orientation conditions
- 📈 **Deployment-ready**: Easily portable for mobile/web-based applications

## 🗣️ Voice Interface

The system integrates **Google Text-to-Speech (gTTS)** to announce the recognized medicine. This adds a powerful layer of accessibility:

- 👓 **Visually impaired** users can hear the medicine name
- 🧓 **Elderly users** can operate without needing to read screens
- 🚫 **Non-literate users** can benefit from spoken output
- 🎧 **Hands-free operation** for safer use in medical environments

## 👩‍💻 Authors

- **Ravi Kishan Surapaneni**
- **Jadam Aruna Bharathi**
- **Durgempudi Divya**

*Affiliated with the International Conference on Business Intelligence and Data Analytics (BIDA 2024).*
