from setuptools import find_namespace_packages, setup

setup(
    name="org-pkg2",
    version="0.0.1",
    packages=find_namespace_packages(include=["org.*"], where="src"),
    package_dir={"": "src"},
    package_data={"org.pkg2": ["py.typed"]},
    python_requires=">=3.9",
    zip_safe=False,
)
