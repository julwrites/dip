(import pytest dit dit.documentation bs4 html2text)

(defn test_argument_parsing []
  (setv args (dit.parse_arguments ["-h"]))
  (print args))

(defn test_soup []
  (setv soup (bs4.BeautifulSoup "" "html.parser")
        test_tag (.new_tag (bs4.BeautifulSoup "" "html.parser") "h1")
        (. test_tag string) "something")
  (.append soup test_tag)
  (print soup))

(defn test_stub_directory []
  (setv parser (html2text.HTML2Text)
        document (dit.documentation._generate_stub ["foo" "bar" "baz"]))
  (print (.handle parser (str document)))
  (assert False))
