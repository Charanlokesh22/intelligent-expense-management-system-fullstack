Intelligent Expense Management System

A production-grade full-stack application designed to manage expenses, analyze spending patterns, and provide AI-driven budget recommendations. Built using Angular for the frontend, Spring Boot for backend REST APIs, and a Python-based microservice using FastAPI to deliver intelligent financial insights.

How It Works

This system helps users track expenses by category, date, and amount. The backend stores and manages transactions securely, while the AI microservice processes past expense data to suggest monthly budget limits. The frontend visualizes this information through interactive charts and dashboards, offering users real-time insights into their financial behavior.

The application follows a modular microservices architecture:
- The frontend (Angular) interacts with the backend (Spring Boot) over REST APIs.
- The backend handles authentication, expense logging, and API routing.
- The AI service processes historical data and returns budget suggestions using a lightweight ML model.
- All services are containerized using Docker and orchestrated via Docker Compose.

Features

- Add, update, and delete expense records with category and date.
- JWT-secured user authentication and session management.
- AI-powered budget suggestions based on historical data patterns.
- Dashboard with monthly and category-wise spending visualizations.
- REST APIs built using Spring Boot and integrated with Python microservice.
- Dockerized deployment with all services running in isolated containers.


Installation Steps

1. Clone the repository:
   git clone https://github.com/Charanlokesh22/intelligent-expense-management.git
   cd intelligent-expense-management

2. Start the application using Docker:
   docker-compose up --build

3. Access the app:
   - Frontend:       http://localhost:4200
   - Backend API:    http://localhost:8080/api
   - AI Service:     http://localhost:5000/predict

Usage

- Register or log in from the frontend interface.
- Navigate to the dashboard to enter or update expenses.
- View monthly statistics and download expense logs.
- Receive smart budget recommendations for upcoming months.

Security


- JWT-based secure authentication for all backend routes.
- Separate user sessions and access control.
- Secure inter-service communication across containers.

AI Microservice

The AI service reads transaction patterns and returns a recommended monthly budget threshold. The logic is based on simple statistical trends and can be enhanced with more advanced models.

