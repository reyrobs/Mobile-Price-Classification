import gradio as gr
import joblib

model_lr = joblib.load('logistic_model.sav')

def classifier(battery_power, mobile_wt, px_height, px_width, ram):
    probabilities = model_lr.predict_proba([[battery_power, mobile_wt, px_height, px_width, ram]])[0]
    
    probabilities_percentage = [(float(prob)) for prob in probabilities]

    class_probabilities = {str(i): prob for i, prob in enumerate(probabilities_percentage)}

    return class_probabilities

inputs = [
    gr.Number(value=842),
    gr.Number(value=188),
    gr.Number(value=20),
    gr.Number(value=756),
    gr.Number(value=2549),
]
outputs =  gr.Label()

title = "Mobile Price Classification"
description = "Enter the details to correctly classify the price range?"

demo = gr.Interface(
    fn=classifier,
    inputs=inputs,
    outputs=gr.outputs.Label(num_top_classes=4),
    title=title,
    description=description,
)

if __name__ == "__main__":
    demo.launch()