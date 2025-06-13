Markdown

# Airflow DAG Generator from Image (Vision-AI)

This project leverages Azure OpenAI's Vision capabilities to generate Apache Airflow DAG (Directed Acyclic Graph) Python code directly from an image. Simply provide a diagram of your desired Airflow DAG, and the system will attempt to convert it into executable Python code.

## ✨ Features

* **Image to DAG Code:** Automatically generates Airflow DAG Python code from a visual representation (e.g., a diagram of tasks and dependencies).
* **Base64 Encoding:** Handles local image encoding for submission to the Vision AI model.
* **Azure OpenAI Integration:** Communicates with Azure OpenAI Service to interpret the image and generate code.
* **Configurable Prompts:** Allows customization of the system prompt to guide the AI's code generation.
* **Local File Output:** Saves the generated DAG code directly to a Python file.

## 🚀 Getting Started

Follow these steps to set up and run the DAG generator.

### Prerequisites

* Python 3.8+
* An Azure OpenAI Service instance with a deployed model that supports Vision capabilities (e.g., `gpt-4o`, `gpt-4-vision-preview`).
* Your Azure OpenAI API Key and Endpoint.

### 1. Installation

Clone this repository and install the required Python packages:

```bash
git clone <your-repository-url>
cd airflow-dag-generator
pip install -r requirements.txt
requirements.txt content:

python-dotenv
requests
Pillow
2. Configuration
Create a .env file in the root directory of your project (the same directory as your Python script) and add your Azure OpenAI credentials:

Code snippet

OPENAI_API_KEY="YOUR_AZURE_OPENAI_KEY"
OPENAI_API_ENDPOINT="https://<your-resource-name>[.openai.azure.com/openai/deployments/](https://.openai.azure.com/openai/deployments/)<your-deployment-name>/chat/completions?api-version=2024-02-15-preview"
Replace YOUR_AZURE_OPENAI_KEY with your actual Azure OpenAI API key.
Replace the OPENAI_API_ENDPOINT with your specific endpoint URL, including your resource name, deployment name, and API version.
3. Prepare Your DAG Diagram
Place your Airflow DAG diagram image file (e.g., airflow-dag-diagram.png) in the same directory as your Python script or update the local_image_path variable in main.py accordingly.

Example airflow-dag-diagram.png (conceptual):
(Imagine an image here showing a simple Airflow DAG with nodes like "Start Task" -> "Process Data" -> "Load Data" -> "End Task", possibly with labels.)

4. Running the Generator
Execute the main Python script:

Bash

python your_script_name.py
(Replace your_script_name.py with the actual name of your Python file, e.g., generate_dag.py)

The script will:

Read and encode your image.
Send the encoded image and a system prompt to the Azure OpenAI Vision model.
Extract the generated Python DAG code from the AI's response.
Save the generated code to a file named generated_dag.py (or your specified output_path).
⚙️ Configuration (Code Details)
You can adjust the following parameters within the generate_dag_code_from_openai function or by modifying the if __name__ == "__main__": block:

local_image_path: Path to your input DAG diagram image.
system_prompt: A crucial string that guides the AI on what kind of DAG to generate (e.g., prioritizing specific operators, trigger rules, etc.).
seed: (Optional) For reproducible results from the OpenAI model.
temperature: (Default 0.1) Controls the randomness of the output. Lower values mean less creative, more deterministic output.
top_p: (Default 0.95) Controls diversity via nucleus sampling.
max_tokens: (Default 800) Maximum number of tokens for the AI's response. Adjust based on the complexity of expected DAGs.
output_path: (Default generated_dag.py) The filename for the generated DAG Python code.
📝 System Prompt Guidelines
The system_prompt is key to getting good results. Here's what the current prompt emphasizes:

Python

system_prompt = (
    'You are an AI assistant that helps to write an Apache Airflow DAG code by understanding an image that shows '
    'an Apache Airflow DAG containing airflow tasks, task descriptions, parameters, trigger rules and edge labels. '
    'You have to prioritize the Apache Airflow provider operators over core operators if they resonate more with the task. '
    'Use appropriate operators. Use Labels for edges from airflow.utils.edgemodifier. Use DummyOperators for start/end. '
    'Return a JSON like: ```json{"dag": "<DAG code>"}```.'
)
When designing your image, try to:

Clearly label tasks with names and brief descriptions.
Indicate task dependencies with arrows.
If using specific parameters or trigger rules, try to represent them clearly (e.g., text annotations next to tasks or edges).
For advanced features like edge labels, explicitly draw them on the connection lines.
💡 Potential Enhancements
Error Handling Refinements: More specific error messages for API failures or parsing issues.
DAG Validation: Integrate a basic Airflow DAG validator to check the generated Python code for syntax and common issues.
Interactive Input: Allow users to specify image path and prompt interactively.
GUI: Develop a simple graphical user interface (GUI) for easier interaction.
Support for other DAG orchestrators: Extend to generate code for tools like Prefect or dbt.
Dockerization: Provide a Dockerfile for easy environment setup.
🤝 Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests.

📄 License
This project is open-source. (Consider adding a specific license like MIT, Apache 2.0, etc.)
