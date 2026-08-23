---
  title: Setting Up
---

--8<-- "includes/abbreviations.md"

!!! tip
    If you have any questions about setting up your development environment for these SOPs, or you get stuck - feel free to reach out to the Operations Team.

## Requirements

To contribute, you'll need the following -

* A basic code editor or IDE.
    * We recommend [Visual Studio Code](https://code.visualstudio.com/){target=blank}, with a Markdown helper plugin.
* A GitHub account, and a local Git environment - [GitHub Quickstart](https://docs.github.com/en/get-started/quickstart){ target=_blank }
* [uv](https://docs.astral.sh/uv/){ target=_blank } - the tool we use to manage Python and our project dependencies.

Install `uv` with the command for your platform:

``` py title="Windows - Run in PowerShell"
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

``` py title="macOS / Linux - Run in Terminal"
  curl -LsSf https://astral.sh/uv/install.sh | sh
```

!!! info "You don't need to install Python"
    The project pins its Python version in the `.python-version` file. `uv` reads that file and downloads the correct version (currently 3.12) for you, so there's no need to install Python separately.

!!! tip "Using mise"
    If you already use [mise](https://mise.jdx.dev/){ target=_blank }, run `mise install` in the repository folder instead. Our `mise.toml` provisions Python 3.12, `uv`, and the project's virtual environment for you. Then carry on from `uv sync` below.


## Lets do it!

* Fork and clone the [:fontawesome-brands-github:{: .github } -  **SOPs Project**](https://github.com/vatnz-dev/sops){target=new} - [Guide](https://docs.github.com/en/get-started/quickstart/fork-a-repo){target=new}
* Open a command line terminal, `cd` into the cloned repository folder, and install the project:

``` py title="Run in Command Line / Terminal"
  uv sync
```

This creates a `.venv` folder inside the repository and installs the exact package versions recorded in `uv.lock` - so everybody is working with an identical set of dependencies. Our package list lives in `pyproject.toml`, and you should never need to install anything by hand.

!!! info "Cairo and Pillow dependency"
    As a part of the social card feature, the [Pillow](https://pillow.readthedocs.io/){ target=_blank } and [Cairo Graphics](https://www.cairographics.org/){ target=_blank } dependencies are declared in our `pyproject.toml`. This ensures the dependencies are installed when attempting to [test social card generation](#social-cards) locally.

    If you encounter any trouble:

      * Install a [GTK+ runtime](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases){ target=_blank } for Windows.


* Once that's done, start the MkDocs service:

``` py title="Run in Command Line / Terminal"
  uv run mkdocs serve
```

!!! tip "Why `uv run`?"
    Prefixing a command with `uv run` runs it inside the project's virtual environment. It also keeps that environment in sync with `uv.lock` beforehand, so you'll pick up dependency changes automatically after pulling. Any other MkDocs command line instruction should be prefixed the same way.

!!! info "Faster Preview Server"
    You can opt to use a faster instance of the developer server by using the flag `--dirtyreload`. This just checks for any markdown that has changed since the HTML was rendered and will only reconstruct the effected pages, rather than the whole site.

    `uv run mkdocs serve --dirtyreload`


## Social Cards

!!! warning "You do not need to test this feature!"
    In general use, you will not need to test or utilize this feature, unless you are actively developing or changing the configuration. It is tedious to set up, and will be automatically run during the deploy workflow. 

    If you **need** to test this feature, you can follow these instructions.

The SOPs site uses the Social Cards feature provided by Material for MkDocs. When generating these cards locally, these cards are generated and stored in `/.cache/plugin/social`.

The normal `mkdocs.yml` that maintainers will run when testing locally does not include this feature by default, and must be manually included when either building, or needing to test the plugin.

* To test the plugin when testing locally: `uv run mkdocs serve --config-file production.yml`

* To include the plugin during a deploy build: `uv run mkdocs build --config-file production.yml`

`production.yml` includes an `INHERIT` function, which essentially merges the two files together for a build deployment.
