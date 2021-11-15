import cufflinks as cf
import pandas as pd
from persist.persist import IPersist
from persist.mongo_persist import MongoPersist

if __name__ == '__main__':
    cf.set_config_file(world_readable=True, theme='henanigans', offline=True)
    cf.go_offline()
    upid = 176037767
    mongo_persist = MongoPersist()
    data_dict = mongo_persist.read("up_video_list", {"mid": upid})
    df_data = pd.DataFrame(data_dict)
    df_data['created'] = pd.to_datetime(df_data['created'], unit='s')
    # df_data.iplot(kind='bubble',x='created',y='play',size='stat#like')
    # df_data.iplot(kind='histogram', x='created', y='stat#like')
    df1 = df_data[['created', 'stat#favorite', 'stat#coin', 'stat#like']]
    # df1 = df1.set_index('created')
    # df1.iplot(kind='bar', barmode='stack', orientation='h')
    df2 = df1.groupby([df1.created.dt.year, df1.created.dt.month]).agg('sum')
    df2.iplot(kind='bar', barmode='stack', orientation='v')

    df3 = df_data[['created', 'stat#favorite', 'stat#coin', 'stat#like', 'play']]
    df3 = df3.groupby([df1.created.dt.year, df1.created.dt.month]).agg('sum')
    df3['like_rate'] = df3['stat#like'] / df3['play']
    df3['favorite_rate'] = df3['stat#favorite'] / df3['play']
    df3['coin_like_rate'] = df3['stat#coin'] / df3['stat#like']
    df3 = df3[['like_rate', 'favorite_rate', 'coin_like_rate']]
    # df3['like_rate'] = df3['like_rate'].apply(lambda x: '%.2f%%' % (x * 100))
    # df3['favorite_rate'] = df3['favorite_rate'].apply(lambda x: '%.2f%%' % (x * 100))
    # df3['coin_like_rate'] = df3['coin_like_rate'].apply(lambda x: '%.2f%%' % (x * 100))
    df3.iplot(kind='lines', orientation='v',
              title='Loss Exposure', xTitle='USD', yTitle='Relative Frequency')
    