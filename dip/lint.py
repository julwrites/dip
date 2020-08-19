import os
import bs4
import functools
import markdown
import dip.utils
import dip.documentation


def _parse_stub(file):
    """Parse a markdown file into BeautifulSoup HTML document"""
    return bs4.BeautifulSoup(markdown.markdown(dip.utils.read(file)),


def stub_header(document):
    """Header is always an unordered list of children"""
    children = document.findChildren()
    children.first.name = "ul"
    return children


def lint_stub(root, dirs, files, config):
    """Lint the stub with all files or dirs that are not marked as ignore"""
    stub_path = os.path.join(root, "README.md")
    ignore = config.get("ignore")
    document = None
    glob = []

    for x in ignore:
        if (x in root):
            return

    for x in dirs:
        if not x in ignore:
            glob.append(x)

    for x in files:
        if not x in ignore:
            glob.append(x)

    document = _parse_stub(stub_path) if os.path.exists(stub_path) else None

    if document is not None:
        if document is not stub_header:
            print("Warning: Documentation in {} has no managed header.".format(
                stub_path))
        print("Warning: Documentation in {} is missing.".format(stub_path))


def lint_directory(dir=config):
    """For every subdirectory in `dir`, lint stub files"""
    dip.utils.walk(dir, functools.partial(lint_stub, config=config))
