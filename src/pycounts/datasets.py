from importlib import resources

def get_flatland():
    """Get path to example "Flatland" [1]_ text file.
    Returns
    -------
    pathlib.Path
        Path to file.
    References
    ----------
    .. [1] E. A. Abbott, "Flatland", Seeley & Co., 1884.
    """
    # 现代化的写法，不需要 with 语句
    # 它会自动找到 pycounts.data 包下的 flatland.txt 文件
    return resources.files("pycounts.data").joinpath("flatland.txt")