docker build -t morakotdocker/eks-s3-irsa-access:latest
docker buildx build --platform linux/amd64 -t morakotdocker/eks-s3-irsa-access:latest .
