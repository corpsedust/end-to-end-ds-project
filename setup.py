import setuptools

with open("README.md", "r", encoding = "utf-8") as f:
    long_description = f.read()
    
__version__ = "0.0.1"
    
repo_name= "end-to-end-ds-project"
author_user_name = "corpsedust"
src_repo = "ds_project"
author_email = "enivet0@gmail.com"


setuptools.setup(
    name = src_repo,
    version = __version__,
    author = author_user_name,
    author_email = author_email,
    description = "A small puthon package for ml app",
    long_description = long_description,
    long_description_content_type="text/markdown",
    url = f"https://github.com/{author_user_name}/{repo_name}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{author_user_name}/{repo_name}/issues"
    },
    package_dir = {"":"src"},
    packages = setuptools.find_packages(where = "src")
    
)

#why setup_tools : long and short answer is :
#Essentially, if you are working with creating and 
# distributing Python packages, it is very helpful.