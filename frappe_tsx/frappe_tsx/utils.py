from pathlib import Path


def create_file(path: Path, content: str | None = None):
	"""
	Create a file if it doesn't exist
	"""
	if not path.exists():
		path.touch()

	if content:
		with path.open("w") as f:
			f.write(content)


def get_module_path(module: str) -> Path:
	"""
	Get the path to the module
	"""
	return Path(__file__).parent.parent.parent / "apps" / module
