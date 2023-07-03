import openai

def send_prompt(prompt):
    openai.api_key = "?????"
    response = openai.Completion.create(
        engine="text-davinci-003",  # 使用するエンジンを指定します
        prompt=prompt,
        max_tokens=50  # 応答の最大トークン数
    )
    return response.choices[0].text.strip()
