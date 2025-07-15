import os
import google.generativeai as genai
from dotenv import load_dotenv

def ensure_env_key(key_name: str) -> str:
    """Check if an environment variable is set; raise helpful error if not."""
    value = os.getenv(key_name)
    if not value:
        raise EnvironmentError(
            f"❌ Environment variable '{key_name}' is missing.\n\n"
            "✅ To fix this:\n"
            f"1. Create a `.env` file in your project root (if it doesn't exist).\n"
            f"2. Add this line to it:\n\n   {key_name}=your_api_key_here\n\n"
            "🔗 Get your Gemini API key here: https://makersuite.google.com/app/apikey\n"
        )
    return value

# Load environment variables
load_dotenv()

# Ensure API key is present
API_KEY = ensure_env_key("GOOGLE_API_KEY")

# Configure the Gemini client
genai.configure(api_key=API_KEY)

def get_ai_suggestions(analysis: dict) -> str:
    try:
        prompt = (
            "You are a resume expert and career advisor.\n"
            "Based on the following resume analysis, suggest improvements:\n\n"
            f"Summary: {analysis.get('summary', 'N/A')}\n"
            f"Fit Score: {analysis.get('fit_score', 'N/A')}\n"
            f"Missing Keywords: {', '.join(analysis.get('missing_keywords', []))}\n"
            f"Weaknesses: {', '.join(analysis.get('weaknesses', []))}\n"
            f"Strengths: {', '.join(analysis.get('strengths', []))}\n"
            f"Metrics Found: {'Yes' if analysis.get('metrics_found') else 'No'}"
        )

        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)

        return response.text.strip() if hasattr(response, "text") else "⚠️ Empty response from Gemini."

    except Exception as e:
        return f"Gemini suggestion error: {str(e)}"
