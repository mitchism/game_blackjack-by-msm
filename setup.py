from setuptools import setup, find_packages
import pathlib

#with open("README.md", "r") as readme_file:
#    readme = readme_file.read()
here = pathlib.Path(__file__).parent.resolve()
readme = (here / "README.md").read_text(encoding="utf-8")

requirements = ["ipython"]

setup(
    name="game_blackjack-by-msm",
    version="1.0.1a", 
    #ver 1.3.1.2 first stable alpha iteration
    #ver 1.4 upon merge of single player feature branch
    author="Mitch Miller",
    author_email="mitchell.shaw.miller@gmail.com",
    description="Blackjack console game in Python by MSM",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/mitchism/game_blackjack-by-msm",
    packages=find_packages(),
    install_requires=requirements,
    project_urls={  # Optional
        "project GitHub": "https://github.com/mitchism/game_blackjack-by-msm",
        "author url": "http://mitchellsmiller.weebly.com/",
    },
    classifiers=[
        "Classifier: Environment :: Console (Text Based)",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Development Status :: 3 - Alpha", #(3-alpha,4-beta,5-production/stable)
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.9.7",
    ],
    keywords="Blackjack, Single player, Game, Console Game, Text based game",  # Optional
    
    python_requires=">=3.7, <4",
)
