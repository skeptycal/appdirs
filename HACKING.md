# HACKING

## release

ensure correct version in CHANGES.md and appdirs.py, and:

```
# old way ...
python setup.py register sdist bdist_wheel upload
```
Pypi server responds with error 410:

```
Registering appdirs to https://upload.pypi.org/legacy/
Server response (410): Project pre-registration is no longer required or supported, upload your files instead.
```
do not use `register` command; instead use upload directly (with recommended python -m launcher)

```
# new ...
python -m setup sdist bdist_wheel upload
```

to install in dev mode use:

```
python -m setup sdist bdist_wheel develop
```


## docker image

```
docker build -t appdirs .
```

