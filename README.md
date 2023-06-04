# py-dd-trace
Simple python hello world page without modifying logs but trace id is auto injected into logs

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![GitHub Issues](https://img.shields.io/github/issues/streamworx/py-dd-trace.svg)](https://github.com/streamworx/py-dd-trace/issues)
[![GitHub Stars](https://img.shields.io/github/stars/streamworx/py-dd-trace.svg)](https://github.com/streamworx/py-dd-trace/stargazers)

**py-dd-trace** is a Python library that provides distributed tracing support for applications using the Datadog APM (Application Performance Monitoring) system. It enables you to trace requests as they propagate through your distributed system, allowing you to gain insights into performance bottlenecks and dependencies.

## Features

- Automatic instrumentation of supported libraries and frameworks for tracing requests and capturing spans.
- Trace context propagation across different services and systems.
- Integration with the Datadog APM system for collecting and visualizing traces.

## Installation

You can install `py-dd-trace` using pip:

```bash
pip install ddtrace
