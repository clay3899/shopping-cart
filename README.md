"Shopping Cart" Project

> Prerequisites:
>   + [Python Language Overview](/units/unit-2.md)
>   + ["Groceries" Exercise](/exercises/groceries/README.md)
>   + ["List Comprehensions" Exercise](/exercises/list-comprehensions/README.md)
>   + [The `datetime` Module](/notes/python/modules/datetime.md)
>   + [Raising and Handling Errors](/notes/python/errors.md)

## Learning Objectives

  1. Create a tool to facilitate and streamline a real-world business process.
  2. Practice processing and validating user inputs in Python.
  3. Reinforce introductory Python programming language concepts such as datatypes, functions, variables, and loops.
  4. Practice incorporating version control into your development process.
  5. Optional Challenge: Practice incorporating automated testing into your development process.

## Business Prompt

Your local corner grocery store has hired you as a technology consultant to help modernize their checkout system.

Currently, when managing inventory, store employees affix a price tag sticker on each grocery item in stock. And when a customer visits the checkout counter with their selected items, a checkout clerk uses a calculator to add product prices, calculate tax, and calculate the total amount due.

Instead, the store owner describes a desired checkout process which involves the checkout clerk scanning each product's barcode to automatically lookup prices, perform tax and total calculations, and print a customer receipt. To facilitate this process, the store owner has authorized the purchase of a few inexpensive barcode scanners, as well as checkout computers capable of running Python applications.

The store owner says it would be "acceptable but not preferable" to manage the inventory of products via the application's source code, that it would be "better" to manage the inventory of products via a local CSV file stored on the checkout computer, and that it would be "ideal" to be able to manage the inventory of products via a centralized Google Sheet spreadsheet document.

The store owner also says it would be "nice to have" a feature which prompts the checkout clerk or the customer to input the customer's email address in order to send them a receipt via email.

## Instructions

Iteratively develop a Python application which satisfies the store owner's objectives, as described in more detail by the "Basic Requirements" below.

Before attempting to implement the basic requirements, take some time to configure your project repository according to the "Setup" instructions below. After doing so, you'll have a remote repo on GitHub.com and a local copy on your computer within which to develop.

When developing, as you reach key milestones, use the command-line or GitHub Desktop software to intermittently "commit", or save new versions of, your code. And remember to push / sync / upload your work back up to your remote project repository on GitHub.com at least once before you're done.

If you are able to implement the basic requirements with relative ease, or if you are interested in a challenge, consider addressing one or more of the "Further Exploration Challenges". Otherwise, if you need help breaking the problem up into more manageable pieces, consult the "Guided Checkpoints". And if you would like a narrated walkthrough, consult the "Guided Screencast".

## Setup

### Repo Setup

Use the GitHub.com online interface to create a new remote project repository called something like "shopping-cart". When prompted by the GitHub.com online interface, let's get in the habit of adding a "README.md" file and a Python-flavored ".gitignore" file (and also optionally a "LICENSE") during the repo creation process. After this process is complete, you should be able to view the repo on GitHub.com at an address like `https://github.com/YOUR_USERNAME/shopping-cart`.

After creating the remote repo, use GitHub Desktop software or the command-line to download or "clone" it onto your computer. Choose a familiar download location like the Desktop.

After cloning the repo, navigate there from the command-line:

```sh
cd ~/Desktop/shopping-cart