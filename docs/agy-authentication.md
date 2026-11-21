# Use a company Gemini API key with Antigravity CLI

Use a Gemini API key from a Google Cloud project your company has approved for this work. The key's project determines API usage, quota and billing. Ask your Cloud administrator which project and authentication method to use, especially for company source code or data. [Gemini API key guide](https://ai.google.dev/gemini-api/docs/api-key).

## Gemini Developer API key

1. Sign in to Google AI Studio with your work account. In **Dashboard → Projects**, import the approved Cloud project if needed. In **API Keys**, create a key for that project if your organisation allows it. If the project or key creation is unavailable, ask the project administrator for access or the company's approved alternative. [AI Studio API keys](https://aistudio.google.com/apikey).
2. In `~/.gemini/antigravity-cli/settings.json`, add `"modelProvider": "gemini"` to the existing top-level settings. Keep the other keys. A new file can contain just this.

   ```json
   {
     "modelProvider": "gemini"
   }
   ```

3. Export `GEMINI_API_KEY` from your approved secret store before starting `agy` in the target checkout. For a one-off Bash or Zsh session, the snippet below prompts for the key without echoing it and keeps the exported value inside the subshell.

   ```bash
   (
     printf 'Gemini API key: '
     IFS= read -rs GEMINI_API_KEY || exit 1
     printf '\n'
     [ -n "$GEMINI_API_KEY" ] || exit 1
     export GEMINI_API_KEY
     agy
   )
   ```

4. Check for **Gemini API key** in the CLI header. Use `/model` to choose from the models available with this credential. The interactive CLI needs the provider setting and the exported variable together. It reads `GEMINI_API_KEY` from the environment, so an unexported `.env` entry or `GOOGLE_API_KEY` does not supply the key. Keep the actual credential out of repo files and shell history. [Antigravity authentication](https://antigravity.google/docs/install?tab=cli#using-a-gemini-api-key).

## Company-managed sign-in or Google Cloud ADC

If your company provides managed Antigravity access, use the work-account sign-in your administrator sets up. For a Google Cloud deployment where your administrator directs you to use Application Default Credentials (ADC), remove the Gemini API `modelProvider` override and use your work identity and assigned project.

```bash
gcloud auth application-default login --project YOUR_COMPANY_PROJECT_ID
AGY_ADC_AUTH=true agy
```

Your administrator can confirm the enabled API, project permissions and location for ADC. To return to normal account sign-in after API-key use, remove `modelProvider` from the CLI settings and relaunch `agy`. [Antigravity Enterprise](https://antigravity.google/docs/enterprise/), [Antigravity authentication](https://antigravity.google/docs/install?tab=cli).
