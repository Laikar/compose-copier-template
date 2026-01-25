<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<summary>Table of contents</summary>

- [Docker Compose Template Generator](#docker-compose-template-generator)
  - [Features](#features)
  - [Usage](#usage)
  - [Roadmap](#roadmap)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Docker Compose Template Generator

A **Copier template** for bootstrapping docker(or podman)compose projects with soem defaults.

This template generates my prefered configurations for selfhosting apps using docker compose:

- **Justfile** with common tasks.
- **Traefik** reverse proxy configuration
- **Authentik** authentication & forward-auth integration
- **Automated Borg backups** for persistent data

## Features

- SSO integration with authentik
- Routing with traefik without exposing docker socket
- Monitoring config with gatus

## Usage

```bash
copier copy <template-repo-url> <destination>
```

Answer the prompts, then start your stack with:

```bash
docker compose up -d
```

## Roadmap

- Child templates for services I am familiar with.
- Backups using borgmatic.
