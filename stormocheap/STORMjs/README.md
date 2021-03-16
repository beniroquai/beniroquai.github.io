# Steps to setup TFJS

- Export Model using Tensorflow==2.2.0
- Use the file ```keras_exportjs.py```
- Use model: [Google Colab](https://colab.research.google.com/drive/1Dfop6YTcXnAtDCq_LAREGM3ZKVrVglgj?usp=sharing)
- Download model folder and open ```config.json```; Replace ```Functional```with ```Model```
- Add ```N_x```, etc. variables in ```index_webcam.js``` and replace filename for modelfolder
- Run Server using ```python3 -m http.server 8000``` and open the browser [localhost:8000/index_webcam.html](localhost:8000/index_webcam.html)
- Accept Webcam => Done 


# Knwon issues 

- [Floating Values](https://github.com/tensorflow/tfjs/issues/415)