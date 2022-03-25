from jinja2 import Environment, FileSystemLoader, Template
from pathlib import Path
from typing import List
from bs4 import BeautifulSoup
from argparse import ArgumentParser

current_dir: Path = Path(__file__).parent
templates_dir: Path = current_dir / 'templates'
export_dir: Path = current_dir / 'empty_pages'


def export(template_fn: str, data: dict = {}, export_fn: str = None) -> None:
    template_path: Path = templates_dir / template_fn
    template_content: str = template_path.read_text(encoding='utf-8')
    template: Template = Environment(loader=FileSystemLoader(
        templates_dir)).from_string(template_content)
    export_fn = export_fn or template_fn
    export_fp: Path = export_dir / export_fn
    rendered: str = template.render(data)
    soup: BeautifulSoup = BeautifulSoup(rendered, "html.parser")
    rendered: str = soup.prettify()
    export_fp.write_text(rendered, encoding='utf-8')


def export_quiz_articles(index: int, is_last_article: bool = False):
    title: str = f"第{index}問"
    Q_fn: str = f"{index}Q.html"
    S1_fn: str = f"{index}S1.html"
    S2_fn: str = f"{index}S2.html"
    S3_fn: str = f"{index}S3.html"
    next_fn: str = "fin.html"if is_last_article else f"{index+1}Q.html"

    export("Q.html", {
        "title": title,
        "S1_fn": S1_fn,
        "S2_fn": S2_fn,
        "S3_fn": S3_fn},
        Q_fn)
    for S_fn in [S1_fn, S2_fn, S3_fn]:
        export("S.html", {
            "title": title,
            "next_fn": next_fn,
            "Q_fn": Q_fn},
            S_fn)


def main():
    parser = ArgumentParser()
    parser.add_argument('-n', '--num_question_articles', type=int, default=3)
    args = parser.parse_args()

    num_question_articles: int = args.num_question_articles
    for index in range(1, num_question_articles+1):
        is_last_article: bool = (index == num_question_articles)
        export_quiz_articles(index, is_last_article)

    export("index.html")
    export("fin.html")


main()
