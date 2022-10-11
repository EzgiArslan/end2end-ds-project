# End2End DS Project


- :white_check_mark: Training of Model
- :white_check_mark: Deployment of Model with Kubernetes
- :black_square_button: Load testing and Scaling

## :dart: Training of Model

[Credit card fraud dataset](https://www.kaggle.com/datasets/dhanushnarayananr/credit-card-fraud) iss used for this project. This dataset include 1 million data and 8 features. It is an unbalanced dataset. There is only 8% of the data is not fraud. But, Logistic Regression model got 0.99 accurate result.

When you run the fraud-detection.ipynb you get the model as model.pkl and, min-max scaler as preprocess.pkl for later using.

## :dart: Deployment of Model with Kubernetes

Let's build an image to use in Kubernetes Deployment.
```
    # build image
    docker build -t frauddetection:latest .
```

Create a Kubernetes Deployment using api_kubernetes_deployment.yaml file.

```
	kubectl apply -f ./deployment/api_kubernetes_deployment.yaml 
```