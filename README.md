# Face Recognition System

Um sistema completo de reconhecimento facial em tempo real usando face_recognition, dlib e OpenCV.

## 📋 Descrição

Este projeto implementa um sistema de reconhecimento facial completo que permite cadastrar pessoas e identificá-las em tempo real através da webcam. O sistema utiliza a biblioteca `face_recognition` (baseada em dlib) para detectar e codificar faces, armazenando os encodings em um arquivo pickle para comparação posterior.

## ✨ Características

- ✅ Captura de faces para criação de dataset
- ✅ Codificação facial usando modelo CNN
- ✅ Reconhecimento em tempo real via webcam
- ✅ Interface visual com bounding boxes
- ✅ Detecção automática de câmera USB
- ✅ Armazenamento de encodings em arquivo pickle

## 🛠️ Instalação

### Pré-requisitos

- Python (testado somente no 3.12)
- Webcam (para captura e reconhecimento)
- **Windows**: Visual Studio com C++ Build Tools e Windows SDK (necessário para compilar dlib)

### 1. Clone o repositório

```bash
git clone https://github.com/educastelo/face-recognition.git
cd face-recognition
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

⚠️ **Importante**: A biblioteca `dlib` é compilada com C++, então em sistemas Windows você precisará:

1. **Instalar Visual Studio** com componentes C++ e Windows SDK
2. **Instalar CMake** (geralmente já incluído no Visual Studio)
3. **Garantir que o compilador C++ está disponível** no PATH

**Alternativa para Windows**: Você pode usar versões pré-compiladas de dlib disponíveis em sites como [Python Extension Packages](https://www.lfd.uci.edu/~gohlke/pythonlibs/#dlib).

## 🚀 Uso

### Passo 1: Criar o Dataset

Execute o script para capturar faces e criar o dataset:

```bash
cd dataset-generator
python build_face_dataset.py
```

O script irá:
- Solicitar o nome do usuário a ser cadastrado
- Capturar 50 imagens da webcam (a cada 5 frames)
- Salvar as imagens em `dataset-generator/dataset/{nome_usuario}/`

**Controles:**
- **'q'**: Sair do programa antes de completar as 50 capturas

### Passo 2: Gerar Encodings

Após criar o dataset, gere o arquivo de encodings:

```bash
python encode_faces.py
```

Este script irá:
- Processar todas as imagens do dataset
- Gerar encodings faciais usando modelo CNN
- Salvar os encodings em `encodings.pickle`

### Passo 3: Reconhecimento em Tempo Real

Execute o script de reconhecimento:

```bash
python recognize_faces_video.py
```

O script irá:
- Detectar automaticamente a câmera USB disponível
- Processar frames em tempo real
- Identificar faces conhecidas e marcar como "Unknown" faces desconhecidas
- Exibir bounding boxes verdes com os nomes identificados

**Controles:**
- **'q'**: Sair do programa

## 📁 Estrutura do Projeto

```
face-recognition/
├── dataset-generator/
│   ├── build_face_dataset.py      # Script para captura de faces
│   ├── haarcascade_frontalface_default.xml  # Classificador Haar Cascade
│   └── dataset/                   # Pasta do dataset (criada após execução)
│       └── {nome_usuario}/        # Pasta por pessoa cadastrada
├── encode_faces.py                # Script para gerar encodings
├── recognize_faces_video.py       # Script de reconhecimento em tempo real
├── encodings.pickle               # Arquivo de encodings (gerado após encode_faces.py)
├── requirements.txt               # Dependências Python
└── README.md                      # Este arquivo
```

## 🎯 Funcionalidades Técnicas

### Detecção de Faces
- Utiliza Haar Cascade para detecção inicial no dataset
- Usa modelo CNN da face_recognition para detecção no reconhecimento
- Redimensionamento automático para otimização de performance

### Codificação Facial
- Modelo CNN para extração de características faciais
- Armazenamento eficiente em formato pickle
- Suporte para múltiplas faces por pessoa

### Reconhecimento em Tempo Real
- Detecção automática de câmera USB disponível
- Processamento otimizado (redimensionamento para 750px de largura)
- Sistema de votação para identificar faces conhecidas
- Marcação automática de faces desconhecidas

## 🔧 Personalização

### Ajustar Método de Detecção

No arquivo `recognize_faces_video.py`, você pode alterar o método de detecção:

```python
# Modelo CNN (mais preciso, mais lento)
boxes = face_recognition.face_locations(rgb, model="cnn")

# Modelo HOG (mais rápido, menos preciso)
boxes = face_recognition.face_locations(rgb, model="hog")
```

### Ajustar Resolução de Processamento

No arquivo `recognize_faces_video.py`, linha 50:

```python
# Aumentar para melhor qualidade (mais lento)
rgb = imutils.resize(frame, width=1000)

# Diminuir para melhor performance
rgb = imutils.resize(frame, width=500)
```

### Ajustar Número de Capturas

No arquivo `build_face_dataset.py`, linha 30:

```python
# Alterar de 50 para outro número
while total < 100:  # Captura 100 imagens
```

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT.

## 👨‍💻 Autor

**Eduardo** - *Desenvolvimento Inicial*

Este projeto foi desenvolvido com forte influência do [tutorial do pyimagesearch](https://pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/), que serviu como base para a implementação.

## 🙏 Agradecimentos
- [pyimagesearch tutorial](https://pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/)
- [face_recognition](https://github.com/ageitgey/face_recognition) pela biblioteca de reconhecimento facial
- [dlib](http://dlib.net/) pela biblioteca de machine learning
- [OpenCV](https://opencv.org/) pela biblioteca de visão computacional
- [imutils](https://github.com/jrosebr1/imutils) pelas ferramentas utilitárias

---

**Nota**: Este projeto foi desenvolvido para fins educacionais e de demonstração. Certifique-se de estar em conformidade com as leis de privacidade locais (como a LGPD no Brasil) ao usar sistemas de reconhecimento facial.
