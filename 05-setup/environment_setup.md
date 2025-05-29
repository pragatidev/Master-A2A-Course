# Environment Configuration

This guide will help you set up your `.env` file to manage configuration variables securely and efficiently.

## Step-by-Step Setup

1. Copy the example file:

```bash
cp .env.sample .env
```

2. Open the `.env` file and fill in your actual configuration values:
   - Add your **OpenAI API Key**
   - Optional: Add any integration keys (Slack, Salesforce, etc.)
   - Optional: Customize timeouts, ports, and logging settings

3. Don't commit your `.env` file to Git. It's already listed in `.gitignore`.

## Recommended Practices

- Always use environment variables for secrets.
- Keep `.env.sample` up to date for collaborators or learners.
- Validate the environment using the `environment_check.py` script.
