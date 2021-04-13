from . import covid_api_v1_model
from . import covid_api_v2_model

class Model_Creator:

    # The version must either be a 1 or a 2, as the creator uses it to return the right model
    def __init__(self, version: int):
        self.version = version
    

    def get_ConfirmedModel(self, baseModel):
        if(self.version == 1):
            return covid_api_v1_model.ConfirmedModel(baseModel)
        elif(self.version == 2):
            return covid_api_v2_model.ConfirmedModel(baseModel)

    def get_CountriesModel(self, baseModel):
        if(self.version == 1):
            return covid_api_v1_model.CountriesModel(baseModel)


    def get_CurrentListModel(self, baseModel):
        if(self.version == 1):
            return covid_api_v1_model.CurrentListModel(baseModel)


    def get_CurrentModel(self, baseModel):
        if(self.version == 1):
            return covid_api_v1_model.CurrentModel(baseModel)
        elif(self.version == 2):
            return covid_api_v2_model.CurrentModel(baseModel)
    
    def get_DeathsModel(self, baseModel):
        if(self.version == 1):
            return covid_api_v1_model.DeathsModel(baseModel)
        elif(self.version == 2):
            return covid_api_v2_model.DeathsModel(baseModel)

    def get_RecoveredModel(self, baseModel):
        if(self.version == 1):
            return covid_api_v1_model.RecoveredModel(baseModel)
        elif(self.version == 2):
            return covid_api_v2_model.RecoveredModel(baseModel)
            
    def get_TimeseriesCoordinatesModel(self, baseModel):
        if(self.version == 1):
            return covid_api_v1_model.TimeseriesCoordinatesModel(baseModel)


    def get_TimeseriesDataModel(self, baseModel):
        if(self.version == 1):
            return covid_api_v1_model.TimeseriesDataModel(baseModel)

    
    def get_TimeseriesModel(self, baseModel):
        if(self.version == 1):
            return covid_api_v1_model.TimeseriesModel(baseModel)


    def get_TotalModel(self, baseModel):
        if(self.version == 1):
            return covid_api_v1_model.TotalModel(baseModel)
        elif(self.version == 2):
            return covid_api_v2_model.TotalModel(baseModel)



    ### Models available only for version 2
            
    def get_ActiveModel(self, baseModel):
        if(self.version == 2):
            return covid_api_v2_model.ActiveModel(baseModel)
    
    def get_CountryModel(self, baseModel):
        if(self.version == 2):
            return covid_api_v2_model.CountryModel(baseModel)
    
    def get_CurrentUSModel(self, baseModel):
        if(self.version == 2):
            return covid_api_v2_model.CurrentUSModel(baseModel)
    
    def get_TimeseriesCaseCoordinatesModel(self, baseModel):
        if(self.version == 2):
            return covid_api_v2_model.TimeseriesCaseCoordinatesModel(baseModel)
    
    def get_TimeseriesCaseDataModel(self, baseModel):
        if(self.version == 2):
            return covid_api_v2_model.TimeseriesCaseDataModel(baseModel)
    
    def get_TimeseriesCaseModel(self, baseModel):
        if(self.version == 2):
            return covid_api_v2_model.TimeseriesCaseModel(baseModel)
    
    def get_TimeseriesGlobalModel(self, baseModel):
        if(self.version == 2):
            return covid_api_v2_model.TimeseriesGlobalModel(baseModel)
    
    def get_TimeseriesUSCoordinatesModel(self, baseModel):
        if(self.version == 2):
            return covid_api_v2_model.TimeseriesUSCoordinatesModel(baseModel)
    
    def get_TimeseriesUSDataModel(self, baseModel):
        if(self.version == 2):
            return covid_api_v2_model.TimeseriesUSDataModel(baseModel)
    
    def get_TimeseriesUSInfoModel(self, baseModel):
        if(self.version == 2):
            return covid_api_v2_model.TimeseriesUSInfoModel(baseModel)
    
    def get_TimeseriesUSModel(self, baseModel):
        if(self.version == 2):
            return covid_api_v2_model.TimeseriesUSModel(baseModel)


    


