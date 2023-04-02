import typer

import carbonizer.cli


if __name__ == '__main__':
    typer.run(carbonizer.cli.carbonize)