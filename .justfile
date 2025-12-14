dev-push:
  uv version --bump dev
  uv format
  rm -fr dist
  uv build
  uvx twine upload -r matthiasgloriusgenie dist/*

clean:
  find . -path *_cache* -print -delete
  find . -path *__pycache__* -print -delete
  rm -frv .venv dist
  find . -name *pyc -print -delete
  