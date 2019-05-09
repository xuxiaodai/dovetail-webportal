##############################################################################
# Copyright (c) 2019 opnfv.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################

import argparse


def test_config_normal(mocker, config_normal):
    mocker.patch(
        'argparse.ArgumentParser.parse_known_args',
        return_value=(argparse.Namespace(config_file=config_normal), None))
    from opnfv_testapi.common import config
    CONF = config.Config()
    assert CONF.mongo_url == 'mongodb://127.0.0.1:27017/'
    assert CONF.mongo_dbname == 'test_results_collection'
    assert CONF.api_port == 8000
    assert CONF.api_debug is True
    assert CONF.api_authenticate is False
    assert CONF.swagger_base_url == 'http://localhost:8000'
