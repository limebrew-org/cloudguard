import typer
from typing_extensions import Annotated

app = typer.Typer()

@app.command()
def config(provider:Annotated[str, typer.Option("--provider")]):
    print("Provider {}".format(provider))

@app.command()
def providers():
    providers_list = ["GCP", "AWS", "Azure"]

    for i in range(0, len(providers_list)):
        print("[{}] {}".format(i+1, providers_list[i]))

@app.command()
def run(
    provider: Annotated[str, typer.Option("--provider")] = None,
    is_all_selected: Annotated[bool, typer.Option("--all")] = False,
    export_json: Annotated[str, typer.Option("-export-json")] = "output.json",
    list_resources: Annotated[bool, typer.Option("--list")] = False):
    print("running cloudguardian for {} , all:{} export-path: {}".format(provider,is_all_selected,export_json))

    if list_resources:
        print("listing resources for provider: {}".format(provider))


if __name__ == "__main__":
    app()