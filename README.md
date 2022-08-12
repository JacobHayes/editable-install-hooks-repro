# editable-install-hooks-repro
Reproduce static analysis tool issues with editable installs from setuptools v64:
- [python mailing list background](https://mail.python.org/archives/list/typing-sig@python.org/thread/IIVBPYDZR5T5BGPAWFVYS5ZPYDXGVHQN/#OSWHT5VSRGKPSPYD7PQWR2M4OCSL5WO3) (direct discussion here)
- https://github.com/pypa/setuptools/issues/3518
- https://github.com/python/mypy/issues/13392
- ... feel free to PR to add more

```sh
$ cd pkg2
$ python3 -m venv .venv
...
$ source .venv/bin/activate
...
$ pip3 install mypy pylint
...
$ pip3 install -e ../pkg1/  # Uses the *_finder.py file
...
$ mypy --namespace-packages --explicit-package-bases src
src/org/pkg2/__init__.py:1: error: Cannot find implementation or library stub for module named "org.pkg1"
src/org/pkg2/__init__.py:1: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
Found 1 error in 1 file (checked 1 source file)
$ pylint src/
************* Module org.pkg2
src/org/pkg2/__init__.py:2:0: E0611: No name 'pkg1' in module 'org' (no-name-in-module)

--------------------------------------------------------------------
Your code has been rated at 0.00/10

#### Now, go back to the old style editable installs and try again

$ pip3 uninstall org-pkg1
...
$ SETUPTOOLS_ENABLE_FEATURES="legacy-editable" pip3 install -e ../pkg1/  # Uses the *.egg-link file
...
$ mypy --namespace-packages --explicit-package-bases src
Success: no issues found in 1 source file
$ pylint src/

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

```
