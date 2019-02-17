import click


@click.command()
def cli_main():
    click.secho(f'TODO', fg='yellow', bold=True)
