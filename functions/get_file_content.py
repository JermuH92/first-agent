import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):

    try:
        working_directory_abs = os.path.abspath(working_directory)

        target_path = os.path.normpath(os.path.join(working_directory_abs, file_path))
        valid_target_path = os.path.commonpath([working_directory_abs, target_path]) == working_directory_abs

        if not valid_target_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(target_path, "r") as file:
            file_contents_string = file.read(MAX_CHARS)

            if file.read(1):
                file_contents_string += f'[... File "{target_path} truncated at {MAX_CHARS} characters"]'
            
            return file_contents_string
    
    except Exception as e:
        return f"Error: {e}"


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the contents of a specified file relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the file to be read, relative to the working directory",
            ),
        },
        required=["file_path"]
    ),
)



