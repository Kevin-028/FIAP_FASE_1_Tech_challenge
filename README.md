# Tech Challenge – Fase 1 | FIAP
## Classificação de Doenças com Machine Learning
Este projeto realiza análise e classificação de dados médicos usando algoritmos de aprendizado de máquina.  

Uado o Tech challenge B

---

## 📁 Estrutura do Projeto

```
Fase_1/
├── Analise/
│   └── analise_cancer.ipynb     # Probabilidade de câncer de mama
├── DATA/
│   ├── diabetes.csv             # Base de dados – Pima Indians Diabetes
│   └── data.csv                 # Base de dados – Breast Cancer Wisconsin
├── requirements.txt
└── README.md
```

---

## ⚙️ Pré-requisitos

- Python **3.9 ou superior**
- pip

---

## 🚀 Como rodar

### 1. Clone o repositório ou baixe os arquivos

### 2. Crie um ambiente virtual

```bash
python -m venv .venv
```

Ative o ambiente:

- **Windows:**
  ```bash
  .\.venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```bash
  source .venv/bin/activate
  ```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Abra o Jupyter

```bash
jupyter notebook
```

Ou, se preferir o JupyterLab:

```bash
jupyter lab
```

### 5. Execute os notebooks

Navegue até a pasta `Analise/` e abra o notebook desejado.  
Para rodar todas as células em ordem: **Kernel → Restart & Run All**

---

## 📓 Notebooks

### `analise_cancer.ipynb`
Análise da base de dados de câncer de mama (569 pacientes, 30 features).

- Exploração e violin plots por diagnóstico  
- Detecção e correção de escala, assimetria e multicolinearidade (VIF)  
- Remoção automática de features redundantes (correlação > 0.90)  
- Pipeline: `Imputer → PowerTransformer → StandardScaler`  
- Modelos: Regressão Logística, Random Forest, Gradient Boosting, KNN, SVM calibrado  
- Curva ROC, calibração e ajuste de limiar de decisão  
- Função `prever_probabilidade()` — retorna % de risco de malignidade  

---

## 📦 Dependências principais

| Biblioteca | Versão | Uso |
|---|---|---|
| pandas | 3.0.2 | Manipulação de dados |
| numpy | 2.4.4 | Operações numéricas |
| matplotlib | 3.10.9 | Visualizações |
| seaborn | 0.13.2 | Gráficos estatísticos |
| scikit-learn | 1.8.0 | Modelos de ML e pipeline |
| statsmodels | 0.14.6 | Análise de VIF |
| shap | 0.51.0 | Interpretabilidade do modelo |
| jupyter / notebook | 1.1.1 / 7.5.6 | Ambiente dos notebooks |
