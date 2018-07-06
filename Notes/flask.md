#init virtual env
mkdir flaskdir
cd flaskdir
virtualenv venv

#active virtual env
. venv/bin/activate

#deactive vitual env
deactivate

#start flsak app
export FLASK_APP=explore.py
flask run --host=0.0.0.0

#dev mode (auto restart and load changed file)
export FALSK_ENV=development


# run on the internet rather locally
flask run --host=0.0.0.0


#run on python3 interpreter
app.run(debug=True,host='0.0.0.0',port='10001')
