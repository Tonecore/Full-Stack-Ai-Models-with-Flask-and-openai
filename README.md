# Projekt Llama
#### Video Demo:  <https://youtu.be/9R-W5Xo9fOk>
#### Description:

# Welcome To Projekt Llama

In this project, I built a Flask-based web application and connected it with an API to Meta's Llama chatbots. 
The goal was to set up and operate an AI chatbot in a way that it generates high-quality outputs with quotes from legitimate sources.

**Flask Setup:**

The Flask setup contains two crucial modules: "flask" and "openai".

**app.py:**

The main functionality comes from the app.py Python code. 
I used Python 3.11 with pip 3.11 to achieve functionality with the OpenAI module. 
Python 3.12 was not functional early in 2024.

After importing the modules and setting up Flask with app = Flask(__name__), I get the Together API from an environment variable. To achieve this, I put the together.ai API key into the .bashrc with an export command. By doing this, the API setup won't get lost after restarting the system. To initialize the OpenAI client, I followed the instructions on their site and implemented it into the app.py code. Then, I started the @app.route("/") setup to connect the home (index) template. I kept it simple and only displayed text, hyperlinks, and buttons on the following routes: /index, /about, /together, /contact.

The three chatbots were set up with different models and system inputs. For the 7B bot, I used "meta-llama/Llama-2-7b-chat-hf" and no additional system input. For the 13B bot, I used "meta-llama/Llama-2-13b-chat-hf" and the following system input: "you give direct answers only" to modify the request to the model. For the 70B model, I used "meta-llama/Llama-2-70b-chat-hf" and the following system input: "answer like in a scientific summary of a paper with quotes" to modify the request to the model.

The user input will be specified according to the site where the input happened. The POST method was used for security reasons. The user input together with the system input and used model will be part of the client.chat.completions.create() message and sent via the Together API. After that, we will receive the chat_completion.choices[0].message.content from the API with our answers. We return it to the function. In all steps, we built in an exception in the form of except or if/else statements so we can monitor the process and get specific outputs if something goes wrong. With this method, we get a direct package as a response. This is very comfortable but can also take a while when big models and outputs are involved. Take in mind that together.ai also supports the streaming option, where single tokens are constantly streamed. This involves a slightly different setup but could be an option for further projects.

At the end of the app.py code, we check whether the script is being run directly with if __name__ == "__main__": and then start the Flask development server with debugging enabled (debug=True).


**Using Jinja2 Templating Engine:**

By using Jinja2, the website uses reusable templates. The layout.html template saves CSS classes and the reusable frame for all other templates on the site.

Here "<!DOCTYPE html>", viewports as well as the Bootstrap paths are set up. Custom styles for all templates are saved next. The top navigation bar with hyperlinks to the sites: Home, About, Together, and Contact is implemented afterwards. At last, an interactive sidebar is implemented. Jinja2 looks at what site was requested and then sets the according site to "active" in layout.html. For example, the line to activate the 7B path looks like this: >"<a class="list-group-item list-group-item-action {% if request.path == '/7B' %}active{% endif %}" href="/7B">7B chat</a>".


**Chat Bot Templates:**

7B, 13B, and 70B are the Llama chatbot templates.

The templates start by calling the Jinja2 layout.html frame {% extends "layout.html" %}. Content will be set in the main block {% block main %}. In this block, we find a Bot response window, an Input field, and the text-to-speech JavaScript function. The bot response window will only appear when a bot response was generated. The bot response will be provided by the Jinja2 {% if bot_response %} function. When applied, also two buttons will appear to control the text-to-speech (TTS) function. The input field uses the POST method and has autocomplete off.

Script function: First JavaScript stops any ongoing audio output by setting "currentUtterance = null". Then we set up a voice and return it. After that, we implement an event listener for both buttons (play, stop). When the event "click" on the play button occurs, we execute a function to query over the bot response and return it as audio with the setup voice. The stop button sets the current utterance to null. It is possible to implement other voice bots as well as deep learning bots if needed.

**Conclusion:**

This project showcases the integration of advanced natural language processing models into a Flask web application, providing users with interactive chatbot experiences. By leveraging the power of large language models and APIs, the application enables seamless communication with the Llama chatbots, offering various functionalities tailored to different user needs. With further refinement and optimization, this project sets the foundation for the development of more sophisticated and efficient conversational interfaces in future endeavors.


Created by Konrad Bizer

Output Example: ![Example of modified Llama2 70B output](/example.png)
