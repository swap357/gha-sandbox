# gha-sandbox

debug GHA environment quirks

This repository contains a workflow that exercises `pygraphviz` on
GitHub Actions using both conda and pip installs. The `pygraphviz-test`
workflow runs automatically on pull requests and can also be triggered
manually. One job installs `graphviz` and `pygraphviz` via conda.
The other installs system packages with `apt` and then installs the
Python packages via `pip`. Use this workflow to verify that the shared
libraries required by `pygraphviz` are available on the Ubuntu runner.
