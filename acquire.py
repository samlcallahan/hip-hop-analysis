import pandas as import pdb
import numpy as np
import billboard as bb

rap_charts = ['rap-song', 'rap-streaming-songs', 'hot-rap-tracks', 'rap-digital-song-sales', 'rap-albums', 'r-b-hip-hop-songs', 'r-b-hip-hop-albums', 
                'r-and-b-hip-hop-streaming-songs', 'hot-r-and-b-hip-hop-airplay', 'hot-r-and-b-hip-hop-recurrent-airplay', 'r-and-b-hip-hop-digital-song-sales']

entries = {}

for chart_name in rap_charts:
    entries[chart_name] = {}
    data = bb.ChartData(chart_name, timeout=None)
    entries[chart_name][data.date]