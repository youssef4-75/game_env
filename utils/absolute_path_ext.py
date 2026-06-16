from pathlib import Path


def get_absolute_path(relative_path: str, file: str) -> str:
    """
    Convert a relative path to an absolute path based on the script's location.
    
    Args:
        relative_path: Path relative to the script file
    
    Returns:
        Absolute path as string
    """
    # Get the directory where the current script is located
    script_dir = Path(file).parent.resolve()
    
    # Join with the relative path
    absolute_path = script_dir / relative_path
    
    # Return as string
    return str(absolute_path)



def get_project_root() -> Path:
    """Get the project root by going up from this utils file."""
    return Path(__file__).parent.parent.resolve()

def from_root(relative_path: str) -> str:
    """Resolve path relative to project root."""
    return str(get_project_root() / relative_path)