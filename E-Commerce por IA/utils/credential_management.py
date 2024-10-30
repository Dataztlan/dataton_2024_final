import yaml

def load_credentials() -> dict:
    """
    Load credentials from credentials.yaml file
    
    Parameters
    ----------
    None
    
    Returns
    -------
    dict
        The credentials loaded from the file
    """
    with open('credentials.yaml', 'r') as file:
        credentials = yaml.safe_load(file)
    return credentials