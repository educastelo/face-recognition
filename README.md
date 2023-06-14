# face-recognition

Este repositório contém um projeto de reconhecimento facial.

1. Instale as dependências com `pip install -r requirements.txt`
2. Garanta que a instalação da biblioteca "dlib" foi instalada corretamente (a bibliteca dlib é compilada com c++, por isso, caso a instalação seja em um computador Windows, deve-se instalar o visual studio com c++ e dev kit)
3. Utilize o script build_face_dataset.py para criar um dataset
4. Em seguida, utilize o script encode_faces.py para gerar o arquivo "encodings.pickle", onde serão armazenados as características das faces
5. Por fim, execute o script "recognize_faces_video.py"
