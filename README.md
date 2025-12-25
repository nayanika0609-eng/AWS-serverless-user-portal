#AWS Serverless User Portal

This project is a fully serverless web application developed using core AWS cloud services and DevOps best practices.

Tech Stack

Amazon S3 – Static frontend hosting

Amazon API Gateway – RESTful API management

AWS Lambda – Backend business logic

Amazon DynamoDB – NoSQL database for data storage

GitHub Actions – Continuous Integration and Continuous Deployment (CI/CD)

Key Features

Users can submit their name and email through the frontend interface

Submitted data is securely stored in DynamoDB

Completely serverless architecture, eliminating server management

Automated CI/CD pipeline to deploy updates on every GitHub commit

System Architecture

S3 (Frontend) → API Gateway → Lambda Function → DynamoDB

DevOps Implementation

GitHub Actions automates build and deployment processes

Ensures fast, reliable, and consistent application updates

Author
Nayanika Prasad
