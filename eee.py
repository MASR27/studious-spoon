{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "db014425-d3b7-44ed-a7a3-9c430d8b5c0a",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "created virtual environment CPython3.10.4.final.0-64 in 258ms\n",
      "  creator CPython3Posix(dest=/workspaces/codespaces-jupyter/venv, clear=False, no_vcs_ignore=False, global=False)\n",
      "  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/codespace/.local/share/virtualenv)\n",
      "    added seed packages: pip==23.0.1, setuptools==67.4.0, wheel==0.38.4\n",
      "  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator\n"
     ]
    }
   ],
   "source": [
    "!virtualenv venv\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "60196b16-8129-4477-967c-1dd3aae5814e",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "!source venv/bin/activate\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "22eba130-b798-4f68-a0bd-5ec1b9db3d1c",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting flask\n",
      "  Downloading Flask-2.2.3-py3-none-any.whl (101 kB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m101.8/101.8 kB\u001b[0m \u001b[31m4.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hCollecting mkdocs\n",
      "  Downloading mkdocs-1.4.2-py3-none-any.whl (3.7 MB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m3.7/3.7 MB\u001b[0m \u001b[31m49.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m00:01\u001b[0m00:01\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: plotly in /home/codespace/.local/lib/python3.10/site-packages (5.13.1)\n",
      "Collecting markdown\n",
      "  Downloading Markdown-3.4.1-py3-none-any.whl (93 kB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m93.3/93.3 kB\u001b[0m \u001b[31m6.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hCollecting itsdangerous>=2.0\n",
      "  Downloading itsdangerous-2.1.2-py3-none-any.whl (15 kB)\n",
      "Requirement already satisfied: Jinja2>=3.0 in /home/codespace/.local/lib/python3.10/site-packages (from flask) (3.1.2)\n",
      "Collecting click>=8.0\n",
      "  Downloading click-8.1.3-py3-none-any.whl (96 kB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m96.6/96.6 kB\u001b[0m \u001b[31m7.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hCollecting Werkzeug>=2.2.2\n",
      "  Downloading Werkzeug-2.2.3-py3-none-any.whl (233 kB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m233.6/233.6 kB\u001b[0m \u001b[31m15.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: packaging>=20.5 in /home/codespace/.local/lib/python3.10/site-packages (from mkdocs) (23.0)\n",
      "Collecting pyyaml-env-tag>=0.1\n",
      "  Downloading pyyaml_env_tag-0.1-py3-none-any.whl (3.9 kB)\n",
      "Collecting mergedeep>=1.3.4\n",
      "  Downloading mergedeep-1.3.4-py3-none-any.whl (6.4 kB)\n",
      "Collecting ghp-import>=1.0\n",
      "  Downloading ghp_import-2.1.0-py3-none-any.whl (11 kB)\n",
      "Collecting markdown\n",
      "  Downloading Markdown-3.3.7-py3-none-any.whl (97 kB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m97.8/97.8 kB\u001b[0m \u001b[31m7.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: pyyaml>=5.1 in /home/codespace/.local/lib/python3.10/site-packages (from mkdocs) (6.0)\n",
      "Collecting watchdog>=2.0\n",
      "  Downloading watchdog-2.3.1-py3-none-manylinux2014_x86_64.whl (80 kB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m80.6/80.6 kB\u001b[0m \u001b[31m5.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: tenacity>=6.2.0 in /home/codespace/.local/lib/python3.10/site-packages (from plotly) (8.2.2)\n",
      "Requirement already satisfied: python-dateutil>=2.8.1 in /home/codespace/.local/lib/python3.10/site-packages (from ghp-import>=1.0->mkdocs) (2.8.2)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in /home/codespace/.local/lib/python3.10/site-packages (from Jinja2>=3.0->flask) (2.1.2)\n",
      "Requirement already satisfied: six>=1.5 in /home/codespace/.local/lib/python3.10/site-packages (from python-dateutil>=2.8.1->ghp-import>=1.0->mkdocs) (1.16.0)\n",
      "Installing collected packages: Werkzeug, watchdog, pyyaml-env-tag, mergedeep, markdown, itsdangerous, click, ghp-import, flask, mkdocs\n",
      "Successfully installed Werkzeug-2.2.3 click-8.1.3 flask-2.2.3 ghp-import-2.1.0 itsdangerous-2.1.2 markdown-3.3.7 mergedeep-1.3.4 mkdocs-1.4.2 pyyaml-env-tag-0.1 watchdog-2.3.1\n"
     ]
    }
   ],
   "source": [
    "!pip install flask mkdocs plotly markdown"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "70c8fd4f-6201-4a50-b205-6092f7f47f8d",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/')\n",
    "def index():\n",
    "    return 'Welcome to the ISO 10012:2003 Measurement Management System app!'\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "351de350-20e7-4278-bfa9-2a785c85f48e",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "!flask run"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bd56e0e9-9a9a-42f0-94f4-66196535e027",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "!mkdocs new docs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e4f27dd2-91ad-40c8-82c9-62d86dff6a64",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "from flask import Flask, render_template\n",
    "import plotly.offline as pyo\n",
    "import plotly.graph_objs as go\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/')\n",
    "def index():\n",
    "    data = [go.Bar(x=['A', 'B', 'C'], y=[1, 2, 3])]\n",
    "    fig = pyo.plot(data, output_type='div')\n",
    "    return render_template('index.html', plot=fig)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "081535d4-1133-45d7-887d-41102ffc1864",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/')\n",
    "def index():\n",
    "    return render_template('index.html')\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
