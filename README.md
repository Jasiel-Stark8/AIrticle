# 🚀 AIrticle: "Where Code Meets Content"

AIrticle is an innovative web application designed to harness the capabilities of GPT-4 for generating high-quality newsletters based on user-defined topics or prompts. Crafted for those who value precision and efficiency, AIrticle is ready to revolutionize the way you create articles & newsletters.

- 👉 **AIrticle** - AI-Powered Newsletter Generator
- 👉 **Demo**: (Coming Soon)
- 👉 **Support**: 
    - 📧 [Email](mailto:nftsingularity8@gmail.com)
    - 📱 [Telegram](https://t.me/Json_format)
    - 🐞 [Report Bugs](#) *(Link to your project's issues tab)*
    - 📖 [FAQs](#) *(Link to FAQs)*

> 🚀 Built with cutting-edge technologies, Timestamp: `2023-10-10`

- ✅ `Up-to-date dependencies`
- ✅ `Database`: `PostgreSQL`
- ✅ Deployment on `Zeet` | `Docker`
- ✅ Automated testing with `Github Actions`

## 🖼️ Screenshots

![AIrticle - AI-Powered Newsletter Generator.](#)

## ✨ Getting Started

> **System Dependencies**
- Python 3.11.5
- PostgreSQL 16.0

> **Step 1** - Clone the repository

```bash
$ git clone https://github.com/Jasiel-Stark8/AIrticle.git
$ cd AIrticle
```

> **Step 2** - Set up the environment and start the app

```bash
# For Unix/MacOS
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
$ flask run --debug
```

> **Environment Variables**
- `OPENAI_API_KEY`: Your OpenAI API key.
- `DATABASE_URL`: Your PostgreSQL Database URL.

Visit `http://localhost:5000` in your browser. The app should be up & running.

## ✨ Features

- **AI-Powered Content Generation**: Utilizes GPT-4 to produce newsletters tailored to user input.
- **Intuitive User Interface**: Designed for ease of use, ensuring a seamless user experience.
- **Export Options**: Allows users to export their articles in various formats (DOC, DOCX, PDF, TXT).

### 🚀 Provisions

A commercialized version of this app will be available, allowing users without an OpenAI API key to generate content.

## ✨ Code-base Structure

```bash
📂 AIrticle/
│
├── 📂 templates/
│   ├── 📄 landing.html            # Landing page of the application
│   ├── 📄 login.html             # User login form
│   ├── 📄 register.html          # New user registration form
│   └── 📄 dashboard.html         # Main dashboard for users to manage their articles
│
├── 📂 static/
│   ├── 📂 css/
│   │   └── 📄 style.css           # Global styles for the application
│   ├── 📂 js/
│   │   ├── 📄 scripts.js          # General scripts used across different pages
│   │   └── 📄 dashboard.js        # Scripts specific to dashboard functionalities
│   └── 📂 images/                # Holds image assets used in the application
│
├── 📂 models/
│   ├── 📄 user.py                # Defines User model and related functions
│   ├── 📄 article.py             # Defines Article model and related functions
│   └── 📄 autosave.py            # Defines Autosave model and related functionality
│
├── 📂 api/
│   ├── 📂 v1/
│   │   ├── 📄 auth.py                # Handles authentication routes (login, register)
│   │   └── 📄 articles.py            # Routes related to dashboard functionalities and articles
│   │   └── 📄 autosave.py            # Routes related to autosave functionalities
│
├── 📄 app.py                    # Main application initialization and configuration
├── 📄 config.py                 # Configuration settings for the application
├── 📄 requirements.txt          # Required Python packages for the project
├── 📄 README.md                 # Project documentation and setup guide
├── 📄 .env                      # Environment variables (keep private!)
└── 📄 .gitignore                # List of files/folders to ignore in version control
```

## API Endopints

### Auth & User
1. `/signup` - `['GET', 'POST']`
2. `/login` - `['GET', 'POST']`
3. `/logout` - `['POST']` (usually, logging out is a POST operation)
4. `/update_username` - `['PUT']`
5. `/update_password` - `['PUT']`
6. `/username` - `['GET']`
7. `/user_info` - `['GET']` (To provide additional user info if needed)

### Content Generation
8. `/generate` - `['POST']`

### Article Management
9. `/view_articles` - `['GET']`
10. `/edit_article/<article_id>` - `['GET', 'PUT']` (use article_id as a parameter)
11. `/new_article` - `['POST']` (To save a new article, similar to save but initializes a new article)
12. `/save_article` - `['POST', 'PUT']` (Could also allow PUT for updates)
13. `/delete_article/<article_id>` - `['DELETE']` (To delete an article)
  
### Article Export
14. `/export/<article_id>` - `['POST']` (use article_id as a parameter)

### AutoSave
15. `/auto_save` - `['POST']`

### Extra Features
16. `/search_articles` - `['GET']` (To allow users to search their saved articles)
17. `/forgot_password` - `['POST', 'PUT']` (In case user forgets the password)
18. `/activate_account` - `['GET']` (If you want to include email-based account activation)


## 🛠️ Technologies

- **Languages**: 
  - Python (Primary backend language)
  - JavaScript (Frontend scripting)
  - HTML (Webpage structure)
  - CSS (Styling)
  
- **Frameworks**: 
  - Flask (Backend server handling)
  - Bootstrap (Responsive frontend styling)
  
- **API**: 
  - OpenAI GPT-4 (Content generation)
  
- **Database**: 
  - PostgreSQL (Reliable storage solution)
  
- **Deployment**: 
  - Docker (Containerization solution for reproducible builds)
  - Vercel (For front-end deployment and serverless functions)
  
- **Version Control**: 
  - Git (Codebase version tracking)
  - GitHub (Code repository and collaboration)

---

---
## 📖 User Guide

### **1. Sign Up/Log In**:
- **Description**: Our platform offers simple email and password-based authentication. New users can quickly create an account, and returning users can seamlessly log in.
- **Steps**:
  - **Sign Up**: Navigate to the sign-up page. Enter your email and create a password. Submit the form to register.
  - **Log In**: Navigate to the log-in page. Enter your registered email and password. Submit the form to access the dashboard.

### **2. Dashboard**:
- **Description**: The user dashboard is a centralized area where users can access saved articles and initiate new content generation requests.
- **Steps**: 
  - Once logged in, the dashboard is the primary view. Here, you can see a list of your saved articles.
  - Click on an article title to view, edit, or export the article.
  - Use the "Generate New Content" button to start the content generation process.

### **3. Content Generation**:
- **Description**: Input topics or keywords to receive AI-generated content. You have the option to edit the content directly on the platform.
- **Steps**: 
  - From the dashboard, click on "Generate New Content."
  - Input your topic or keywords in the provided field.
  - Click "Generate" to receive AI-produced content.
  - You can now edit the content as you see fit, with changes being automatically saved.

### **4. Export**:
- **Description**: After finalizing the content, users have the option to save their articles in multiple formats including DOC, DOCX, PDF, and TXT.
- **Steps**: 
  - Navigate to the article you wish to export.
  - Choose the desired format from the "Export As" dropdown.
  - Click the "Export" button. Your article will be downloaded in the selected format.

---

## 🎉 AIrticle PRO (COMING SOON)

> For more features and priority support, consider upgrading to our PRO version.

- [AIrticle PRO](#) - Product Page (COMING SOON)
- [AIrticle PRO Demo](#) - LIVE Demo (COMING SOON)

## 👥 Contributing

We welcome contributions! See our [Contributor's Guide](#).

## 📜 License

AIrticle is licensed under the **GNU Affero General Public License v3.0 (AGPL-3.0)**. Open-source project crafted with ❤️ by [Jason Quist](https://github.com/Jasiel-Stark8/).
