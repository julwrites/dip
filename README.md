  * [dip](./dip)

  * [test](./test)

  * [.gitignore](./.gitignore)

  * [config.doc.yaml](./config.doc.yaml)

  * [conftest.py](./conftest.py)

  * [main.py](./main.py)

  * [README.md](./README.md)

  * [requirements.txt](./requirements.txt)

* * *

* * *

## Brief:

We propose an automated documentation helper in git ( _dip_ ) consisting of

the following parts:

  * MVS

    * Repository Linting

    * Automated linting of a repository's documentation

  * Repository Stubbing

    * Automated creation of documentation stubs in the target repository
  * Stretch

    * Report Generation

    * Automated generation of a repository-wide overview based on repository history and existing documentation

    * Documentation Indexing

    * Automated generation of a repository wiki using documentation

We would like _dip_ to be deployable on any repository (perforce, git, svn

mercurial, etc...) and provide the same value to all

## Solution

### Tech Stack

  * Git: Provide repository and change history

### High Level Design

#### Stub

  * Documentation stubs are generated if a folder is found without a recognized (`README.md`) documentation markdown file

  * Documentation stubs will contain an automatically populated breadcrumb trail and child listings 

#### Lint

  * If the stub does not exist, Documentation lint will flag this as `Warning: Documentation is missing`

  * If the documentation markdown file has no auto-generated header, Documentation lint will flag this as `Warning: Documentation has no managed header`

## Setup

### Requirements

  * Git should be installed

  * Python 3.7.3 should be installed with `pip`

  * Run `pip install -r requirements.txt`

### Running Dit

  * Use `python bootstrap.py` to lint and document the existing directory

  * To specify a directory, use `python bootstrap.py <dir>`

  * To specify a config file, use `python bootstrap.py <dir> <cfg>`