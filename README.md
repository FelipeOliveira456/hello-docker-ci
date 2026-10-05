# hello-docker-ci

Exercicio: Docker, GitHub Actions e Container Registry.

- `GET /hello` — versao `1.0` responde `Hello World`; versao `2.0` responde `Hello World 2`
- Imagem: `ghcr.io/felipeoliveira456/hello-app:1.0` e `:2.0`
- Pipeline: `.github/workflows/docker.yml` (dispara no push da `main`)

```bash
docker pull ghcr.io/felipeoliveira456/hello-app:1.0
docker run --rm -p 8080:8080 ghcr.io/felipeoliveira456/hello-app:1.0
curl http://localhost:8080/hello
```

Evidencias: `EVIDENCIAS.md`.
