from flask import Flask, render_template, request
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

app = Flask(__name__)

# Load the GPT-2 model and tokenizer
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Set the model to evaluation mode
model.eval()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['user_message']

    # Encode the user message
    input_ids = tokenizer.encode(user_message, return_tensors="pt")

    # Generate a response from the model
    with torch.no_grad():
        output = model.generate(input_ids, max_length=100, num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95, temperature=0.7)

    # Decode and extract the response
    bot_response = tokenizer.decode(output[0], skip_special_tokens=True)

    return {'bot_response': bot_response}

if __name__ == '__main__':
    app.run(debug=True)
