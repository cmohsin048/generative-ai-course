# Your AI engineering course

Start by double-clicking **start-course.cmd** in this folder. It opens this guide in VS Code.

Your existing Python 3.13 environment has the core course packages installed and verified. You do not need to activate it or reinstall Python.

## Start today

1. Open [Introduction to Generative AI](./01-introduction-to-genai/README.md). In VS Code, press Ctrl+Shift+V to preview Markdown with its images.
2. Read the lesson and write five sentences explaining what an LLM does and where it can fail.
3. Open [your practice script](./my-learning/practice.py), change it, and run it with **practice.cmd**. This exercise needs no API key.
4. Tick the lesson in [your progress tracker](./my-learning/progress.md).

The README files are the lessons. Videos are optional external resources.

## Run code and notebooks

- Double-click **check-course.cmd** to check packages and credential availability. It never prints your keys or makes paid requests.
- Double-click **practice.cmd** to run your practice script.
- To run a lesson script from a terminal, use `.\.venv\Scripts\python.exe .\06-text-generation-apps\python\oai-app.py`.
- For notebooks, install the recommended Jupyter extension when VS Code prompts you. Open an `.ipynb`, select **Select Kernel > Python Environments > .venv**, and run cells in order.
- Double-click **notebooks.cmd** for a browser notebook interface using JupyterLab. Keep its terminal open while working; press Ctrl+C there when finished.
- In JupyterLab, open [your first notebook](./my-learning/first-notebook.ipynb) and press Shift+Enter on the code cell to try it without credentials.

## Configure one provider when you reach API exercises

Your existing `.env` has been preserved. For the simplest OpenAI path, fill in `OPENAI_API_KEY` there and use examples beginning with `oai-`. For Azure, fill in the Azure endpoint, key, and deployment settings and use `aoai-` examples. Only configure the provider you choose. Never paste credentials into your practice code.

Run **check-course.cmd** after editing `.env`. Credential presence does not prove the account has access or credit. API exercises require your own provider account and may incur usage charges.

Some lessons need additional services or packages: lesson 15's supplied notebook uses Azure Cosmos DB; open-source models may require model downloads; fine-tuning needs datasets and provider support. Follow that lesson's prerequisites when you reach it.

Individual lesson requirements contain older, conflicting OpenAI versions. Avoid installing every requirements file into this shared environment. Follow the root requirements first; use a separate environment if an older example specifically needs one.

## How to finish effectively

Use 60–90 minutes per session: read for 20 minutes, code for 45 minutes, and record results for 10 minutes. Finish a lesson when you can explain it and modify its example yourself.

Build three projects as you progress: a chatbot (06–07), document Q&A with sources (08 and 15), and a tool-using assistant (11 and 17). Add evaluation and security using 13–14. Keep your own experiments in `my-learning`.

After the course, learn FastAPI, SQL, testing, deployment, and basic machine learning to strengthen your AI engineering skills.
