# **Detectare imagini in timp real folosind 2 modele diferite**
## **Cerinta**
1. Identifica o camera web publica de la care poti prelua un stream video (minimum 720p/20fps) prin rtsp/webrtc – de preferat imaginile sa fie dintr-un spatiu deschis in aer liber cu persoane sau masini
2. Creeaza o aplicatie prin care:
     - Sa te conectezi la camera pentru preluare de imagini (opencv sau alternativa)
     - Aplica doua modele pentru detectie de obiecte pe acest stream video (modelele trebuie sa fie diferite din perspectiva capacitatii de procesare (ex effDet5 vs YoloV2)
     - Afiseaza in paralel doua imagini de la stream-ul procesat (una pentru fiecare model) – cu un overlay care sa contina box-uri care incadreaza obiectele detectate
     - Cele doua ferestre/imagini trebuie sa fie sincronizate (atentie: modelul mai rapid va procesa mai multe frame-uri decat cel mai incet)
3. Codul trebuie structurat pe o arhitectura OOP

# Modalitate rezolvare
Am folosit doua modele, YOLOv8l si YOLOv5su pentru detectia in timp real. Am folosit un stream live de la o [camera publica](http://195.196.36.242/mjpg/video.mjpg).


