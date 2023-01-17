# Trasher- smart sorting mechanism 

## Presented by Team Akira
![](https://github.com/NodiraTillayeva/AKIRA-Trasher/blob/main/model.png)

**Objective Statement:**
Not “trash” but “raw material” 

**Problem:**
Every year, Uzbekistan generates 9 million tons of municipal solid 
waste, and only 9% of it is recycled. While in many developed countries 
this index is up to 50%. 

* Low level of recycling 
* Emission of harmful gases at the sites of landfills 
* Unpreparedness population to sort garbage 

**Objectives:**
 After researching the problem, we established our goals: 
* Qualitatively separate recyclable waste 
* Reducing the area of polygons 
* Teaching the population to sort their waste

**Solution:**
We decided to develop smart mechanism that consists of 3 major parts: 
* Camera that is attached to trash bin 
* AI model that will analyze type of trash (paper, metal, glass or 
plastic) 
* Hardware mechanism that will automatically open allocated trash 
bin

Instructions:
1. Download pre-trained model_new2 archive and unpack it.
2. Download libraries: PyTorch & torchvision- model loading and evaluation; Pillow - work with images; open-cv 2 - work with camera; pyfirmata - work with arduino hardware
3. Load the firmata library in arduino using arduino ide > examples
4. Connect arduino to pc/laptop.
5. Run code.
6. Place object in front of camera.
7. Press e button to take a photo and predict its material. Press e again to stop taking photos.
8. Press q for exit.

Dataset info:
https://www.kaggle.com/datasets/asdasdasasdas/garbage-classification
Contains 6 classes: cardboard, glass, metal , paper, plastic and trash
Open source kaggle dataset
Garbage segregation involves separating wastes according to how it's handled or processed. It's important for recycling as some materials are recyclable and others are not.

Additional Materials: 
[Presentation](https://github.com/NodiraTillayeva/AKIRA-Trasher/blob/main/Presentation.pdf)
[Report](https://github.com/NodiraTillayeva/AKIRA-Trasher/blob/main/Rep.pdf)
[YouTube Video](https://youtu.be/xzYkIli7oVY)
