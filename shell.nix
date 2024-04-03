let
  pkgs = import <nixpkgs> {};
in
  pkgs.mkShell {
    packages = [
      (pkgs.python3.withPackages (python-pkgs: [
        python-pkgs.appdirs
        python-pkgs.black
        python-pkgs.flake8
        python-pkgs.isort
        python-pkgs.pylint
        python-pkgs.pytest
        python-pkgs.setuptools
      ]))
    ];
    shellHook = ''
      python -m venv .venv
      source .venv/bin/activate
      pip install ofxstatement
      export PYTHONPATH=$(ls -d $(pwd)/.venv/lib/python3.*/site-packages)
    '';
  }
