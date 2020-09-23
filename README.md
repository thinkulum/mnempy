# Mnempy

Tools for creating a dictionary of mnemonic substitutes

## Table of contents

* [Synopsis](#synopsis)
* [Prerequisites](#prerequisites)
* [Downloading](#downloading)
* [Installing](#installation)
* [Documentation](#documentation)
* [Usage](#usage)
* [Development](#development)
* [Deployments](#deployments)
* [Testing](#testing)
* [Changelog](#changelog)
* [License](#license)
* [Authors](#authors)
* [Credits](#credits)

<a id="synopsis"></a>
## Synopsis

<a id="prerequisites"></a>
## Prerequisites

You'll need to have Python 3 installed. The rest of the requirements should be handled by the installation script.

<a id="downloading"></a>
## Downloading

<a id="installation"></a>
## Installation

```
$ pip install -r requirements.txt

$ pip install setup.py
```

<a id="documentation"></a>
## Documentation

The documentation is in `docs/source/index.rst`. To create a more readable version, from a command prompt in the `docs` directory run the command `make html`. The start page for that documentation will be `docs/build/html/index.html`.

<a id="usage"></a>
## Usage

<a id="development"></a>
## Development

This project includes a number of helpers in the `Makefile` to streamline common development tasks.

### Environment Setup

The following demonstrates setting up and working with a development environment:

```
### create a virtualenv for development

$ make virtualenv

$ source env/bin/activate


### run mnempy cli application

$ mnempy --help


### run pytest / coverage

$ make test
```

### Releasing to PyPi

Before releasing to PyPi, you must configure your login credentials:

**~/.pypirc**:

```
[pypi]
username = YOUR_USERNAME
password = YOUR_PASSWORD
```

Then use the included helper function via the `Makefile`:

```
$ make dist

$ make dist-upload
```

<a id="deployments"></a>
## Deployments

### Docker

Included is a basic `Dockerfile` for building and distributing `Mnempy`,
and can be built with the included `make` helper:

```
$ make docker

$ docker run -it mnempy --help
```

<a id="testing"></a>
## Testing

From a command prompt in the project directory, run the command `pytest` to automatically run all the tests.

<a id="changelog"></a>
## Changelog

<a id="license"></a>
## License

This project uses the MIT license. See the file `LICENSE.md` for details.

<a id="authors"></a>
## Authors

* Andy Culbertson (thinkulum@gmail.com) - original author

<a id="credits"></a>
## Credits

This package was created with [Cement](https://builtoncement.com/).
