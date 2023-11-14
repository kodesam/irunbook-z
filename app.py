from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_response', methods=['POST'])
def generate_response():
    input_text = request.form['inputText']
    instruction = request.form['instruction']
    model = request.form['model']

    # Make a request to OpenAI API
    response = openai.Completion.create(
        engine=model,
        prompt=f"{instruction}\n\n{input_text}",
        max_tokens=100  # You can customize other parameters as needed
    )

    # Get the generated text
    generated_text = response['choices'][0]['text']

    return jsonify({'generatedText': generated_text})

if __name__ == '__main__':
    app.run(debug=True)
