# python

In Tools -> Build System choose `python3` - if it does not exist then read on.

Run python 3 in Sublime - https://towardsdatascience.com/run-python3-on-sublime-text-5949e55450b2

## pyenv

See [https://realpython.com/intro-to-pyenv/](https://realpython.com/intro-to-pyenv/)


#### Install python with brew & pyenv

```sh
brew install pyenv
pyenv install <version>
```

To select a version

```sh
pyenv local 3.5.0    // local version
pyenv global 3.5.0    // global version
```

To List versions

```sh
pyenv versions
```

As per the instructions in [https://realpython.com/intro-to-pyenv/](https://realpython.com/intro-to-pyenv/), add the following to ~/.bashrc: or ~/.zshrc

```sh
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
```

To list python version.

```sh
python -V
```

