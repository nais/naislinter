# naislinter

A simple Python script to validate that your NAIS yaml file adheres to the NAIS specifications.

## Local installation

```bash
$ pip install naislinter
```

## Local usage

```bash
$ naislinter nais.yaml
```

Will print any path in the config tree that falls outside of the spec and return a non-zero code if any were encountered.

Returns 0 if the file is valid according to the NAIS specifications.