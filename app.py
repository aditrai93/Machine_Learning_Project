from flask import Flask
from housing.exception import HousingException
from housing.logger import logging
import sys
app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception('we are testing exception')
    except Exception as e:
        housing=HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info('testing log')
    return "Sucessfully deployed with CI"

if __name__=='__main__':
    app.run(debug=True)