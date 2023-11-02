# Common Options in Typer

## Installation

1. `poetry config virtualenvs.in-project true`
2. `poetry install`
3. `source .venv/bin/activate` (Linux) **or** `\.venv\Scripts\activate` (Windows)

## Execution

* `python -m typer_common_options --verbose hello world`
* `python -m typer_common_options hello --verbose world`
* `python -m typer_common_options hello world --verbose`

All three examples work.

## Development

```py
from dataclasses import dataclass
from typing import Annotated

from typer import Option, Context

from typer_common_options.base_options import BaseOptions
from typer_common_options.__main__ import app
from typer_common_options.typer_extensions import command

# Create a custom options class.
@dataclass
class MyOptions(BaseOptions):
    my_option: Annotated[str, Option("-f", "--foo", help="Foo")] = "foo"


# Access the custom class.
@command(app, [MyOptions])
def my_command(ctx: Context):
    print(MyOptions.instance.my_option)
```
