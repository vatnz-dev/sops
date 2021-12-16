# Management of our SOPs

The Standard Operating Procedures Refresh project aims to provide easily accessible and high quality SOPs to the Community, enabling both Pilots and Controllers to excel in the New Zealand Flight Information Regions.

We readily welcome collaboration from members of the Community on these SOPs, and encourage members of the Community to make these SOPs their own.

## What we're looking for

We're well aware that members of the Community flock to VATSIM for different reasons. Some want to imitate the real-world as close as possible, whereas some are here just to have fun with a different hobby.

When contributing to the SOPs Project, it's important to understand the practical limitations of the network. 

There are some aspects of Controlling that we might not want to implement because it adds too many unnecessary complications, such as low-visibility and noise abatement procedures. Because of this, we ask you to have a chat to the Operations Team in the [:fontawesome-brands-discord:{: .discord } - **VATNZ Discord**](https://www.vatnz.net/discord/){target=new} before you get too into it.




## How to Contribute

You don't need to have an in-depth knowledge of programming to contribute to this project - as most of our documentation pages are written in [Markdown](https://www.markdownguide.org/){target=new}. Everything else will be explained in this section.

!!! important
    If you have any questions about setting up your development environment for these SOPs or get stuck, please reach out to the **Operations Team**.

### Tools

There's a little bit of setup required, but these instructions will get you going in no time.


* Setup a GitHub account, and your local Git environment ([Github Quickstart Guide](https://docs.github.com/en/get-started/quickstart){target=new})
* Setup Python ([Python](https://www.python.org/downloads/){target=new})
* Install the following Python-based packages:
     * MkDocs
     * mkdocs-material
     * mkdocs-git-revision-date-localized-plugin
     * mkdocs-awesome-pages-plugin

!!! info "Easy Python Package Installing"
    These packages can be installed easily through a single command. 

    ```
      pip install -r requirements.txt
    ```

    !!! danger ""
        You'll still need to ensure you have Python installed first, as these use **pip** - the Python Package Installer.

* Make sure you've got a Code Editor / IDE installed on your system.
    * We recommend [VS Code](https://code.visualstudio.com/){target=new}, with a Markdown helper plugin.
  

### Setup your local Development Environment

- Fork and clone the [:fontawesome-brands-github:{: .github } -  **SOPs Project**](https://github.com/flybywiresim/docs){target=new} ([How to fork a repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo){target=new}).
- In a command line terminal, navigate to the cloned repository and run the MkDocs serve command to start the local development server.

```
> mkdocs serve
```

- Give it a few seconds, and you'll soon be notified that MkDocs is `Serving on http://127.0.0.1:8000/`. Open up your web browser, and head to that address.

!!! info
    MkDocs converts your Markdown into HTML on every save - so when you make changes and save it, it may take a little bit to re-render the website and serve it to you locally.


### Make your Changes

!!! tip
    As a general rule of thumb, it's not a good idea to make changes directly to the `main` branch of the repo. When you're working on the SOPs, we ask that you create a new branch that we can then merge into `main`. 

    This also makes the Operation Team's life easier when reviewing your pull request.

- Create a new branch based off the `main` branch. Make the branch name short, yet descriptive. Maybe `typo-fixes`, or `greymouth`,  if you were adding Greymouth procedures, for example.
- Make your changes.
- Create a [Pull Request](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-forkhttps://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork){target=new} early on, to let people know that you're working on a project. 
    - Make sure you explain in the Description exactly what you're doing.
    - As you work on your changes locally, make sure that you regularly commit and push your code so that other people can give you feedback as you work. 
- When you've finished, ensure all of your work has pushed to your PR, and mark your PR as 'Ready for Review'.
- Somebody from the Operations Team will then review your PR, give you feedback or potentially ask for changes, before approving and merging you changes.


## Working with MkDocs

!!! hint
    If you've got the space, have your web browser and code editor side-by-side. This means that as you make changes and save, these are immediately reflected in front of you.

You can find documentation for [MkDocs here](https://squidfunk.github.io/mkdocs-material/reference/abbreviations/){target=new}. 

All of MarkDown's default syntax is supported by MkDocs, including links, images, etc. It's also got some pretty nifty features, which assist in writing documentation.

### Links

Links that navigate a user through the Documentation site can follow the normal Markdown convention. However, all links that take a user away from the Documentation site should have `{target=new}` appended.

``` markdown
[Internal Link](/enroute/)
[External Link](https://vatnz.net){target=new}
```

### Admonitions

Admonitions are enabled in this project, with all types being supported. Have a look at the [Admonitions page on MkDocs](https://squidfunk.github.io/mkdocs-material/reference/admonitions/){target=new} for usage information.

We try not to use these too much, as they can potentially distract a user's reading flow.

### Buttons

Buttons should be used sparingly, if at all. Inline text links are the preferred method of user interaction.

### Images

If context needs to be added, then an image is the key way to go. Images should be clearly readable. You should **always** specify whether the image is aligned to the left or right, and lazy loaded should not be enabled.

More information on image usage can be found on the [MkDocs website](https://squidfunk.github.io/mkdocs-material/reference/images/#image-alignment){target=new}.

