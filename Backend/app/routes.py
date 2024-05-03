import os 
import datetime
import pandas as pd
from flask import request, jsonify
from app.helpers.psx_helper import create_vector_db, get_qa_chain
from app.helpers.psx_data import stocks_data
def init_routes(app):

    @app.route('/api/create_vector_db', methods=['GET'])
    def create_vector_db_1():
        symbols = ['SILK', 'PACE','KEL', 'WTL', 'BOP','PIAA', 'FABL', 'PAEL', 'AIRLINK', 'TOMCL', 'NBPXD', 'LOADS',
           'AGLNCPS', 'SGPL', 'FPRM', 'PIM', 'SAIF', 'LOADS', 'SMCPL', 'DAAG', 'THCCL', 'BELADEF',
           'HIRATDEF', 'FIBLM', 'TRSM', 'GFIL', 'RUBYDEF', 'BNL', 'NETSOL', 'TRG', 'AGL', 'HCL','PIBTL', 'FFL', 'FCCL','BOP','SNGP', 'GHNI', 'TELE', 'GAL', 'WAVES', 'HBLXD', 'SEARL', 'CSIL', 'SNBL', 'KOSM', 'FFC', 'OCTOPUS', 'JSBL', 'LOTCHEM', 'HUBC', 'PACE', 'EFERTXD', 'TPLP', 'ASC', 'HCAR', 'AKBL', 'AVNXDXB', 'LPL', 'HUMNL', 'POWER', 'DCL', 'RPL', 'HTL', 'PAKRIXD', 'GATM', 'NCPL', 'NPL', 'ASL', 'PSO', 'BAFL', 'KAPCO', 'SILK', 'ILP', 'FLYNG', 'WAVESAPP', 'ATRL', 'SAZEWXD', 'HIRATDEF', 'CPHL', 'AGHA', 'MEBLX']
        
        # start date should be today -2 days
        # end date should be today
        start_date = datetime.date.today() - datetime.timedelta(days=1)
        end_date = datetime.date.today()
        # Get stock data
        file_path = stocks_data(symbols, start=start_date, end=end_date)
        
        # Find country details
        vector_db = create_vector_db(file_path)
        return jsonify({"message": "Vector database created successfully."})
    

    @app.route('/api/ask_question', methods=['POST'])
    def ask_question():
        data = request.get_json()
        question = data.get('question')

        qa_chain = get_qa_chain()
        response = qa_chain(question)
        print(response,"response")
        answer = {"answer": response.get('result')}
        return jsonify(answer), 200