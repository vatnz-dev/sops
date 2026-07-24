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
* The latest version of Python - [Install Python](https://www.python.org/downloads/){ target=_blank }


## Lets do it!

* Fork and clone the [:fontawesome-brands-github:{: .github } -  **SOPs Project**](https://github.com/vatnz-dev/sops){target=new} - [Guide](https://docs.github.com/en/get-started/quickstart/fork-a-repo){target=new}
* Install the following Python packages: 
    * `mkdocs-material`
    * `mkdocs-awesome-pages-plugin`
    * `mkdocs-git-revision-date-localized-plugin`
    * `mkdocs-redirect`
    * `mkdocs-glightbox`
    * `cairosvg`
    * `pillow`
* Install with this single command:

``` py title="Run in Command Line / Terminal"
  pip install -r requirements.txt
```


!!! info "Cairo and Pillow dependency"
    As a part of the social card feature, the [Pillow](https://pillow.readthedocs.io/){ target=_blank } and [Cairo Graphics](https://www.cairographics.org/){ target=_blank } dependencies were added. We bundle these into our `requirements.txt` to ensure the dependencies are installed when attempting to [test social card generation]() locally.

    If you encounter any trouble:

      * Install a [GTK+ runtime](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases){ target=_blank } for Windows.


* Once you've installed those, open a command line terminal, `cd` into the cloned repository folder and enter start the MkDocs service:

```
    mkdocs serve
```

!!! danger "Serve command error"
    Sometimes the above `serve` command will throw an error. This is due to your computer not being able to find the exact location of the MkDocs module on your computer. If this is the case, use the following command instead:

    ``` python
      python -m mkdocs serve
    ```

    If you need to use any other MkDocs command line instructions, you should also add `python -m` to the start of it.

!!! info "Faster Preview Server"
    You can opt to use a faster instance of the developer server by using the flag `--dirtyreload`. This just checks for any markdown that has changed since the HTML was rendered and will only reconstruct the effected pages, rather than the whole site.

    `mkdocs serve --dirtyreload`


## Social Cards

!!! warning "You do not need to test this feature!"
    In general use, you will not need to test or utilize this feature, unless you are actively developing or changing the configuration. It is tedious to set up, and will be automatically run during the deploy workflow. 

    If you **need** to test this feature, you can follow these instructions.

The SOPs site uses the Social Cards feature provided by Material for MkDocs. When generating these cards locally, these cards are generated and stored in `/.cache/plugin/social`.

The normal `mkdocs.yml` that maintainers will run when testing locally does not include this feature by default, and must be manually included when either building, or needing to test the plugin.

* To test the plugin when testing locally: `mkdocs serve --config-file production.yml`

* To include the plugin during a deploy build: `mkdocs build --config-file production.yml`

`production.yml` includes an `INHERIT` function, which essentially merges the two files together for a build deployment.
