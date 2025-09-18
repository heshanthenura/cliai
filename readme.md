# CLI-AI 🤖💻

**CLI-AI** is a command-line assistant powered by [OpenRouter](https://openrouter.ai/).  
It helps you generate **safe Linux commands** with explanations, and lets you **choose to run them interactively** from the terminal.

I originally built this just for fun, but it turned out to be much better and more useful than I expected.

## 📂 Project Structure

```text
CLIAI/
├── src/
│   ├── app.py               # Entry point
│   ├── utils/
│   │   ├── openRouterClient.py  # Handles OpenRouter API calls
│   │   ├── processCommand.py    # Parses JSON and displays steps
│   │   ├── runCommand.py        # Executes Linux commands with consent
│   │   ├── bcolors.py           # CLI color helper
│   │   └── userCLI.py           # CLI loop & interaction
└── README.md
```

## 🔑 API Key Setup

You need an **API key from [OpenRouter](https://openrouter.ai/)**.

- Sign up for free and grab your API key.
- Set it as an **environment variable** so the app can use it:

### Linux / macOS

```bash
export OPENROUTER_API_KEY="your_api_key_here"
```

(You can add this line to your `~/.bashrc` or `~/.zshrc` to make it permanent.)

### Windows (PowerShell)

```powershell
setx OPENROUTER_API_KEY "your_api_key_here"
```

After setting it, restart your terminal.

> ✅ The app will automatically read the key from the `OPENROUTER_API_KEY` environment variable.
> Currently, the project is configured to run on the free model:
> `deepseek/deepseek-chat-v3.1:free`

## 🚀 How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/CLIAI.git
   cd CLIAI
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:

   ```bash
   python src/app.py
   ```

## ⚠️ Disclaimer

This project is **not production ready**.
Always review commands before running them. The authors are **not responsible** for any damage caused by running generated commands.
