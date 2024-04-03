import os

from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)


# Get Together API key from environment variable
TOGETHER_API_KEY = os.environ.get("TOGETHER_API_KEY")

# Check if the API key is available
if TOGETHER_API_KEY is None:
    raise ValueError("TOGETHER_API_KEY environment variable is not set.")

# Initialize OpenAI client
client = OpenAI(
    api_key=TOGETHER_API_KEY,
    base_url='https://api.together.xyz/v1',
)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/together")
def together():
    return render_template("together.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


#Set up 7B bot
@app.route("/7B", methods=["GET", "POST"])
def b7():
    if request.method == "POST":
        user_input7B = request.form.get("input", "")
        bot_response7B = generate_bot_response7B(user_input7B)
        return render_template("7B.html", bot_response7B=bot_response7B, user_input7B=user_input7B)
    else:
        return render_template("7B.html")

def generate_bot_response7B(user_input7B):
    try:
         # Send user input to the Together API
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": ""},
                {"role": "user", "content": user_input7B}
            ],
            model="meta-llama/Llama-2-7b-chat-hf"
        )

        # Extract and return bot response from the API response
        return chat_completion.choices[0].message.content
    except Exception as e:
        # Handle API request errors
        print("Error:", e)
        return ["Error occurred while processing the request."]



#Set up 13b bot
@app.route("/13B", methods=["GET", "POST"])
def b13():
    if request.method == "POST":
        user_input13B = request.form.get("input", "")
        bot_response13B = generate_bot_response13B(user_input13B)
        return render_template("13B.html", bot_response13B=bot_response13B, user_input=user_input13B)
    else:
        return render_template("13B.html")

def generate_bot_response13B(user_input13B):
    try:
        # Send user input to the Together API
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "you give direkt answers only"},
                {"role": "user", "content": user_input13B}
            ],
            model="meta-llama/Llama-2-13b-chat-hf"
        )

        # Extract and return bot response from the API response
        return chat_completion.choices[0].message.content
    except Exception as e:
        # Handle API request errors
        print("Error:", e)
        return "Error occurred while processing the request."
    

#set up 70b bot
@app.route("/70B", methods=["GET", "POST"])
def b70():
    if request.method == "POST":
        user_input70B = request.form.get("input", "")
        bot_response70B = generate_bot_response70B(user_input70B)
        return render_template("70B.html", bot_response70B=bot_response70B, user_input70B=user_input70B)
    else:
        return render_template("70B.html")

def generate_bot_response70B(user_input70B):
    try:
        # Send user input to the Together API
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "answer like in a scientific summery of a paper with quotes"},
                {"role": "user", "content": user_input70B}
            ],
            model="meta-llama/Llama-2-70b-chat-hf"
        )

        # Extract and return bot response from the API response
        return chat_completion.choices[0].message.content
    except Exception as e:
        # Handle API request errors
        print("Error:", e)
        return "Error occurred while processing the request."

if __name__ == "__main__":
    app.run(debug=True)
