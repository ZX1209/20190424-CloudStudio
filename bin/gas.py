#!/usr/bin/env python3

# git auto save

from clara import ThirdShell
from pathlib import Path
import os


if ThirdShell.isNoInternetConnected():
    pass
else:
    home = Path.home()
    os.chdir(home/'CloudStudio')

    ThirdShell.RUN(
        ['git add --all', 'git commit -m "auto commit     by git-auto-save.sh" ', ' git pull ', ' git push'])
