import typer, time

app = typer.Typer( )

def main(delete: bool = typer.Option(False, help="Supprime les fichiers trouvés" ), extension: str = typer.Argument("txt", help="Extension à chercher")):
    """Affich les fichiers trouvés avec l'extension données
    """
    fichiers = typer.style("fichiers", bold=True, fg=typer.colors.RED)
    typer.secho(f"Recherche des {fichiers} avec l'extension {extension}.", fg=typer.colors.BLUE)
    if delete:
        confirm = typer.confirm("Shouaitez vous vraiment supprimer les fichiers ?")
        if not confirm:
            typer.echo("On annule.")
            raise typer.Abort()
        files = range(100)
        with typer.progressbar(files) as progress:
            for file in progress:
                time.sleep(0.05)
        print("Suppression des fichiers.")

@app.command("search")
def search_py():
    main(delete=False, extension="py")

@app.command("delete")
def delete_py():
    main(delete=True, extension="py")

if __name__ == "__main__":
    app()