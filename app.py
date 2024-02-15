from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = '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'


# Home route
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/cb')
def cb():
    return render_template('cb.html')


# Chat route
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']

    # Generate a conversational response
    bot_response = generate_conversational_response(user_input)

    return {'bot_response': bot_response}


def generate_conversational_response(text):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",  # Adjust the engine as per your requirement
        prompt=f"Q: {text}\nA:",
        temperature=0.7,
        max_tokens=100
    )
    return response.choices[0].text.strip()


if __name__ == "__main__":
    app.run(debug=True)
