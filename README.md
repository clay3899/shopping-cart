"Shopping Cart" Project

> Prerequisites:
>   + [Python Language Overview](/units/unit-2.md)
>   + ["Groceries" Exercise](/exercises/groceries/README.md)
>   + ["List Comprehensions" Exercise](/exercises/list-comprehensions/README.md)
>   + [The `datetime` Module](/notes/python/modules/datetime.md)
>   + [Raising and Handling Errors](/notes/python/errors.md)


## Instructions

Please fork the repository. After forking the repository clone the repository with the instructions below.


## Setup

### Repo Setup

Use the GitHub.com online interface to clone a remote project repository called something like "shopping-cart". After this process is complete, you should be able to view the repo on GitHub.com at an address like `https://github.com/YOUR_USERNAME/shopping-cart`.

Use GitHub Desktop software or the command-line to download or "clone" it onto your computer. Choose a familiar download location like the Desktop.


### Directory Set up
After cloning the repo, navigate there from the command-line:

```sh
cd ~/Desktop/shopping-cart
```
### Environment Setup
After setting directory to ~/Desktop/shopping-cart, we need to create an shopping environment called shopping-env

```sh
conda create -n shopping-env python=3.7 #first time only


conda activate shopping-env

```

## Usage

### Installation
    
Within this environment, before running the program and adjusting tax, you should install the dotenv package with

```sh   
pip install python-dotenv #note: Not just "dotenv
```  

### Run the checkout process

```sh
python shopping_cart.py
```



### Local tax data

You may wish to put local tax data into the file.

Go to the .env file and adjust the tax rate as you desire