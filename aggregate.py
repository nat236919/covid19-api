from models.covid_api_v2_model import (ActiveModel, ConfirmedModel,
                                         CountryModel, CurrentModel,
                                         DeathsModel,
                                         RecoveredModel,
                                         TimeseriesCaseCoordinatesModel,
                                         TimeseriesCaseDataModel,
                                         TimeseriesCaseModel,
                                         TimeseriesGlobalModel,
                                         TimeseriesUSCoordinatesModel,
                                         TimeseriesUSDataModel,
                                         TimeseriesUSInfoModel,
                                         TimeseriesUSModel, TotalModel)
from utils.get_data import (DailyReports, DataTimeSeries,
                              get_data_lookup_table)
#######################################
# CurrentModel
#######################################
class CurrentModel(BaseModel):
    Country_region: str
    confirmed: int
    deaths: int
    recovered:     intactive:int
#######################################################################################
    # GET - Current
    #######################################################################################
    @wrap_data
    def get_current(self) -> List[CurrentModel]:
        """ Current data from all locations (Lastest date) """
        if:
        self.df_US = self.daily_reports.get_data_daily_reports(US=True) # Get base data

        concerned_columns = ['Confirmed', 'Deaths', 'Recovered', 'Active']
        df = self.df_US.groupby(['Province_State'])[concerned_columns].sum().sort_values(by='Confirmed', ascending=False)
        df = df[concerned_columns].astype(int)
        df = df.reset_index()
        df.columns = ['Province_State'] + concerned_columns

        data = [CurrentUSModel(**v) for v in df.to_dict('index').values()]

        return data
        
        else:
        concerned_columns = ['Confirmed', 'Deaths', 'Recovered', 'Active']
        self.df = self.daily_reports.get_data_daily_reports() # Get base data
        self.df_grp_by_country = self.df.groupby('Country_Region')[concerned_columns].sum()
        self.df_grp_by_country[concerned_columns] = self.df_grp_by_country[concerned_columns].astype(int)

        df_grp_by_country = self.df_grp_by_country.sort_values(by='Confirmed', ascending=False)
        df_grp_by_country = df_grp_by_country.reset_index()
        df_grp_by_country.columns = ['location', 'confirmed', 'deaths', 'recovered', 'active']

        data = [CurrentModel(**v) for v in df_grp_by_country.to_dict('index').values()]

        return data
    
    
    
