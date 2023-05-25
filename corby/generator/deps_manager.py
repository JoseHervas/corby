"""Manages a virtual environment and installs dependencies"""

import os
import sys
import subprocess

class DependencyManager:
    """Manages a virtual environment and installs dependencies"""

    def __init__(self, app_path, virtual_dir):
        self.virtual_dir = virtual_dir
        self.virtual_python = os.path.join(app_path, self.virtual_dir, "bin", "python")

    def install_virtual_env(self):
        """Creates the virtualenv if it doesn't exist"""
        self.pip_install("virtualenv")
        if not os.path.exists(self.virtual_python):
            subprocess.call([sys.executable, "-m", "virtualenv", self.virtual_dir])

    def is_venv(self):
        """Checks if virtualenv exists"""
        return sys.prefix == self.virtual_dir

    def pip_install(self, package):
        """Installs packages programmatically"""
        try:
            __import__(package)

        except ImportError:
            subprocess.call([sys.executable, "-m", "pip", "install", package, "--upgrade"])

    def install_dependencies(self, requirements_path):
        """Installs all the required dependencies under the virtualenv"""
        subprocess.call([self.virtual_python, "-m", "pip", "install", "-r", requirements_path])
