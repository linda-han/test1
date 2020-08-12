import pytest
import yaml



def test_func():
    print(yaml.safe_load(open("./data.yml")))
