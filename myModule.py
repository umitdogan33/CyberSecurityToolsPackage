from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel

def credit():
    def get_content():
        return "created by github:umitdogan33"

    console = Console()
    user_renderables = [Panel(get_content(), expand=True)]
    console.print(Columns(user_renderables))
