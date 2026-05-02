# Visão Computacional — Reconhecimento de Gestos (0–9)

Módulo de visão computacional que identifica **dígitos de 0 a 9** mostrados com a mão via webcam, usando **MediaPipe Hands** + **Random Forest**.

---

## Como funciona

```
Webcam → MediaPipe (21 landmarks) → Random Forest → Dígito predito
```

O MediaPipe extrai 21 pontos 3D da mão. Os landmarks são normalizados em relação ao pulso e usados como features para um classificador Random Forest.

---

## Fluxo de uso

### 1. Coletar dados de treino

```bash
python visao/collect_data.py
```

- Pressione `0`–`9` para gravar 200 frames de cada dígito
- Pressione `Q` para sair
- Os dados são salvos em `visao/data/landmarks.csv`

> **Dica:** Varie ângulos e distâncias da câmera para um modelo mais robusto.

### 2. Treinar o modelo

```bash
python visao/train_model.py
```

- Treina o Random Forest com validação cruzada (5-fold)
- Exibe relatório de classificação e matriz de confusão
- Salva o modelo em `visao/modelo/modelo_visao.pkl`

### 3. Predição em tempo real

```bash
python visao/predict_live.py
```

- Abre a webcam
- Mostra o dígito reconhecido e a confiança em tempo real
- Pressione `Q` para sair

---

## Estrutura

```
visao/
├── collect_data.py      # Coleta landmarks via webcam
├── train_model.py       # Treina e avalia o classificador
├── predict_live.py      # Reconhecimento em tempo real
├── data/
│   └── landmarks.csv    # Dados coletados (gerado em runtime)
└── modelo/
    ├── modelo_visao.pkl       # Modelo treinado (gerado em runtime)
    └── confusion_matrix.png   # Matriz de confusão (gerado em runtime)
```

---

## Dependências

```
mediapipe
opencv-python
scikit-learn
joblib
numpy
pandas
matplotlib
seaborn
```

Instalar:
```bash
pip install mediapipe opencv-python scikit-learn joblib numpy pandas matplotlib seaborn
```
