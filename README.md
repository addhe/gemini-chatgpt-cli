**README.md**

**Introduction**

This Python script uses Google Gen AI Gemini to generate code and perform various tasks. It requires an API key and installation of necessary requirements.

**Prerequisites**

* Python 3.7 or later
* Google Gen AI Gemini API key
* Virtual environment
* Requirements.txt

**Installation**

1. Clone the repository:

```
$git clone https://github.com/addhe/my-google-gemini-bot.git
```

2. Create a virtual environment:

```
$python3 -m venv venv
```

3. Activate the virtual environment:

```
source venv/bin/activate
```

4. Install the requirements:

```
pip install -r requirements.txt
```

**Usage**

1. Obtain a Google Gen AI Gemini API key:

```
https://makersuite.google.com/app/apikey
```

2. Set the API key as an environment variable:

```
$export GOOGLE_GEMINI_API_KEY="YOUR_API_KEY"
```

3. Run the Program:

```
$python3 gemini-bot.py
```

3. Exit the Program:

```
>exit()
```

**Using Docker and Dockerfile**

*** Pre-Requisite ***
1. Please make sure your Docker already exists
2. Auth your account into docker registry

*** Installation via Docker ***
1. Build our docker google gemini bot
```
$docker build --tag gemini-bot:v1.0 .
```

2. Using it directly, you will need the API Key
```
$docker run -it --name {{container_name}} --env GOOGLE_GEMINI_API_KEY={{you_gemini_api_key}} gemini-bot:v1.0

```

```
e.g.
$docker run -it --name awan-chatgpt-test --env GOOGLE_GEMINI_API_KEY=ChangeMe-ToValidKey gemini-bot:v1.0
```

**Troubleshooting**

If you encounter any issues, check the following:

* Ensure that you have an active Google Gen AI Gemini API key.
* Make sure the API key is set as an environment variable.
* Check that the Python script is running in the virtual environment.
* Verify that the requirements are installed correctly.

**Contributions**

Contributions are welcome! Please read the CONTRIBUTING.md file for more information.

**License**

This project is licensed under the MIT License - see the LICENSE file for details.%
