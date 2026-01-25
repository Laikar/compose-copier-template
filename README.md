<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<summary>Table of contents</summary>

- [Docker Compose Template Generator](#docker-compose-template-generator)
  - [Features](#features)
  - [Usage](#usage)
  - [Roadmap](#roadmap)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Docker Compose Template Generator

A **Copier template** for bootstrapping docker(or podman)compose projects with my prefered integrations into other self hosted services.

## Features

- **Justfile** with common tasks.
- **gitignore** and **pre-commit** config.
- Reverse proxy with **Traefik**
- Single Sign On with **Authentik**
- Uptime monitoring with **Gatus**

## Usage

```bash
copier copy https://github.com/Laikar/compose-copier-template <destination>
```

Answer the prompts, then start your stack with:

```bash
docker compose up -d
```

## Roadmap

- Child templates for services I am familiar with.
- Backups using borgmatic.
