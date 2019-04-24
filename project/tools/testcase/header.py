#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import platform

from config.env import Ftest
from lib.request import Response
from lib.request import Request
from lib import Fassert
if platform.system() == "Linux":
    from lib.linux_log import Flog
else:
    from lib.win_log import Flog

"""
Author:fured
Date:2018.06.30
Desc:interface test case
"""

project_name = "Data Api"
desc = ""

# mongo connect pool
