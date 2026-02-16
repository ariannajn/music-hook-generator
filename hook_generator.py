import openai

# Replace with your API key
openai.api_key = "YOUR_API_KEY"

persona = "Bedroom music producer"

prompt = f"""
Generate 20 short paid ad hooks for a consumer AI music app targeting {persona}.
Group them into categories:
- Hype
- Emotional
- Technical
- Creator-focused
Keep each hook under 12 words.
"""

response = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)

print(response.choices[0].message.content)
