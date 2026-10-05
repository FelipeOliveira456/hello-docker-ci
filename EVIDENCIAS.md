# Evidencias

## Build e teste local (antes da pipeline)

```
docker build -t hello-app:1.0 .
hello-app:1.0 78.9MB
curl local 1.0: Hello World
```

## Pipeline e registry — versao 1.0

- Repo: https://github.com/FelipeOliveira456/hello-docker-ci
- Imagem: ghcr.io/felipeoliveira456/hello-app:1.0
- Pacote: https://github.com/users/FelipeOliveira456/packages/container/hello-app

```
curl pull 1.0: Hello World
```

## Versao 2.0

```
curl pull 2.0: Hello World 2
```

Tags no registry: ghcr.io/felipeoliveira456/hello-app:1.0 e ghcr.io/felipeoliveira456/hello-app:2.0
