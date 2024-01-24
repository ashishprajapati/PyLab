from datetime import datetime, timedelta

# Historical data of SENSEX milestones
milestones = {
    1000: "1990-07-25",
    2000: "1992-01-15",
    3000: "1992-02-29",
    4000: "1992-03-30",
    5000: "1999-10-11",
    6000: "2000-02-11",
    7000: "2005-06-20",
    8000: "2005-09-08",
    9000: "2005-12-09",
    10000: "2006-02-07",
    20000: "2007-12-11",
    21000: "2010-11-05",
    22000: "2014-03-24",
    23000: "2014-05-09",
    24000: "2014-05-13",
    25000: "2014-05-16",
    26000: "2014-07-07",
    27000: "2014-09-02",
    28000: "2014-11-05",
    29000: "2015-01-23",
    30000: "2015-03-04",
    31000: "2017-05-26",
    32000: "2017-07-13",
    33000: "2017-10-25",
    34000: "2017-12-26",
    35000: "2018-01-17",
    36000: "2018-01-23",
    37000: "2018-07-27",
    38000: "2018-08-09",
    39000: "2019-04-01",
    40000: "2019-05-23",
    41000: "2019-11-26",
    42000: "2020-01-16",
    45000: "2020-12-04",
    46000: "2020-12-09",
    50000: "2021-01-21",
    60000: "2021-09-24",
    70000: "2023-12-11"
}

# Convert dates to datetime objects
milestones = {k: datetime.strptime(v, "%Y-%m-%d") for k, v in milestones.items()}

# Calculate the time intervals between each milestone
intervals = {}
previous_milestone = None
previous_date = None
for milestone, date in milestones.items():
    if previous_milestone is not None:
        interval = (date - previous_date).days
        intervals[previous_milestone] = interval
    previous_milestone = milestone
    previous_date = date

# Focusing on the intervals from 30,000 points onwards
recent_intervals = {k: v for k, v in intervals.items() if k >= 30000}

# Calculate the average interval
average_interval = sum(recent_intervals.values()) / len(recent_intervals)

# Predict the date for the 80,000 milestone
last_milestone_date = milestones[70000]
predicted_date_80000 = last_milestone_date + timedelta(days=average_interval)

# Output the predicted date
print("Predicted date for SENSEX to reach 80,000: ", predicted_date_80000.strftime("%Y-%m-%d"))