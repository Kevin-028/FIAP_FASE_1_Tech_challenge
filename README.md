# Tech Challenge – Fase 1 | FIAP
### Classificação de Câncer de Mama + Visão Computacional

Projeto desenvolvido para o Tech Challenge B da FIAP, composto por três módulos independentes: análise exploratória em notebook, interface web de predição e reconhecimento de gestos por visão computacional.

---

## 📁 Estrutura do Projeto

```
Fase_1/
├── Analise/
│   └── analise_cancer.ipynb          # Análise exploratória + modelos de ML
├── DATA/
│   ├── data.csv                      # Breast Cancer Wisconsin (569 pacientes, 30 features)
│   └── diabetes.csv                  # Pima Indians Diabetes (referência)
├── modelo/
│   └── modelo_cancer.pkl             # Modelo serializado (gerado pelo notebook)
├── web/                              # Aplicação Flask MVC
│   ├── app.py                        # Entry point
│   ├── controllers/
│   │   ├── prediction_controller.py  # Rotas: predição de câncer
│   │   └── visao_controller.py       # Rotas: visão computacional
│   ├── models/
│   │   ├── cancer_model.py           # Carrega .pkl e executa predição
│   │   └── visao_model.py            # Treinamento e predição de gestos
│   ├── templates/
│   │   ├── base.html                 # Layout base (Navbar + Footer FIAP)
│   │   ├── index.html                # Formulário de diagnóstico
│   │   ├── result.html               # Resultado da predição
│   │   ├── exemplos.html             # Exemplos benignos/malignos
│   │   └── visao/
│   │       ├── index.html            # Predição de gestos em tempo real
│   │       ├── coletar.html          # Coleta de dados de treino
│   │       └── treinar.html          # Treinamento do classificador
│   └── static/
│       ├── css/
│       │   ├── bootstrap.min.css     # Bootstrap 5.3 (local)
│       │   └── custom.css            # Tema FIAP (vermelho #EF3340)
│       ├── js/bootstrap.bundle.min.js
│       └── mediapipe/                # Bibliotecas MediaPipe (local, ~24 MB)
├── visao/                            # Scripts de linha de comando (terminal)
│   ├── collect_data.py               # Coleta via webcam (terminal)
│   ├── train_model.py                # Treina o classificador (terminal)
│   ├── predict_live.py               # Predição ao vivo com OpenCV (terminal)
│   ├── data/landmarks.csv            # Dados coletados (gerado em runtime)
│   └── modelo/modelo_visao.pkl       # Modelo treinado (gerado em runtime)
├── requirements.txt
└── README.md
```

---

## ⚙️ Pré-requisitos

- Python **3.10 ou superior**
- pip
- Webcam (para o módulo de visão computacional)

---

## 🚀 Como rodar

### 1. Clone o repositório

```bash
git clone https://github.com/Kevin-028/FIAP_Tech_challenge_B.git
cd FIAP_Tech_challenge_B/Fase_1
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv .venv
```

- **Windows:** `.\.venv\Scripts\activate`
- **Mac/Linux:** `source .venv/bin/activate`

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Rode a aplicação web

**Via VS Code** — pressione `F5` (configuração de debug já incluída em `.vscode/launch.json`).

**Via terminal:**
```bash
cd web
python app.py
```

Acesse **http://localhost:5000** no navegador.

---

## 🌐 Módulo Web — Diagnóstico de Câncer de Mama

Interface web em Flask (arquitetura MVC) com tema visual FIAP.

| Rota | Descrição |
|---|---|
| `/` | Formulário com os 30 parâmetros citológicos |
| `/resultado` | Resultado: Benigno / Maligno + probabilidade |
| `/exemplos` | Casos reais: benignos, malignos, falsos positivos/negativos |

### Funcionalidades
- Valores pré-preenchidos com médias do dataset (facilita o uso clínico)
- Grupos organizados por característica (Raio, Textura, Área, etc.)
- Probabilidade de malignidade com barra visual
- Exemplos reais rotulados com contexto médico

---

## ✋ Módulo de Visão Computacional — Reconhecimento de Gestos

Reconhece **números de 1 a 5** mostrados com a mão via webcam, usando **MediaPipe Hands** + **Random Forest**.

```
Webcam → MediaPipe (21 landmarks 3D) → normalização → Random Forest → Dígito (1–5)
```

Com **duas mãos**, exibe os dois dígitos e a soma (ex: 3 + 4 = 7).

### Uso via Web (recomendado)

| Rota | Descrição |
|---|---|
| `/visao` | Predição em tempo real (1 ou 2 mãos) |
| `/visao/coletar` | Coleta de amostras de treino via webcam |
| `/visao/treinar` | Treina o modelo e exibe métricas + matriz de confusão |

**Fluxo:**
1. Vá em `/visao/coletar` — selecione um dígito (1–5), clique em **Gravar** (200 amostras por dígito)
2. Vá em `/visao/treinar` — clique em **Treinar Agora**
3. Vá em `/visao` — inicie a câmera e mostre sua mão

> As bibliotecas MediaPipe ficam em `web/static/mediapipe/` — **não há dependência de CDN ou internet**.

### Uso via Terminal (alternativo)

```bash
# 1. Coletar dados
python visao/collect_data.py      # pressione 1–5 para gravar, Q para sair

# 2. Treinar
python visao/train_model.py

# 3. Predizer ao vivo
python visao/predict_live.py
```

---

## 📓 Notebook de Análise

`Analise/analise_cancer.ipynb` — análise completa do dataset Breast Cancer Wisconsin:

- Exploração com violin plots por diagnóstico
- Detecção de assimetria, escala e multicolinearidade (VIF)
- Remoção de features redundantes (correlação > 0.90)
- Pipeline: `Imputer → PowerTransformer → StandardScaler`
- Modelos comparados: Regressão Logística, Random Forest, Gradient Boosting, KNN, SVM calibrado
- Curva ROC, calibração e ajuste de limiar de decisão

Abrir:
```bash
jupyter notebook Analise/analise_cancer.ipynb
```

---

## 📦 Dependências principais

| Biblioteca | Uso |
|---|---|
| `Flask` | Servidor web (MVC) |
| `scikit-learn` | Modelos de ML (Logística, Random Forest, pipeline) |
| `pandas` / `numpy` | Manipulação de dados |
| `matplotlib` / `seaborn` | Visualizações |
| `statsmodels` | Análise VIF |
| `shap` | Interpretabilidade |
| `mediapipe` | Extração de landmarks da mão |
| `opencv-python` | Captura de webcam (scripts terminais) |
| `joblib` | Serialização de modelos |
| `jupyter` / `jupyterlab` | Ambiente dos notebooks |

---

## 🌿 Branches

| Branch | Descrição |
|---|---|
| `main` | Versão estável (merge de DEV_WEB + DEV_VISAO) |
| `DEV_WEB` | Desenvolvimento da interface web Flask |
| `DEV_VISAO` | Desenvolvimento do módulo de visão computacional |

