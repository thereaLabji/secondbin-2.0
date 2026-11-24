# SecondBIN 2.0 (sBIN)

SecondBIN is Secrip's custom, extensible command-line terminal. This repository is the clean 2.0 rebuild.

## Development status

The first bootstrap milestone provides:
- An interactive terminal prompt (`sBIN>`)
- A command registry
- Built-in commands: `help`, `clear`, `echo`, `version`, `date`, `time`, `pwd`, `ls`, `cd`, and `exit`
- A Python package and console entry point

The canonical Python API is `secrip.products.secondbin`. For example:

```python
from secrip.products import secondbin as sbin
```

The older top-level `secondbin` import remains as a compatibility layer.

## Requirements

- Python 3.10 or newer

## Run from source

PowerShell:

```powershell
py -m pip install -e .
sbin
```

Or without installing:

```powershell
$env:PYTHONPATH = "src"
py -m secrip.products.secondbin
```

## Original addon compatibility notes

The recovered addon example used `AddonInit.py`, `SBIN.container.xml`, and the `secrip.products.secondbin` API. Its manifest demonstrated `InitQueue=BeforeSystem`.

The six remembered `InitQueue` values are:
- `BeforeSystem`
- `AfterSystem`
- `BeforeApp`
- `AfterApp`
- `BeforeInit`
- `AfterInit`

These are documented as supported values only. Their exact execution semantics will be specified from the original design notes before the addon loader is implemented.

## Planned components

- **sBIN Core:** terminal, command registry, configuration
- **sBIN Addons:** manifest, loader, lifecycle hooks, addon API
- **KPT:** package and dependency manager
- **Clod3:** Cloudflare-hosted package and update services
- **Licensing:** application license activation and verification

## Security

Python addons execute code with the permissions of the user running sBIN. Only install addons from sources you trust. License verification secrets will remain server-side; no private signing key will be embedded in the executable.
