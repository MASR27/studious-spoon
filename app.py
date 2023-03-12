{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fee3fd3c-4b7c-45eb-8da2-b85227529a27",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      " * Restarting with watchdog (inotify)\n",
      "Traceback (most recent call last):\n",
      "  File \"/home/codespace/.local/lib/python3.10/site-packages/ipykernel_launcher.py\", line 17, in <module>\n",
      "    app.launch_new_instance()\n",
      "  File \"/home/codespace/.local/lib/python3.10/site-packages/traitlets/config/application.py\", line 1042, in launch_instance\n",
      "    app.initialize(argv)\n",
      "  File \"/home/codespace/.local/lib/python3.10/site-packages/traitlets/config/application.py\", line 113, in inner\n",
      "    return method(app, *args, **kwargs)\n",
      "  File \"/home/codespace/.local/lib/python3.10/site-packages/ipykernel/kernelapp.py\", line 678, in initialize\n",
      "    self.init_sockets()\n",
      "  File \"/home/codespace/.local/lib/python3.10/site-packages/ipykernel/kernelapp.py\", line 317, in init_sockets\n",
      "    self.shell_port = self._bind_socket(self.shell_socket, self.shell_port)\n",
      "  File \"/home/codespace/.local/lib/python3.10/site-packages/ipykernel/kernelapp.py\", line 252, in _bind_socket\n",
      "    return self._try_bind_socket(s, port)\n",
      "  File \"/home/codespace/.local/lib/python3.10/site-packages/ipykernel/kernelapp.py\", line 228, in _try_bind_socket\n",
      "    s.bind(\"tcp://%s:%i\" % (self.ip, port))\n",
      "  File \"/home/codespace/.local/lib/python3.10/site-packages/zmq/sugar/socket.py\", line 300, in bind\n",
      "    super().bind(addr)\n",
      "  File \"zmq/backend/cython/socket.pyx\", line 564, in zmq.backend.cython.socket.Socket.bind\n",
      "  File \"zmq/backend/cython/checkrc.pxd\", line 28, in zmq.backend.cython.checkrc._check_rc\n",
      "zmq.error.ZMQError: Address already in use\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[0;31mSystemExit\u001b[0m\u001b[0;31m:\u001b[0m 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/home/codespace/.local/lib/python3.10/site-packages/IPython/core/interactiveshell.py:3468: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
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
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f67ab117-c495-4483-86cc-2541bba10bd4",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Traceback (most recent call last):\n",
      "  File \"/home/codespace/.python/current/bin/flask\", line 8, in <module>\n",
      "    sys.exit(main())\n",
      "  File \"/usr/local/python/3.10.4/lib/python3.10/site-packages/flask/cli.py\", line 1050, in main\n",
      "    cli.main()\n",
      "  File \"/usr/local/python/3.10.4/lib/python3.10/site-packages/click/core.py\", line 1055, in main\n",
      "    rv = self.invoke(ctx)\n",
      "  File \"/usr/local/python/3.10.4/lib/python3.10/site-packages/click/core.py\", line 1657, in invoke\n",
      "    return _process_result(sub_ctx.command.invoke(sub_ctx))\n",
      "  File \"/usr/local/python/3.10.4/lib/python3.10/site-packages/click/core.py\", line 1404, in invoke\n",
      "    return ctx.invoke(self.callback, **ctx.params)\n",
      "  File \"/usr/local/python/3.10.4/lib/python3.10/site-packages/click/core.py\", line 760, in invoke\n",
      "    return __callback(*args, **kwargs)\n",
      "  File \"/usr/local/python/3.10.4/lib/python3.10/site-packages/click/decorators.py\", line 84, in new_func\n",
      "    return ctx.invoke(f, obj, *args, **kwargs)\n",
      "  File \"/usr/local/python/3.10.4/lib/python3.10/site-packages/click/core.py\", line 760, in invoke\n",
      "    return __callback(*args, **kwargs)\n",
      "  File \"/usr/local/python/3.10.4/lib/python3.10/site-packages/flask/cli.py\", line 911, in run_command\n",
      "    raise e from None\n",
      "  File \"/usr/local/python/3.10.4/lib/python3.10/site-packages/flask/cli.py\", line 897, in run_command\n",
      "    app = info.load_app()\n",
      "  File \"/usr/local/python/3.10.4/lib/python3.10/site-packages/flask/cli.py\", line 312, in load_app\n",
      "    app = locate_app(import_name, None, raise_if_not_found=False)\n",
      "  File \"/usr/local/python/3.10.4/lib/python3.10/site-packages/flask/cli.py\", line 218, in locate_app\n",
      "    __import__(module_name)\n",
      "  File \"/workspaces/codespaces-jupyter/app.py\", line 82, in <module>\n",
      "    \"execution_count\": null,\n",
      "NameError: name 'null' is not defined\n"
     ]
    }
   ],
   "source": [
    "!flask run\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f0183bea-627f-4583-8d55-8c62fde8fc13",
   "metadata": {},
   "outputs": [],
   "source": []
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
