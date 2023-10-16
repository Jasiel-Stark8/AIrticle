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
- ✅ Deployment on `Zeet` | `fl{/}`
- ✅ Automated testing with `Github Actions`

## 🖼️ Screenshots

![AIrticle - AI-Powered Newsletter Generator.](#)

## ✨ Getting Started

> **System Dependencies**
- Python 3.12.0
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

## 🎉 AIrticle PRO (COMING SOON)

> For more features and priority support, consider upgrading to our PRO version.

- [AIrticle PRO](#) - Product Page (COMING SOON)
- [AIrticle PRO Demo](#) - LIVE Demo (COMING SOON)

## 👥 Contributing

We welcome contributions! See our [Contributor's Guide](#).

## 📜 License

AIrticle is licensed under the **GNU Affero General Public License v3.0 (AGPL-3.0)**. Open-source project crafted with ❤️ by [Jason Quist](https://github.com/Jasiel-Stark8/).
