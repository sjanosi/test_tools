import plotly
import plotly.graph_objects as go


class Chart(object):
    """
    a chart represents a certain timeframe candlesticks
    """
    # a dictionary of all candles { unix_time : candle }
    candles_dict = {}
    candles = []

    def __init__(self, pair, timeframe, logger):
        self.pair = pair


    def plot_candles(self):
        """
        creates an offline plot as a html file
        """
        # get the touch string
        self.plot_fig = go.Figure(data=[go.Candlestick(x=[candle.h_open_time for candle in self.candles],
                                                       open=[candle.open for candle in self.candles],
                                                       high=[candle.high for candle in self.candles],
                                                       low=[candle.low for candle in self.candles],
                                                       close=[candle.close for candle in self.candles],
                                                       increasing_line_color='white', decreasing_line_color='grey',
                                                       hovertext=[candle.touch_string for candle in self.candles])])
        plotly.offline.plot(self.plot_fig, auto_open=False, filename=self.h_timeframe + '-chart.html')


    def plot_pattern_fractals(self):
        """
        plot the pattern fractals as colored candles
        """
        self.plot_fig.add_trace(go.Candlestick(x=[candle.h_open_time for candle in self.yang_pattern_candles],
                                               open=[candle.open for candle in self.yang_pattern_candles],
                                               high=[candle.high for candle in self.yang_pattern_candles],
                                               low=[candle.low for candle in self.yang_pattern_candles],
                                               close=[candle.close for candle in self.yang_pattern_candles],
                                               increasing_line_color='blue', decreasing_line_color='blue',
                                               hovertext=[candle.touch_string for candle in self.yang_pattern_candles]))
        plotly.offline.plot(self.plot_fig, auto_open=False, filename=self.h_timeframe + '-chart.html')


    def plot_volume(self):
        pass

        # add the level with the most volume
        # high_vol_lvls = self.levels.get_high_volume_levels()
        # highest_vol_lvl = high_vol_lvls[-1]
        # self.plot_fig.add_trace(go.Candlestick(x=df1.index,
        #                              open=df1['O'],
        #                              high=df1['H'],
        #                              low=df1['L'],
        #                              close=df1['C'],
        #                              increasing_line_color='red', decreasing_line_color='red', hovertext='yo!'))

        # TODO: only color the candles that make up the highest volume level
        # self.plot_fig.add_hline(y=high_vol_lvls[-1].value, annotation={'y': str(highest_vol_lvl.volume)})


