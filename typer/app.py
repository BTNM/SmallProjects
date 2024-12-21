import typer
import logging

#create typer.typer() app
app = typer.Typer()

# Define a callback function to be executed before a command is invoked
@app.callback()
def before_command_callback():
    typer.echo("Before command, callback method is invoked first")


@app.command()
def CrawlNovel(novelname: str, novelurl: list[str], output_folder: str):
    print(f"novelname: {novelname}, novelurl: {novelurl}, output_folder: {output_folder}")
    if len(novelurl) == 1:
        crawl_single_movel()
    elif len(novelurl) > 1:
        crawl_multiple_novel()
    else:
        logging.info(f"Something went wrong with the crawl_novel methond")


def crawl_single_movel():
    logging.INFO("Crawl single novel started!") 

def crawl_multiple_novel():
    logging.INFO("Crawl multiple novels started!")



if __name__ == "__main__":
    app()
