# CI/CD Pipeline (Personne 3 – ready to use)

## 1. Create Docker Hub repo
- Log in hub.docker.com → Repositories → Create Repository → `myapp` (must match IMAGE_NAME in workflow)

## 2. Add GitHub secrets
Settings → Secrets → Actions → New repository secret  
- `DOCKER_USERNAME`   your Docker Hub username  
- `DOCKER_PASSWORD`   Docker Hub Access Token (Hub → Account Settings → Security → New Access Token)  
- `KUBE_CONFIG`       base64 of your cluster kubeconfig:  
  `base64 -w 0 ~/.kube/config`  (copy whole output)

## 3. Drop your code in root
- `Dockerfile` (must be multi-stage)  
- `requirements.txt` or `package.json`  
- `Makefile` (optional) with `lint` and `test` targets  
- If no Makefile, place `pytest` tests → pipeline will auto-run them

## 4. Push
```bash
git add .
git commit -m "add app code"
git push origin main