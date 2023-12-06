## Running this project

- Make a new virtual environment: `python3 -m venv playn_env`
- and activate the new environment: `source ~/playn_env/bin/activate`
- and install the requirements: `pip3 install -r requirements.txt`
- setup the OpenAI key by using the following command (if running locally): `export OPENAI_API_KEY="API-KEY-HERE"`
- Build the image for Docker using: `docker build -t playn-challenge .`
- Run the docker image: `docker run -it -p 8372:8372 -e OPENAI_API_KEY=API-KEY-HERE playn-challenge`
- To run it locally just run the following command: `python main.py` with the key already setup.


## Caveats

- The log probabilities are missing from the chat endpoint of OpenAI: `https://community.openai.com/t/logprobs-are-missing-from-the-chat-endpoints/289514/13`
- Since the log probabilities cannot be used, I use the `langchain-visualizer` to see how the chain works and to see what is the raw input being fed to the OpenAI model. To run the visualizer, `python visualizer.py` which will open a browser window in which you can see the agent work in real time.
