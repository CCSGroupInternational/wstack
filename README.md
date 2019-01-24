WSTack
======

[![PyPI](https://img.shields.io/pypi/v/wstack.svg)](https://pypi.python.org/pypi/wstack)
[![PyPI version](https://img.shields.io/pypi/pyversions/wstack.svg)](https://pypi.python.org/pypi/wstack)
[![Documentation](https://img.shields.io/badge/docs-latest-brightgreen.svg)](https://miyakogi.github.io/wstack)
[![Build Status](https://travis-ci.org/miyakogi/wstack.svg?branch=master)](https://travis-ci.org/miyakogi/m2r)
[![codecov](https://codecov.io/gh/miyakogi/wstack/branch/master/graph/badge.svg)](https://codecov.io/gh/miyakogi/m2r)

--------------------------------------------------------------------------------

WStack provides an integration framework for Python based web applications.

## Why another Python Web Framework?

WStack is not a web development framework per si, it is a middleware framework that can integrate diverse WSGI compliant application frameworks, middleware and servers. It is a pure Python tool without external library dependencies, it can be easily deployed into any Python supported platform.

## Planned Features

- Web Stack
    - Declarative definition for a group of WSGI applications and middleware:
        - Explicit routing
        - Automatic path name based routing
        - Pre-processing bindings:
            - Session management
            - Authentication/authorization
            - Caching
        - Post-processing bindings:
            - Logging
            - Performance metrics

- Web Stack Runtime Engines
    - Run "Web Stacks" using a plugin based WSGI server:
        - wsgiref: Standard Python WSGI reference implementation
        - cheroot: pure-Python HTTP server used by CherryPy

## Examples:
`wstack run uaa-with-api.json`
```json
{
    "description": "cf-micro UAA+API ",
    "apps":
        [
            {
                "path" : "/",
                "module": "webroot.index"
            },
            {
                "path" : "/api",
                "package": "api",
                "auto_routing": true,
                "pre-processing": [
                    "pre.authentication"
                ]
            },
            {
                "path" : "/uaa",
                "package": "uaa",
                "auto_routing": true
            }
        ],
    "post-processing":
        [
            "post.logging"
        ]
}
```
