# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from yaml import load


def pytest_addoption(parser):
    group = parser.getgroup("pytest_yaml")

    group.addoption(
        "--yaml-file",
        action="store",
        dest="yaml_file",
        help='used to define the yaml file',
    )


@pytest.fixture
def yaml_output(request):
    yaml_file = request.config.getoption("yaml_file")
    return load(open(yaml_file, 'r')) if yaml_file is not None else {}
