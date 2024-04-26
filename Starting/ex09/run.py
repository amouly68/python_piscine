import sys
import os


def build_package():
    """Build the package."""
    os.system("python3 setup.py sdist bdist_wheel")


def clear_package():
    """Clear the built package files."""
    os.system("rm -rf dist")
    os.system("rm -rf build")
    os.system("rm -rf ft_package.egg-info")
    os.system("rm -rf ft_package/__pycache__")
    os.system("pip uninstall ft_package")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py [build|clear]")
        sys.exit(1)

    action = sys.argv[1]

    if action == "build":
        build_package()
    elif action == "clear":
        clear_package()
    elif action == "install":
        os.system("pip install dist/ft_package-0.0.1-py3-none-any.whl")
    elif action == "test":
        os.system("python3 tester.py")
    elif action == "show":
        os.system("pip show -v ft_package")
    else:
        print("Unknown action. Please specify 'build' or 'clear'.")
