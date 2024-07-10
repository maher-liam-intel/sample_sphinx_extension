import json

from sphinx.parsers import RSTParser
from docutils.frontend import OptionParser
from sphinx.util.docutils import SphinxDirective
from docutils.utils import new_document


class ShowJsonDirective(SphinxDirective):
    has_content = True

    def run(self) -> list:
        rst = ""
        with open("airports.json", "r") as f:
            airports = json.load(f)
        for airport in airports:
            rst += f"* `{airport['Name']} <{airport['Url']}>`_\n"
        print(rst)
        return self.parse_rst(rst)

    def parse_rst(self, text):
        parser = RSTParser()
        parser.set_application(self.env.app)

        settings = OptionParser(
            defaults=self.env.settings,
            components=(RSTParser,),
            read_config_files=True,
        ).get_default_values()
        document = new_document("<rst-doc>", settings=settings)
        parser.parse(text, document)
        return document.children


def setup(app: object) -> dict:
    app.add_directive("show-json", ShowJsonDirective)
