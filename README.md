
# Academic API DevOps

Projeto desenvolvido para demonstrar conhecimentos em desenvolvimento backend com Python, conteinerização com Docker, testes automatizados e implantação contínua utilizando GitLab CI/CD e Kubernetes.

## Visão Geral

A aplicação disponibiliza endpoints para verificação de disponibilidade da API e cálculo de média acadêmica.

## Tecnologias

- Python
- FastAPI
- PyTest
- Docker
- GitLab CI/CD
- Kubernetes

## Endpoints

### GET /health
Retorna o status da aplicação.

### POST /media
Calcula a média de três notas e informa a situação do aluno.

## Executando Localmente

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Docker

```bash
docker build -t academic-api .
docker run -p 8000:8000 academic-api
```

## Pipeline CI/CD

1. Execução de testes automatizados.
2. Construção da imagem Docker.
3. Preparação para publicação e deploy.

## Kubernetes

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

## Estrutura

```text
academic-api-devops
├── app
├── tests
├── Dockerfile
├── .gitlab-ci.yml
├── deployment.yaml
├── service.yaml
└── README.md
```

## Autor

Filipe Oliveira Cardoso
GitHub: https://github.com/Filipcardos
LinkedIn: https://www.linkedin.com/in/filipcardos
