# sonarqube-e2e-monorepo

A test fixture for Trent's SonarQube Cloud connector. SonarQube analyses only
`services/api` (`sonar.projectBaseDir`), so its findings name paths relative to
that folder and Trent must root them at `services/api/`. The weakness in
`services/web` sits outside the analysis and must never reach Trent. Every
weakness is planted and made up.
