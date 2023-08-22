import os
from typing import Optional

VYPER_COLOR_OUTPUT = os.environ.get("VYPER_COLOR_OUTPUT", "0") == "1"
VYPER_ERROR_CONTEXT_LINES = int(os.environ.get("VYPER_ERROR_CONTEXT_LINES", "1"))
VYPER_ERROR_LINE_NUMBERS = os.environ.get("VYPER_ERROR_LINE_NUMBERS", "1") == "1"

VYPER_TRACEBACK_LIMIT: Optional[int]

_tb_limit_str = os.environ.get("VYPER_TRACEBACK_LIMIT")
VYPER_TRACEBACK_LIMIT = None if _tb_limit_str is None else int(_tb_limit_str)
