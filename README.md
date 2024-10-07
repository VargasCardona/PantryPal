![PantryPal](https://github.com/user-attachments/assets/899d7172-9799-459a-9328-b88b9ca6f062)
# RecetApp - Microservices-based Recipe Management Application
Microservices-based application designed to help users organize their cooking recipes, plan weekly menus, generate shopping lists based on selected recipes, and suggest recipes based on available ingredients in their pantry.

## Table of Contents
- [Project Description](#project-description)
- [Microservices](#microservices)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Contributors](#contributors)
- [License](#license)

## Project Description

RecetApp is a platform that streamlines meal planning and recipe management. The application is built using a microservices architecture to ensure scalability, maintainability, and flexibility. Users can create and manage recipes, plan menus, generate shopping lists, and receive recipe suggestions based on their available ingredients.

## Microservices

1. **User Management Service**
2. **Recipe Management Service**
3. **Menu Planning Service**
4. **Shopping List Generation Service**
5. **Notification Service**
6. **Pantry Management Service**
7. **Recipe Suggestion Service**

## Features

### User Management:
- User registration and authentication (JWT or OAuth2)
- Profile management
- Role-based access control for family/group accounts

### Recipe Management:
- Create, edit, and search recipes
- Categorize recipes
- Share recipes (public/private)

### Menu Planning:
- Plan daily or weekly meals
- Create recurring menus
- Calendar view for meal plans

### Shopping List Generation:
- Automatic compilation of ingredients for weekly menus
- Ingredient categorization
- Integration with online shopping services

### Notifications:
- Shopping reminders
- Meal preparation reminders
- Pantry item expiration alerts

### Pantry Management:
- Inventory tracking of available ingredients
- Expiration date monitoring

### Recipe Suggestions:
- Suggest recipes based on available ingredients
- Filter suggestions by meal type, difficulty, preparation time, etc.

## Technologies Used

- Microservices Architecture
- RESTful APIs
- JWT or OAuth2 for authentication
- Database (to be determined: e.g., PostgreSQL, MongoDB)
- Message Queue (e.g., RabbitMQ, Apache Kafka)
- Docker for containerization
- Kubernetes for orchestration (optional)

## Getting Started

### Prerequisites
- [Docker](https://www.docker.com/get-started)

### Installation
1. Clone the repository:
 ```
git clone https://github.com/your-username/recetapp.git
 ```
2. Navigate to the project directory:
 ```
cd PantryPal
 ```
## Contributors

- **Nicolás Vargas Cardona** - [GitHub Profile](https://github.com/VargasCardona)
- **Mateo Loaiza García** - [GitHub Profile](https://github.com/Matthub05)

## License

This project is licensed under the GPL License. See the [LICENSE](LICENSE) file for details.
