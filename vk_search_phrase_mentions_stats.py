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
    day_pariod_in_seconds = 86400
    for number in range(days_range):
        end_timestamp = start_timestamp - day_pariod_in_seconds
        datetime_date = start_date - datetime.timedelta(days = number)
        dates = [datetime_date,
                 start_timestamp,
                 end_timestamp
                 ]
        dates_range.append(dates)
        start_timestamp = start_timestamp - day_pariod_in_seconds
    return dates_range


def get_vk_response_contents(search_phrase,
                            dates_range,
                            vk_service_token):
    url = 'https://api.vk.com/method/newsfeed.search'
    number_of_posts = 1
    response_contents = []
    for calendar_date, end_time_stamp, start_time_stamp in dates_range:
        params = {'q': search_phrase,
                  'count': number_of_posts,
                  'start_time': start_time_stamp,
                  'end_time': end_time_stamp,
                  'access_token': vk_service_token,
                  'v': 5.21
                  }
        response = requests.get(url, params=params)
        response.raise_for_status()
        vk_response_content = response.json()
        response_contents.append(vk_response_content)

    return response_contents

def get_x_and_y_values(response_contents):
    data_for_x_value = []
    data_for_y_value = []
    for response_content in response_contents:
        phrase_count = response_content['response']['total_count']
        date_timestamp = response_content['response']['items'][0]['date']
        date_from_timestamp = datetime.date.fromtimestamp(date_timestamp)
        data_for_x_value.append(date_from_timestamp)
        data_for_y_value.append(phrase_count)
    data_for_x_value.reverse()
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
    vk_response_content = get_vk_response_contents(search_phrase,
                                                              dates_range,
                                                              vk_service_token)

    x_value, y_value = get_x_and_y_values(vk_response_content)

    get_stats_chart(x_value,
                    y_value,
                    search_phrase)


if __name__ == '__main__':
    main()
