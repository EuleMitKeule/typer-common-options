from typer import Context, Typer

from typer_common_options.common_options import CommonOptions
from typer_common_options.typer_extensions import callback, command

app = Typer()


@command(app, [CommonOptions])
def hello(ctx: Context, name: str):
    if CommonOptions.instance.verbose:
        print("Verbose mode is on (hello)")
    print(f"Hello {name}")


@callback(app, [CommonOptions])
def main(ctx: Context):
    if CommonOptions.instance.verbose:
        print("Verbose mode is on (main)")


if __name__ == "__main__":
    app()
