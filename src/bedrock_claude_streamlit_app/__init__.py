
import click


@click.command()
def main() -> int:
    import streamlit.web.cli as cli
    cli._main_run("app.py")
    return 0