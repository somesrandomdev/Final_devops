# Mon appli – Personne 2

A simple FastAPI web application demonstrating a modern Python microservice with Docker containerization, Kubernetes deployment, and CI/CD pipeline integration.

## 🚀 Features

- **FastAPI Framework**: High-performance async web framework for Python
- **Health Check Endpoint**: `/health` for monitoring and load balancer checks
- **Version Information**: Returns application version and Git commit hash
- **Docker Support**: Multi-stage Dockerfile for optimized container builds
- **Kubernetes Ready**: Complete K8s deployment configuration
- **CI/CD Pipeline**: Automated testing and deployment with GitHub Actions
- **Test Suite**: Comprehensive test coverage with pytest

## 📋 Prerequisites

- Python 3.12+
- Docker (for containerization)
- Kubernetes cluster (for deployment)
- Git

## 🛠️ Installation

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd final_devops
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

5. **Access the application**
   - Main endpoint: http://localhost:8000/
   - Health check: http://localhost:8000/health
   - API docs: http://localhost:8000/docs

### Docker Deployment

1. **Build the image**
   ```bash
   docker build -t myapp:latest .
   ```

2. **Run the container**
   ```bash
   docker run -p 8000:8000 -e GIT_HASH=$(git rev-parse --short HEAD) myapp:latest
   ```

3. **Access the application**
   - Visit http://localhost:8000 in your browser

## 📡 API Endpoints

### GET /
Returns application information including message, version, and Git commit hash.

**Response:**
```json
{
  "message": "Hello le prof, tout marche !",
  "version": "1.0.0",
  "commit": "abc1234"
}
```

### GET /health
Health check endpoint for monitoring and load balancer configuration.

**Response:**
```json
{
  "status": "OK"
}
```

## 🧪 Testing

Run the test suite:

```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov=app

# Run specific test file
pytest tests/test_main.py
```

### Test Coverage

The application includes tests for:
- Root endpoint functionality
- Health check endpoint
- Response status codes
- JSON response structure

## 🐳 Docker Configuration

The application uses a multi-stage Dockerfile for optimized builds:

- **Builder stage**: Installs Python dependencies
- **Runtime stage**: Creates minimal final image
- **Environment variables**: Supports GIT_HASH for version tracking
- **Port exposure**: Exposes port 8000

### Docker Commands

```bash
# Build image
docker build -t myapp:latest .

# Run container
docker run -p 8000:8000 myapp:latest

# Run with environment variables
docker run -p 8000:8000 -e GIT_HASH=abc1234 myapp:latest

# View logs
docker logs <container_id>

# Interactive shell
docker run -it myapp:latest /bin/bash
```

## ☸️ Kubernetes Deployment

### Prerequisites

- Kubernetes cluster access
- kubectl configured
- Docker image pushed to registry

### Deployment Steps

1. **Apply namespace**
   ```bash
   kubectl apply -f k8s/namespace.yaml
   ```

2. **Deploy application**
   ```bash
   kubectl apply -f k8s/deployment.yaml
   kubectl apply -f k8s/service.yaml
   ```

3. **Check deployment status**
   ```bash
   kubectl get pods -n demo
   kubectl get service -n demo
   ```

4. **Port forward for testing**
   ```bash
   kubectl port-forward svc/myapp 8000:80 -n demo
   ```

### Kubernetes Features

- **3 Replicas**: High availability with rolling updates
- **Health Probes**: Liveness and readiness checks
- **Rolling Updates**: Zero-downtime deployments
- **ClusterIP Service**: Internal service discovery

## 🔄 CI/CD Pipeline

The application includes a complete GitHub Actions workflow for automated deployment.

### Required GitHub Secrets

Configure the following secrets in your GitHub repository:

- `DOCKER_USERNAME`: Your Docker Hub username
- `DOCKER_PASSWORD`: Docker Hub Access Token
- `KUBE_CONFIG`: Base64-encoded kubeconfig file

### Pipeline Features

- **Automated Testing**: Runs pytest on every push
- **Docker Build**: Multi-stage Docker image building
- **Container Registry**: Pushes to Docker Hub
- **Kubernetes Deployment**: Automated K8s deployment
- **Rollback Support**: Includes rollback.sh script

### Manual Deployment

For manual deployments, use the provided rollback script:

```bash
./rollback.sh
```

## 📁 Project Structure

```
final_devops/
├── app/
│   ├── __init__.py
│   └── main.py              # FastAPI application
├── k8s/
│   ├── deployment.yaml      # Kubernetes deployment
│   ├── namespace.yaml       # K8s namespace
│   └── service.yaml         # K8s service
├── tests/
│   └── test_main.py         # Test suite
├── .github/
│   └── workflows/           # CI/CD pipeline
├── .dockerignore
├── .flake8
├── Dockerfile
├── kubeconfig
├── kubeconfig_raw
├── README.md
├── requirements.txt
└── rollback.sh
```

## 🔧 Configuration

### Environment Variables

- `GIT_HASH`: Git commit hash for version tracking (default: "unknown")

### Application Settings

- **Host**: 0.0.0.0 (all interfaces)
- **Port**: 8000
- **Title**: "Mon appli – Personne 2"
- **Version**: 1.0.0

## 🚀 Deployment to Production

### Docker Hub Setup

1. Create Docker Hub repository named `myapp`
2. Configure GitHub secrets as described above
3. Push code to trigger automatic deployment

### Kubernetes Production Considerations

- **Resource Limits**: Add CPU/memory limits to deployment
- **Ingress**: Configure ingress controller for external access
- **Secrets Management**: Use Kubernetes secrets for sensitive data
- **Monitoring**: Integrate with Prometheus/Grafana
- **Logging**: Configure centralized logging (ELK stack)

## 🐛 Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   # Find process using port 8000
   lsof -i :8000
   # Kill process
   kill -9 <PID>
   ```

2. **Docker build fails**
   ```bash
   # Check Dockerfile syntax
   docker build --no-cache -t myapp:latest .
   ```

3. **Kubernetes deployment fails**
   ```bash
   # Check pod logs
   kubectl logs -f <pod-name> -n demo
   # Check events
   kubectl get events -n demo
   ```

4. **Tests failing**
   ```bash
   # Run tests with verbose output
   pytest -v tests/test_main.py
   ```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add type hints where appropriate
- Write comprehensive tests
- Update documentation as needed

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Check the troubleshooting section above
- Review the FastAPI documentation: https://fastapi.tiangolo.com/
- Check Kubernetes documentation: https://kubernetes.io/docs/

## 🔄 Changelog

### Version 1.0.0
- Initial release
- FastAPI web application
- Docker containerization
- Kubernetes deployment configuration
- CI/CD pipeline setup
- Test suite implementation

---

**Note**: This is a demonstration application for educational purposes, showcasing modern Python web development practices with containerization and orchestration.