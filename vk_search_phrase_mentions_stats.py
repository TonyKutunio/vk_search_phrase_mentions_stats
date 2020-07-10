import os
import datetime
import requests
import plotly.graph_objects as go
import chart_studio
from dotenv import load_dotenv



def get_time_stamp(year, month,
                   day,  hour=0,
                   minute=0, second=0):

    timestamp = datetime.datetime(year=year,
                                  month=month,
                                  day=day,
                                  hour=hour,
                                  minute=minute,
                                  second=second).timestamp()
    return int(timestamp)


def get_dates_range(start_timestamp, days_range):
    dates_range = []
    start_date = datetime.date.fromtimestamp(start_timestamp)
    for number in range(days_range):
        end_timestamp = start_timestamp - 86400
        datetime_date = start_date - datetime.timedelta(days = number)
        dates = [datetime_date,
                 start_timestamp,
                 end_timestamp
                 ]
        dates_range.append(dates)
        start_timestamp = start_timestamp - 86400
    return dates_range


def get_x_and_y_values(search_phrase, dates_range, vk_service_token):
    url = 'https://api.vk.com/method/newsfeed.search'
    number_of_posts = 1
    index = 0
    data_for_x_value = []
    data_for_y_value = []
    for date in dates_range:
        start_time = date[2]
        end_time = date[1]
        params = {'q': search_phrase,
                  'count': number_of_posts,
                  'start_time': start_time,
                  'end_time': end_time,
                  'access_token': vk_service_token,
                  'v': 5.21
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        response_content = response.json()
        index += 1
        phrase_count = response_content['response']['total_count']

        data_for_x_value.append(date[0])
        data_for_x_value.reverse()
        data_for_y_value.append(phrase_count)
        data_for_y_value.reverse()
    return data_for_x_value, data_for_y_value


def get_stats_chart(x_value, y_value, title):
    fig = go.Figure(
        data=[go.Bar(y=y_value, x=x_value)
              ], layout_title_text=title,
    )
    return fig.show()


def main():
    load_dotenv()
    vk_service_token = os.getenv('VK_SERVICE_TOKEN')
    plotly_username = os.getenv('PLOTLY_USERNAME')
    plotly_api_key = os.getenv('PLOTLY_API_KEY')
    chart_studio.tools.set_credentials_file(username=plotly_username,
                                            api_key=plotly_api_key)

    search_phrase = 'search phrase'
    days_range = 7

    start_date = datetime.date.today()
    start_date_timestamp = get_time_stamp(start_date.year,
                                          start_date.month,
                                          start_date.day)

    dates_range = get_dates_range(start_date_timestamp, days_range)
    x_value, y_value = get_x_and_y_values(search_phrase,
                                          dates_range,
                                          vk_service_token)

    get_stats_chart(x_value,
                    y_value,
                    search_phrase)


if __name__ == '__main__':
    main()

