import numpy
import pandas as pd
pd.read_csv('data/rain_data_2015-12.csv',usecols=['Site', 'Date', 'Rainfall (mm)'])

from catchment import models
dataset = models.read_variable_from_csv('data/rain_data_2015-12.csv')
#print(dataset.shape)
#print(dataset)

def daily_total(data):
    """Calculate the daily total of a 2D data array.

    :param data: A 2D Pandas data frame with measurement data.
                 Index must be np.datetime64 compatible format. Columns are measurement sites.
    :returns: A 2D Pandas data frame with total values of the measurements for each day.
    """
    return data.groupby(data.index.date).sum()

sample_dataset = models.read_variable_from_csv('data/rain_data_small.csv')
print(sample_dataset)

from catchment.models import daily_total

print(daily_total(sample_dataset))

import pandas as pd
import pandas.testing as pdt
from catchment.models import daily_mean
import datetime

test_input = pd.DataFrame(
                data=[[2.0, 0.0],
                      [4.0, 0.0]],
                index=[pd.to_datetime('2000-01-01 01:00'),
                       pd.to_datetime('2000-01-01 02:00')],
                columns=['A', 'B']
)
test_result = pd.DataFrame(
                 data=[[3.0, 0.0]],
                 index=[datetime.date(2000, 1, 1)],
                 columns=['A', 'B']
)
print(pdt.assert_frame_equal(daily_mean(test_input), test_result))

test_input = pd.DataFrame(
                data=[[0.0, 0.0],
                      [0.0, 0.0]],
                index=[pd.to_datetime('2000-01-01 01:00'),
                       pd.to_datetime('2000-01-01 02:00')],
                columns=['A', 'B']
)
test_result = pd.DataFrame(
                 data=[[0.0, 0.0]],
                 index=[datetime.date(2000, 1, 1)],
                 columns=['A', 'B']
)
print(pdt.assert_frame_equal(daily_mean(test_input), test_result))

test_input = pd.DataFrame(
                data=[[1.0, 2.0],
                      [3.0, 4.0],
                      [5.0, 6.0]],
                index=[pd.to_datetime('2000-01-01 01:00'),
                       pd.to_datetime('2000-01-01 02:00'),
                       pd.to_datetime('2000-01-01 03:00')],
                columns=['A', 'B']
)
test_result = pd.DataFrame(
                 data=[[3.0, 4.0]],
                 index=[datetime.date(2000, 1, 1)],
                 columns=['A', 'B']
)
print(pdt.assert_frame_equal(daily_mean(test_input), test_result))