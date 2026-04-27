import os
import subprocess
from google.genai import types


def run_python_file(working_directory, file_path, args=None):

    working_directory_abs = os.path.abspath(working_directory)

    target_path = os.path.normpath(os.path.join(working_directory_abs, file_path))
    valid_target_path = os.path.commonpath([working_directory_abs, target_path]) == working_directory_abs

    if not valid_target_path:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(target_path):
        return f'Error: "{file_path}" does not exist or is not a regular file'
    
    if not target_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file'
    
    command = ["python", target_path]
    if args is not None:
        command.extend(args)

    try:
        result = subprocess.run(command, cwd=working_directory_abs, capture_output=True, text=True, timeout=30)

        result_parts = []

        if result.stdout != "":
            result_parts.append(f"STDOUT:\n{result.stdout}")
        
        if result.stderr != "":
            result_parts.append(f"STDERR:\n{result.stderr}")

        if result.returncode != 0:
            result_parts.append(f"Process exited with code {result.returncode}")
        
        if result.stdout == "" and result.stderr == "":
            result_parts.append("No output produced")
        
        return "\n".join(result_parts)
        

    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a specified Python file and returns the output.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the Python file to run, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING
                ),
                description="Optional command line arguments to pass to the script",
            ),        
        },
        required=["file_path"]
    ),
)
