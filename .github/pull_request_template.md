### Related Issue:

* Aggregation could be applied to the code design in certain spots
* I've added some aggregation in the covid_api_v2_models.py class



### Proposed Changes

* The CurrentModel class can be inherited by several other classes like ConfirmedModel, DeathsModel, RecoveredModel, ActiveModel, CountryModel and TotalModel to make the design smoother

### Addtional Info

- any additional information or context

### Checklist

* [ ] Tests
* [ ] Translations
* [ ] Documentation

### Screenshots

* screenshot 1
![CurrentAggregation](https://user-images.githubusercontent.com/56807471/111401179-2692a980-869f-11eb-8d2f-9344e0025d2b.png)
