# SEC460 LAB4: Dependency Scanning with Snyk

- Student: ChinEnCheng
- Date: 2026/05/10
- Lab: LAB4

This small Python project is intentionally prepared with an outdated dependency
so that the initial Snyk scan can demonstrate Software Composition Analysis.

## Initial scan state

The `requirements.txt` file pins `urllib3` to version `1.26.4`. Do not update the
version until the initial repository has been imported into Snyk and the initial
dashboard result has been captured.

## Planned remediation

After reviewing Snyk's recommendation, update `urllib3` to the recommended safe
version, commit the change, push it to GitHub, and re-scan the project in Snyk.
