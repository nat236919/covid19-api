# Import libraries
from datetime import datetime
from typing import Any, Dict, List

import pandas as pd
from utils.get_data import get_data
import models.covid_model_api_v1
import models.covid_model_api_v2

class APIversionAdapter:
    def __init__(self):
        self.version1 = CovidAPIv1()
        self.version2 = CovidAPIv2()
    
    def get_confirmed(self, v):
        if v == 1: 
            version1.get_confirmed_cases()
        if v == 2:
            version2.get_confirmed()
    
    def get_death(self, v):
        if v == 1:
            version1.get_deaths()
        if v == 2:
            version2.get_deaths()
    
    def get_recovered(self, v):
        if v == 1:
            version1.get_recovered()
        if v == 2:
            version2.get_recovered()