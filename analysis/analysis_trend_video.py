import cufflinks as cf
import pandas as pd
from persist.persist import IPersist
from persist.mongo_persist import MongoPersist


class AnalysisVideo:
    def __init__(self, upid):
        cf.set_config_file(world_readable=True, theme='henanigans', offline=True)
        cf.go_offline()
        self.mongo_persist = MongoPersist()
        self.upid = upid
        data_dict = self.mongo_persist.read("up_video_list", {"mid": upid})
        self.df_data = pd.DataFrame(data_dict)
        self.df_data['created'] = pd.to_datetime(self.df_data['created'], unit='s')



    def month_video_play_rate(self):
        df3 = self.df_data[['created', 'stat#favorite', 'stat#coin', 'stat#like', 'play']]
        df3 = df3.groupby([df3.created.dt.year, df3.created.dt.month]).agg('sum')
        df3['like_rate'] = df3['stat#like'] / df3['play']
        df3['favorite_rate'] = df3['stat#favorite'] / df3['play']
        df3['coin_like_rate'] = df3['stat#coin'] / df3['stat#like']
        df3 = df3[['like_rate', 'favorite_rate', 'coin_like_rate']]
        df3.iplot(kind='lines', orientation='v',
                  title='up视频质量走势参考', xTitle='时间', yTitle='比率')
        return df3.figure(kind='lines', orientation='v', )

    def month_video_play(self):
        df1 = self.df_data[['created', 'stat#favorite', 'stat#coin', 'stat#like']]
        df2 = df1.groupby([df1.created.dt.year, df1.created.dt.month]).agg('sum')
        # df2.iplot(kind='bar', barmode='stack', orientation='v')
        df2.iplot(kind='histogram', bins=10)
        return df2


if __name__ == '__main__':
    upid = 176037767
    analysis_video = AnalysisVideo(upid)
    figs = cf.figures(analysis_video.month_video_play(), [dict(kind='bar', barmode='stack')], asList=True)
    figs.append(analysis_video.month_video_play_rate())
    layout = cf.tools.get_base_layout(figs)
    sp = cf.subplots(figs, shape=(1, 2), base_layout=layout)
    sp['layout'].update(showlegend=False)
    cf.iplot(sp)
