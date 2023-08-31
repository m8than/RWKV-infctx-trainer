
from lightning.pytorch.cli import LightningCLI

class RWKVLightningCLI(LightningCLI):
    def add_arguments_to_parser(self, parser):
        parser.add_argument("--trainer.optimizer", default="adam")
        parser.link_arguments("trainer.optimizer", "model.optimizer")