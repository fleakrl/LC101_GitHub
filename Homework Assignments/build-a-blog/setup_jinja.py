import jinja2
import os


def setup_jinja():
    # set up jinja
    template_dir = os.path.join(os.path.dirname(__file__), "Templates")
    jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)

    return jinja_env
