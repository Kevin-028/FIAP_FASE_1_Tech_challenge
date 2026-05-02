"""
Controller layer — define as rotas (Blueprint) para predição de câncer.
"""
import os, json
from flask import Blueprint, render_template, request
from models.cancer_model import predict, FEATURES, FEATURE_META, FEATURE_GROUPS, METRICAS, NOME_MODELO

prediction_bp = Blueprint("prediction", __name__)

# ── helpers ────────────────────────────────────────────────────────────────

def _build_form_groups(form_data: dict):
    groups = {}
    for gkey, gmeta in FEATURE_GROUPS.items():
        groups[gkey] = {**gmeta, "inputs": []}
    for f in FEATURES:
        meta = FEATURE_META[f]
        groups[meta["group"]]["inputs"].append({
            "label": meta["label"],
            "value": form_data.get(f, "—"),
        })
    return groups


# ── rotas ──────────────────────────────────────────────────────────────────

@prediction_bp.route("/", methods=["GET"])
def index():
    groups = {}
    for gkey, gmeta in FEATURE_GROUPS.items():
        groups[gkey] = {**gmeta, "features": []}
    for feat in FEATURES:
        meta = FEATURE_META[feat]
        groups[meta["group"]]["features"].append({"name": feat, **meta})
    return render_template("index.html", groups=groups,
                           nome_modelo=NOME_MODELO, metricas=METRICAS)


@prediction_bp.route("/predict", methods=["POST"])
def predict_view():
    form_data = request.form.to_dict()
    try:
        result = predict(form_data)
    except Exception as e:
        return render_template("index.html", error=str(e))

    patient = {
        "nome":       form_data.get("paciente_nome", "").strip(),
        "data":       form_data.get("paciente_data", "").strip(),
        "prontuario": form_data.get("paciente_prontuario", "").strip(),
    }
    return render_template("result.html", result=result,
                           groups=_build_form_groups(form_data),
                           patient=patient)


@prediction_bp.route("/exemplos", methods=["GET"])
def exemplos():
    _dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(_dir, "examples_data.json"), encoding="utf-8") as fp:
        raw = json.load(fp)

    CAT_META = {
        "benigno_claro":   {"label": "Benigno Evidente",        "color": "success",  "icon": "🟢"},
        "benigno_limiar":  {"label": "Benigno com Atipia Leve", "color": "info",     "icon": "🔵"},
        "maligno_claro":   {"label": "Maligno Evidente",        "color": "danger",   "icon": "🔴"},
        "maligno_limiar":  {"label": "Maligno Borderline",      "color": "warning",  "icon": "🟡"},
        "falso_positivo":  {"label": "Falso Positivo ⚠️",       "color": "fp",       "icon": "⚠️"},
        "falso_negativo":  {"label": "Falso Negativo ⚠️",       "color": "fn",       "icon": "⚠️"},
    }

    examples = []
    for i, ex in enumerate(raw):
        meta = CAT_META.get(ex["cat"], {})
        examples.append({
            "id":      i,
            "cat":     ex["cat"],
            "label":   meta.get("label", ex["cat"]),
            "color":   meta.get("color", "secondary"),
            "icon":    meta.get("icon", ""),
            "real":    ex["real_s"],
            "pred":    ex["pred_s"],
            "prob":    ex["prob"],
            "dados":   {f: ex[f] for f in FEATURES},
        })

    return render_template("exemplos.html", examples=examples, features=FEATURES,
                           feature_meta=FEATURE_META)

