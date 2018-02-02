
class ClimateData:

    def __init__(self):
        self.dataframe=[]

    def get_climate_conditions(self, condition_name):
        return self.climate_conditions[condition_name]

    def add_condition(self, condition_set):
        pass