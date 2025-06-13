import io
import os
import json
import base64
import requests
from PIL import Image
from dotenv import load_dotenv


def encode_local_image(image_path: str) -> dict:
    """
    Reads a local image file and encodes it as Base64.

    :param image_path: Path to the local image file.
    :return: Dictionary containing the Base64-encoded image.
    """
    try:
        with Image.open(image_path) as img:
            buffered = io.BytesIO()
            img.save(buffered, format="PNG")
            encoded_image = base64.b64encode(buffered.getvalue()).decode('ascii')
            return {"encoded_image": encoded_image}
    except Exception as e:
        raise Exception(f"Failed to read or encode image: {str(e)}")


def generate_dag_code_from_openai(encoded_image: dict, system_prompt: str, seed=42, temperature=0.1, top_p=0.95, max_tokens=800) -> dict:
    """
    Sends the encoded image and prompt to the OpenAI model to generate a DAG.

    :return: Dictionary with the generated DAG code.
    """
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY") #Should be AzureAI Key
    openai_endpoint = os.getenv("OPENAI_API_ENDPOINT")  # Should be like "https://<resource>.openai.azure.com/openai/deployments/<deployment>/chat/completions?api-version=2024-02-15-preview"
    

    headers = {
        "Content-Type": "application/json",
        "api-key": openai_api_key,
    }

    payload = {
        "messages": [
            {
                "role": "system",
                "content": [{"type": "text", "text": system_prompt}]
            },
            {
                "role": "user",
                "content": [{
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{encoded_image['encoded_image']}"
                    }
                }]
            }
        ],
        "seed": seed,
        "temperature": temperature,
        "top_p": top_p,
        "max_tokens": max_tokens
    }

    response = requests.post(openai_endpoint, headers=headers, json=payload)
    response.raise_for_status()
    response_json = response.json()

    if 'choices' in response_json and len(response_json['choices']) > 0:
        content = response_json['choices'][0]['message']['content']
        start_index = content.find('```json')
        end_index = content.rfind("```")

        if start_index == -1 or end_index == -1:
            raise ValueError("Could not find JSON block in OpenAI response.")

        extracted_json_str = content[start_index + 7:end_index].strip()
        dag_json = json.loads(extracted_json_str)
        dag_code = dag_json.get("dag")

        if not dag_code:
            raise ValueError("Missing 'dag' key in response JSON.")
        return {"dag_code": dag_code}
    
    raise Exception("No valid choices returned from OpenAI")


def save_dag_code_to_file(dag_code: str, output_path: str = "generated_dag.py"):
    """
    Saves the generated DAG code to a Python file locally.

    :param dag_code: Python code string of the DAG.
    :param output_path: Path to save the DAG file.
    """
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(dag_code)
        print(f" DAG saved successfully at: {output_path}")
    except Exception as e:
        raise Exception(f"Failed to write DAG to file: {str(e)}")


if __name__ == "__main__":
    print("Current Working Directory:", os.getcwd())
    # Local image path
    local_image_path = r"airflow-dag-diagram.png"  # Change as needed
    base_dir = os.path.dirname(__file__)
    image_path = os.path.join(base_dir, "airflow_dag_diagram.png")
   

    
    if not os.path.exists(local_image_path):
        raise FileNotFoundError(f"File doesn't exist at path: {local_image_path}")

    # Prompt
    system_prompt = (
        'You are an AI assistant that helps to write an Apache Airflow DAG code by understanding an image that shows '
        'an Apache Airflow DAG containing airflow tasks, task descriptions, parameters, trigger rules and edge labels. '
        'You have to prioritize the Apache Airflow provider operators over core operators if they resonate more with the task. '
        'Use appropriate operators. Use Labels for edges from airflow.utils.edgemodifier. Use DummyOperators for start/end. '
        'Return a JSON like: ```json{"dag": "<DAG code>"}```.'
    )

    try:
        # Step 1: Encode image
        encoded = encode_local_image(local_image_path)

        # Step 2: Call OpenAI
        dag_output = generate_dag_code_from_openai(encoded, system_prompt)

        # Step 3: Save to file
        save_dag_code_to_file(dag_output["dag_code"])

    except Exception as err:
        print(f" Error: {err}")
