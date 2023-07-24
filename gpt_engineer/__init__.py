def get_version():
    """
    Get the version from the package metadata
    """
    from importlib.metadata import version

    return version("gpt_engineer")


__version__ = get_version()