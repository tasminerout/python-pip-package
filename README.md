#py-test-taz

A sample python project

### Run Tests
`python3 -m unittest discover -v`

### build
`python3 -m build`

### upload to pypi
`python3 -m pip install --upgrade twine`

`python3 -m twine upload --repository testpypi dist/*`


### Test this package
create a virtual environment `python3 -m venv env`

activate the virtual env `source env/bin/activate`

install the pip package `pip install -i https://test.pypi.org/simple/ py-test-taz`

run test
```
from basic_calculator.TestCalculator import TestCalculator

print(TestCalculator.add(1, 24))
```

deactivate the virtual env `deactivate`