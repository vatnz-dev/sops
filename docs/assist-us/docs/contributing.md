---
  title: Contributing
---

--8<-- "includes/abbreviations.md"

The Operations Team actively welcomes new contributions to the Project, and has aimed to make it as easy as possible for members of the Community to help out.

## Requirements

Contributions can be made on any platform that is supported by MkDocs - at the moment limited to Windows, Mac and Linux. This walkthrough is specifically targeted toward Windows users.

In order to contribute, you'll need to have the following tools installed:

* A GitHub account and Git - ([GitHub Quickstart](https://docs.github.com/en/get-started/quickstart){ target=_blank })
* The latest version of Python - ([Install Python](https://www.python.org/downloads/){ target=_blank })
* An Editor / IDE:
    * We recommend [Visual Studio Code](https://code.visualstudio.com/){target=blank}, with the following plugins:
        * Any Markdown helper
        * Any Markdown Table tool
* The following Python tools:
    * mkdocs
    * mkdocs-material
    * mkdocs-awesome-pages-plugin
    * mkdocs-git-revision-date-localized-plugin
    * mkdocs-redirects
    * mkdocs-video
    * pillow
    * cairosvg

!!! info
    These packages can be installed easily through a single command:

    ``` python
      pip install -r requirements.txt
    ```

## Setting up the project

### Preview your local clone

* Fork the [:fontawesome-brands-github:{: .github } -  **SOPs Project**](https://github.com/vatnz-dev/sops){target=new} - ([How to fork a repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo){target=new})
* Create a local clone.
* Checkout the main branch, which is the most up to date version of the project.
* In a command line terminal, navigate to the cloned repository folder and enter `mkdocs serve` to start the local preview server.
    * You will then see a lot of text whizzing by on your command prompt. Eventually, you'll see that it is serving the website on `localhost:8000`.

!!! danger "Serve command error"
    Sometimes the above `serve` command will throw an error. This is due to your computer not being able to find the exact location of the MkDocs module on your computer. If this is the case, use the following command instead:

    ``` python
      python -m mkdocs serve
    ```

    If you need to use any other MkDocs command line instructions, you should also add `python -m` to the start of it.

!!! info "Faster Preview Server"
    You can opt to use a faster instance of the developer server by using the flag `--dirtyreload`. This just checks for any markdown that has changed since the HTML was rendered and will only reconstruct the effected pages, rather than the whole site.

    `mkdocs serve --dirtyreload`

### Making Changes or Additions to the SOPs

* Create a new branch based off the main branch, and checkout this branch. Make sure you give a short and meaningfull name to the branch.
* Make your changes to the branch.
* Create a Pull Request (PR) early on to let people know that you're working on a feature.
    * Explain in the PR what you are changing or adding, and reference a GitHub issue where appropriate.
* Work on your changes locally, preview constantly and push your changes regularly to allow others to see your work.
* When finsished, push your final changes to the PR, update the PR description if required, and mark your PR as "Ready for review".


### Deployment Pipeline

!! TODO: Explain how deployment works once I've figured it out


