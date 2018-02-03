import sqlite3
import pandas as pd
import numpy as np
from flask_restful import Resource, reqparse
from load_data import load_all_data

class TemperatureList(Resource):
    def get(self, region, year):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT  region_name,c_year, c_month, w_condition, w_value  FROM w_conditions " \
                "WHERE region_name='{}' AND c_year= {} ".format(region, year)
        result = cursor.execute(query)
        resultset=result.fetchall()
        if len(resultset) > 0:
            return self.serialize_temperature_data(resultset, year, region), 200
        return {'message':"Check the input data year: {}, region: {}. "
                          "No coincidences found in the database.".format(year,region)}, 404

    @staticmethod
    def serialize_temperature_data(resultset, year, region):
        temp_conditions=['Tmax','Tmin','Tmean']
        months = ['JAN', 'FEB', 'MAR', 'APR','MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
        all_arrays = [list(row) for row in resultset]
        all_matrix=np.array(all_arrays)
        regions = set(all_matrix[:,0])
        all_df = pd.DataFrame(all_matrix, columns = ['region', 'year', 'month', 'condition', 'value'])
        cond_dic={}
        for condition in temp_conditions:
            mont_values=[]
            for month in months:
                query = all_df[(all_df['region']==region) & (all_df['year']==year)
                               & (all_df['month']==month) & (all_df['condition']==condition)] ['value']
                if not query.empty:
                    value = float(query.iloc[0])
                else:
                    value = 'na'
                mont_values.append(value)
            cond_dic.update({condition: mont_values})
        return cond_dic


class RegionCompare(Resource):

    def get(self, year, condition):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT  region_name,c_year, c_month, w_condition, w_value  FROM w_conditions " \
                "WHERE c_year={} AND w_condition= '{}' ".format(year,condition)
        result = cursor.execute(query)
        resultset=result.fetchall()
        if len(resultset) > 0:
            return self.serialize_compare_data(resultset, year, condition), 200
        return {'message':"Check the input data year: {}, condition: {}. "
                          "No coincidences found in the database.".format(year,condition)}, 404

    @staticmethod
    def serialize_compare_data(resultset, year, condition):
        all_arrays = [list(row) for row in resultset]
        all_matrix=np.array(all_arrays)
        regions = set(all_matrix[:,0])
        months = ['JAN', 'FEB', 'MAR', 'APR','MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
        all_df = pd.DataFrame(all_matrix, columns = ['region', 'year', 'month', 'condition', 'value'])
        r_dic={}
        for region in regions:
            mont_values=[]
            for month in months:
                query = all_df[(all_df['region']==region) & (all_df['year']==year)
                               & (all_df['month']==month) & (all_df['condition']==condition)] ['value']
                if not query.empty:
                    value = float(query.iloc[0])
                else:
                    value = 'na'
                mont_values.append(value)
            r_dic.update({region: mont_values})
        return r_dic


class ConditionList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT DISTINCT w_condition FROM w_conditions"
        result = cursor.execute(query)
        resultset=result.fetchall()
        if len(resultset) > 0:
            conditions=[condition[0] for condition in resultset]
            return {'conditions': conditions}, 200
        return {'message':"No conditions found in de DB"}, 404


class YearList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT DISTINCT c_year FROM w_conditions"
        result = cursor.execute(query)
        resultset=result.fetchall()
        if len(resultset) > 0:
            years=[year[0] for year in resultset]
            return {'years': years}, 200
        return {'message':"No years found in de DB"}, 404


class RegionList(Resource):
    # Exceutes the method that populate/update the database
    # This method should be called first to Create/Update the DB information
    load_all_data()
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT DISTINCT region_name FROM w_conditions"
        result = cursor.execute(query)
        resultset=result.fetchall()
        if len(resultset) > 0:
            regions=[region[0] for region in resultset]
            return {'regions': regions}, 200
        return {'message':"No regions found in de DB"}, 404
