dev-push:
  uv version --bump dev
  uv format
  rm -fr dist
  uv build
  uvx twine upload -r matthiasgloriusgenie dist/*

push-test:
  rm -fr dist
  uv build
  uvx twine upload -r testpypi dist/*

clean:
  find . -path *_cache* -print -delete
  find . -path *__pycache__* -print -delete
  rm -frv .venv dist uv.lock paper/*{aux,lof,log,lot,pdf,toc}
  find . -name *pyc -print -delete
  
test:
  uvx pytest