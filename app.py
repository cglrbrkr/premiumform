#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def display_form():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Your Form</title>
        
        <!-- Include Montserrat font from Google Fonts -->
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600&display=swap" rel="stylesheet">
        
        <style>
            /* Apply the Montserrat font to your website */
            body {
                font-family: 'Montserrat', sans-serif;
                background-image: url('{{ url_for('static', filename='bg.jpg') }}');
                background-size: cover;
                color: white;
            }

            .box {
                border: 2px solid white;
                padding: 20px;
                width: 500px; 
                margin-bottom: 20px;
                border-radius: 15px;
                background-color: rgba(0, 0, 0, 0.6); 
            }

            .field-label {
                display: inline-block;
                width: 150px; 
                vertical-align: top;
            }

            .checkbox-label {
                display: inline-block;
                width: 450px;
                vertical-align: top;
            }

            img {
                border-radius: 50%;
            }

            #agreementLabel span {
                text-decoration: underline;
                color: white;
                cursor: pointer;
            }

            input[type="text"], input[type="email"] {
                width: 250px;  /* Increased the width of the input boxes */
            }

        </style>
    </head>
    <body>
        <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100vh;">
            
            <div class="box" style="text-align: center;">
                <img src="{{ url_for('static', filename='profile.jpg') }}" alt="Your Image" style="width: 200px;">
                <p>@kariyervekisiselgelisim</p>
                <p>Premium Paket</p>
            </div>
            
            <div class="box">
                <div style="margin-bottom: 20px;"><label class="field-label">Ad:</label> <input type="text" id="isim" name="isim"></div>
                <div style="margin-bottom: 20px;"><label class="field-label">Soyad:</label> <input type="text" id="soyisim" name="soyisim"></div>
                <div style="margin-bottom: 20px;"><label class="field-label">E-mail:</label> <input type="email" id="email" name="email"></div>
                <div style="margin-bottom: 20px;"><label class="field-label">Telefon:</label> <input type="text" id="telefon" name="telefon"></div>
                <div style="margin-bottom: 20px;"><input type="checkbox" id="agreement" name="agreement"> 
                <label class="checkbox-label" id="agreementLabel" for="agreement"><span>Kullanım koşullarını okudum, onaylıyorum.</span></label></div>
                <div style="margin-bottom: 30px;"><input type="checkbox" id="marketing" name="marketing"> <label class="checkbox-label" for="marketing">Kampayalar ve haberlerler için iletişime geçilmesini onaylıyorum.</label></div>
                <button type="Submit" onclick="submitForm()">Gönder</button>
            </div>
        </div>

        <div id="agreementPopup" style="display: none; position: fixed; left: 50%; top: 50%; transform: translate(-50%, -50%); background-color: #fff; padding: 20px; border: 1px solid #000; z-index: 1000;">
            <h2>User Agreement</h2>
            <p>Your agreement content goes here...</p>
            <button onclick="closePopup()">Close</button>
        </div>

        <script>
            document.getElementById('agreementLabel').addEventListener('click', function() {
                document.getElementById('agreementPopup').style.display = 'block';
            });

            function closePopup() {
                document.getElementById('agreementPopup').style.display = 'none';
            }

            function submitForm() {
                alert("Form submitted!");
            }
        </script>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == "__main__":
    app.run(debug=True, port=5999)




