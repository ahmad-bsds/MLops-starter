from dotenv import load_dotenv
import os
def load_env_variable(var_name, env_file_path='.env'):
    """
    Load an environment variable from a custom .env file.

    Parameters:
    var_name (str): The name of the environment variable to load.
    env_file_path (str): The path to the .env file (default is '.env').

    Returns:
    str: The value of the environment variable if found, otherwise None.
    """
    # Load the .env file
    load_dotenv(dotenv_path=env_file_path)

    # Get the environment variable
    return os.getenv(var_name)