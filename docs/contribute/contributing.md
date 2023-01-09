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
* Install the following Python packages: `mkdocs-material`, `mkdocs-awesome-pages-plugin`, `mkdocs-git-revision-date-localized-plugin` and `mkdocs-redirect`.

!!! info
    These packages can be installed easily through a single command:

    ``` python
      pip install -r requirements.txt
    ```



* Once you've installed those, open a command line terminal, `cd` into the cloned repository folder and enter start the MkDocs service:

```
    mkdocs serve
```

??? danger "Serve command error"
    Sometimes the above `serve` command will throw an error. This is due to your computer not being able to find the exact location of the MkDocs module on your computer. If this is the case, use the following command instead:

    ``` python
      python -m mkdocs serve
    ```

    If you need to use any other MkDocs command line instructions, you should also add `python -m` to the start of it.

??? info "Faster Preview Server"
    You can opt to use a faster instance of the developer server by using the flag `--dirtyreload`. This just checks for any markdown that has changed since the HTML was rendered and will only reconstruct the effected pages, rather than the whole site.

    `mkdocs serve --dirtyreload`




