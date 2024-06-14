from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
import tensorflow as tf

app = FastAPI()

model_name = "gregorymarchal/projet-7-trained-distilbert"
model = TFAutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

class TextInput(BaseModel):
    text: str

@app.post("/predict")
async def predict(input: TextInput):
    inputs = tokenizer(input.text, return_tensors="tf")
    outputs = model(inputs.data)
    logits = outputs.logits
    predicted_class_id = tf.argmax(logits, axis=1).numpy()[0]
    return {"predicted_class_id": int(predicted_class_id)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
