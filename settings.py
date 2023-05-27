from pathlib import Path


class Settings:
    base_dir = Path(__file__).absolute().parent

    @property
    def resources(self):
        return self.base_dir / "resources"


settings = Settings()
