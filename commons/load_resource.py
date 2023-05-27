from settings import settings


def load_resource(path, mode="r"):
    file_path = settings.resources / path
    with file_path.open(mode=mode) as file:
        return file.read()
