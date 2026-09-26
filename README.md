# hello-actions
[![.github/workflows/workflow.yaml](https://github.com/gnumilanix/hello-actions/actions/workflows/workflow.yaml/badge.svg?branch=main)](https://github.com/gnumilanix/hello-actions/actions/workflows/workflow.yaml)
[![codecov](https://codecov.io/github/gnumilanix/hello-actions/graph/badge.svg?token=I1Q5IE3OI6)](https://codecov.io/github/gnumilanix/hello-actions)

Repository demonstrating GitHub Actions capabilities, including:
- Various dispatch triggers
- Sequential and parallel jobs
- Steps
- Permissions
- Service container for integration testing
- Docker build and publish to GitHub registry
- Trivy security scanning with exported reports
- Code coverage report with gates using Codecov
- Automatic release based on SemVer tags

It's also a fully-fledged Python pipeline, including:
- Linting with Ruff
- Unit tests
- Build
- Integration tests
- Docker builds