import os
import sys
import hy
import dip
import dip.utils
import dip.lint
import dip.documentation


def run(repo, config="dipstick.yaml"):
    cfg = dip.utils.readconfig(config)

    dip.lint.lint_directory(repo, cfg)

    if cfg["auto_fix"] == True:
        dip.documentation.stub_directory(repo, cfg)


if __name__ == "__main__":
    root = "."
    config = "dipstick.yaml"

    if len(sys.argv) > 1:
        root = sys.argv[1]
    if len(sys.argv) > 2:
        config = sys.argv[2]

    run(root, config)
