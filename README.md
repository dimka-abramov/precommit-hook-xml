[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)

# precommit-hook-xml

The repository contains hooks for XML files.

## Using pre-commit-hooks with pre-commit

Add this to your `.pre-commit-config.yaml`

```
-   repo: https://github.com/dimka-abramov/precommit-hook-xml
    rev: 1.0.11 # Use the ref you want to point at
    hooks:
    -   id: remove-leading-whitespaces
    -   id: format-xml
    -   id: remove-empty-lines
```

The hooks in this repository can be used to solve problem of big diffs for GnuCash XML files.
The example configuration file to run the checks on `your.gnucash` file.

```
repos:
-   repo: https://github.com/dimka-abramov/precommit-hook-xml
    rev: 1.0.11
    hooks:
    -   id: remove-leading-whitespaces
        files: your.gnucash
    -   id: format-xml
        types: [file]
        files: your.gnucash
    -   id: remove-empty-lines
        files: your.gnucash
```

## Hooks available

### remove-leading-whitespaces
The hook removes leading whitespaces from text files.

### format-xml
The hook formats the XML files and makes them pretty.

### remove-empty-lines
The hook removes lines only with space characters from text files.
