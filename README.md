# naislinter

A simple Python script to validate that your NAIS yaml file adheres to the NAIS specifications.

## GitHub Action

To set up this as a GitHub Action, add the following as a step in your workflow:

```yaml
    - name: naislint nais.yaml
      uses: nais/naislinter@v1.0.2
      env:
        RESOURCE: nais.yaml
```

The action follows the same footprint as [`nais/deploy`](https://doc.nais.io/deployment#deploy-with-github-actions)
for injecting variables to templates, however some environment variables are not required, such as `APIKEY`, `CLUSTER`.

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


## Limitations

This does not validate value types, this is not in scope as `nais/deploy` verifies types and rejects
a deployment if the NAIS yaml file is malformed in this fashion.

Additionally, this tool requires a fully formed NAIS yaml file, after any template injections.
A file containing `{{ image }}` will therefore fail, unless the variable has been injected.

Finally, in its current state, the tool is unable to verify objects within lists. For instance:

```yaml
spec:
    env:
        - name: KEY
          value: value
        - name: ANOTHER_KEY
          value: another_value
          key_outside_of_spec: hello!
```

`key_outside_of_spec` will not be caught as an error since it's in an object within a list.
