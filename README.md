# hello-actions
[![.github/workflows/workflow.yaml](https://github.com/gnumilanix/hello-actions/actions/workflows/workflow.yaml/badge.svg?branch=main)](https://github.com/gnumilanix/hello-actions/actions/workflows/workflow.yaml)

Repository demonstrating GitHub Actions capabilities, including:
- Various dispatch triggers
- Sequential and parallel jobs
- Steps
- Permissions
- Service container for integration testing
- Docker build and publish to GitHub registry
- Trivy security scanning with exported reports
- Code coverate report with gates using Codecov
- Automatic release based on SemVer tags

It's also a fully-fledged Python pipeline, including:
- Linting with Ruff
- Unit tests
- Build
- Integration tests
- Docker builds