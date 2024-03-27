import click

__all__ = ["MODEL_IDS"]


@click.command()
def main() -> int:
    import streamlit.web.cli as cli

    cli._main_run("app.py")
    return 0


# docs: https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html
MODEL_IDS = {
    "anthropic.claude-v2",  # Claude 2.0
    "anthropic.claude-v2:1",  # Claude 2.1
    "anthropic.claude-3-sonnet-20240229-v1:0",  # Claude 3 Sonnet
    "anthropic.claude-3-haiku-20240307-v1:0",  # Claude 3 Haiku
    "anthropic.claude-instant-v1",  # Claude Instant
}
