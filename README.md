# Smart Task Scheduler

## Overview

Smart Task Scheduler is a task management application designed to help users efficiently schedule and track their tasks. It utilizes modern web technologies including React (Vite), Tailwind CSS, Supabase (for backend services), and TypeScript.

## Features

- User authentication (via Supabase)
- Task creation, editing, and deletion
- Task categorization and prioritization
- Responsive UI with Tailwind CSS
- Real-time updates

## Tech Stack

- **Frontend:** React (Vite), TypeScript, Tailwind CSS
- **Backend:** Supabase (PostgreSQL, Authentication)
- **Build Tool:** Vite
- **Configuration:** ESLint, PostCSS, TypeScript

## Folder Structure

```
Smart Task Scheduler/
├── .env                   # Environment variables
├── .gitignore             # Git ignore file
├── eslint.config.js       # ESLint configuration
├── index.html             # Main HTML file
├── package.json           # Project metadata and dependencies
├── package-lock.json      # Lock file for npm
├── postcss.config.js      # PostCSS configuration
├── tailwind.config.js     # Tailwind CSS configuration
├── tsconfig.app.json      # TypeScript configuration for app
├── tsconfig.json          # TypeScript global configuration
├── tsconfig.node.json     # TypeScript configuration for Node
├── vite.config.ts         # Vite configuration
├── .prompt/               # Prompt-related data (if any)
├── dist/                  # Build output directory
├── src/                   # Main source code
├── supabase/              # Supabase configurations
```

## Setup Instructions

### Prerequisites

- Node.js (LTS version recommended)
- npm or yarn
- Supabase account and API keys

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/smart-task-scheduler.git
   ```

2. Navigate to the project directory:

   ```sh
   cd smart-task-scheduler
   ```

3. Install dependencies:

   ```sh
   npm install
   ```

4. Set up the environment variables:

   - Create a `.env` file in the root directory and add the required Supabase keys and configurations.

5. Run the development server:

   ```sh
   npm run dev
   ```

6. Open `http://localhost:5173/` in your browser.

## Deployment

To deploy the project, use:

```sh
npm run build
```

This will generate production-ready files inside the `dist/` folder.

## Contribution

Feel free to fork the repository, create a branch, and submit a pull request with your improvements.



📸 Screenshots

**Homepage**
![Homepage](https://github.com/Spacey6849/smart-todo-task-scheduler/blob/85ba7f58525736c402558ab847542687af2f57ed/Images/homepage.jpg)

**Task Creation**

![TaskCreation](https://github.com/Spacey6849/smart-todo-task-scheduler/blob/dc710bc532b1ebb792a045ddfa8f1f4d6f711496/Images/CreateTask.jpg)

**User Authentication**
![UserAuthentication](https://github.com/Spacey6849/smart-todo-task-scheduler/blob/dc710bc532b1ebb792a045ddfa8f1f4d6f711496/Images/signIn1.jpg)
__________________________________________________________________________________________________________________________________________________
![UserAuthentication](https://github.com/Spacey6849/smart-todo-task-scheduler/blob/dc710bc532b1ebb792a045ddfa8f1f4d6f711496/Images/signup1.jpg)
