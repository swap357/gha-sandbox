# gha-sandbox

debug GHA environment quirks

This repository contains a workflow that exercises `pygraphviz` on
GitHub Actions using both conda and pip installs. Run the `pygraphviz-test`
workflow manually to check whether the shared libraries required by
`pygraphviz` are available on the Ubuntu runner.
