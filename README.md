# AWS Serverless User Portal

A fully serverless web application built using AWS cloud services and modern DevOps practices.

## 🚀 Overview
This project demonstrates how to design, deploy, and manage a scalable serverless web application on AWS. The application allows users to submit their name and email through a frontend interface, which is then processed and securely stored using backend cloud services.

## 🛠️ Tech Stack
- **Amazon S3** – Hosts the static frontend  
- **Amazon API Gateway** – Exposes RESTful APIs  
- **AWS Lambda** – Handles backend logic  
- **Amazon DynamoDB** – Stores user data  
- **GitHub Actions** – Enables CI/CD automation  

## ✨ Features
- Simple user form for submitting name and email  
- Secure storage of user data in DynamoDB  
- Fully serverless architecture with no server management  
- Automated deployment using CI/CD pipeline  
- Scalable and cost-effective cloud solution  

## 🏗️ Architecture
Frontend (Amazon S3)
↓
API Gateway
↓
AWS Lambda
↓
Amazon DynamoDB

## 🔁 CI/CD & DevOps
- GitHub Actions is used to automate build and deployment  
- Every commit triggers an automatic deployment  
- Ensures faster development cycles and consistent updates  

## 📌 Deployment
- Frontend is deployed on Amazon S3  
- Backend services are integrated using API Gateway and Lambda  
- Infrastructure follows serverless best practices  

## 👤 Author
**Nayanika Prasad**
