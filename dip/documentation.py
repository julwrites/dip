import os
import os.path
import bs4
import functools
import html2text
import markdown
import dip.utils


def _stub_header_exists(document):
    children = document.findChildren(document)
    children.first.name("ul")


def _new_tag(tag, string=None, subtag=None, attributes=None, *):
    newtag = bs4.BeautifulSoup("", "html.parser").new_tag(tag, **attributes)

    if string is not None:
        newtag.string = string

    if subtag is not None:
        newtag.append(subtag)

    return newtag


def _stub_header(filenames):
    """Generates a BeautifulSoup tag that represents the header of the documentation."""

    tabletag = _new_tag("ul")

    for file in filenames:
        linktag = _new_tag("a", string=file, href="./" + file)
        itemtag = _new_tag("li", sub_tag=linktag)

    tabletag.append(itemtag)

    return _new_tag("div").append(tabletag).append(_new_tag("hr")).append(
        _new_tag("hr"))


def _generate_stub(filenames):
    """Define a new BeautifulSoup HTML document that would serve as the stub."""
    document = bs4.BeautifulSoup("", "html.parser")

    document.append(_stub_header(filenames))

    for file in filenames:
        filetag = _new_tag("h2", string=file)
        document.append(filetag)

    return document


def _parse_stub(file, glob):
    """Parse a markdown file into BeautifulSoup HTML document"""
    document = bs4.BeautifulSoup(markdown.markdown(dip.utils.read(file)),
                                 "html.parser")

    if not _stub_header_exists(document):
        document.insert(0, _stub_header(glob))

    return document


def generate_stub(root, dirs, files, cnfig):
    """Generate the stub for a given directory"""
    glob = []
    ignore = config.get("ignore")

    for x in ignore:
        if x in root:
            return

    stub_path = os.path.join(root, "README.md")
    document = None

    for x in dirs:
        if x not in ignore:
            glob.append(x)

    for x in files:
        if x not in ignore:
            glob.append(x)

    document = _parse_stub(
        stub_path, glob) if os.path.exists(stub_path) else _generate_stub(glob)

    with open(stub_path, "w") as fp:
        parser = html2text.HTML2Text()
        fp.write(parser.handle(str(document)))


def stub_directory(dir=config):
    """For every subdirectory in `dir`, generate stub files"""
    dip.utils.walk(dir, functools.partial(generate_stub, config=config))
