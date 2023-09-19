import typer
from typing_extensions import Annotated
from cloudguard.providers.list import provider_modules

cloudguard = typer.Typer()

@cloudguard.command()
def config(provider:Annotated[str, typer.Option("--provider")]):
    print("Provider {}".format(provider))

@cloudguard.command()
def providers():
    for idx,provider in enumerate(provider_modules.keys()):
        print("[{}] {}".format(idx+1,provider))

@cloudguard.command()
def run(
    provider: Annotated[str, typer.Option("--provider")],
    is_all_selected: Annotated[bool, typer.Option("--all")] = False,
    export_json: Annotated[str, typer.Option("-export-json")] = "output.json",
    is_list_resources: Annotated[bool, typer.Option("--list")] = False):

    if is_list_resources:
        print("Listing resources for provider: {}".format(provider))
        for idx,resource in enumerate(provider_modules[provider]):
            print("[{}] {}".format(idx+1, resource))
        exit()