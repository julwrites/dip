import pytest
import dit
import dit.documentation
import bs4
import html2text

def test_argument_parsing():
    args = dit.parse_arguments("-h")
    print(args)

def test_soup():
    soup = bs4.BeautifulSoup("", "html.parser")
    test_tag = bs4.BeautifulSoup("", "html.parser").new_tag("h1")
    test_tag.string = "something"

    soup.append(test_tag)

    print soup

def test_stub_directory():
    parser = html2text.HTML2Text()
    document = dit.documentation._generate_stub("foo", "bar", "baz")

    print(parser.handle(str(document)))

    assert False