from groq import Groq

def tanya_ai(teks_data):
    # Kita letak kunci API terus di sini untuk pastikan ia wujud
    api_key_anda = "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" 
    
    try:
        # Kita cipta client tepat sebelum digunakan
        client = Groq(api_key=api_key_anda)
        
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user", 
                    "content": f"Berikan analisis ringkas trend harga untuk data ini dalam 3 ayat: {teks_data}"
                }
            ],
            model="llama-3.1-8b-instant",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Ralat Teknikal AI: {str(e)}"