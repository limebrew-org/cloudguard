import typer
from typing_extensions import Annotated

cloudguard = typer.Typer()

@cloudguard.command()
def config(provider:Annotated[str, typer.Option("--provider")]):
    print("Provider {}".format(provider))

@cloudguard.command()
def providers():
    providers_list = ["GCP", "AWS", "Azure"]

    for i in range(0, len(providers_list)):
        print("[{}] {}".format(i+1, providers_list[i]))

@cloudguard.command()
def run(
    provider: Annotated[str, typer.Option("--provider")] = None,
    is_all_selected: Annotated[bool, typer.Option("--all")] = False,
    export_json: Annotated[str, typer.Option("-export-json")] = "output.json",
    list_resources: Annotated[bool, typer.Option("--list")] = False):
    print("Running cloudguard for {} , all:{} export-path: {}".format(provider,is_all_selected,export_json))

    if list_resources:
        print("Listing resources for provider: {}".format(provider))