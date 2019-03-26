#!/usr/bin/env python3

# git auto save

from clara import ThirdShell
from pathlib import Path
import os


if ThirdShell.NoInternetConnected():
    pass
else:
    home = Path.home()
    os.chdir(home/'CloudStudio')

    ThirdShell.runCmdStrs(
        ['git add --all',
         'git commit -m "auto commit     by git-auto-save.py" ',
         ' git pull ',
         ' git push']
    )
