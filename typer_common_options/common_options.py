from dataclasses import dataclass
from typing import Annotated

from typer import Option

from typer_common_options.base_options import BaseOptions


@dataclass
class CommonOptions(BaseOptions):
    verbose: Annotated[bool, Option("-v", "--verbose")] = False
