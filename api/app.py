import openai
from flask import Flask, request, jsonify

app = Flask(__name__)

# Masukkan API key OpenAI Anda di sini
openai.api_key = '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'

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    
    # Menggunakan API OpenAI untuk memproses pesan dari pengguna
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Atau bisa menggunakan model lain, seperti 'gpt-3.5-turbo'
            prompt=user_message,
            max_tokens=150,
            temperature=0.7
        )

        # Mendapatkan hasil dari respons model
        chatbot_response = response.choices[0].text.strip()

        return jsonify({"response": chatbot_response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
