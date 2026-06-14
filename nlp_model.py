from transformers import pipeline

# Pretrained model (no training needed)
nlp_model = pipeline(
    "text-classification",
    model="bhadresh-savani/bert-base-uncased-emotion"
)

def predict_text(text):
    result = nlp_model(text)[0]

    label = result["label"]
    score = result["score"] * 100

    return label, score