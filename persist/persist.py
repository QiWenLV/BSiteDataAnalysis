
class IPersist:

    def __init__(self):
        pass

    def write(self, to_sink, data, index=None):
        """
        写出数据
        :param to_sink: 文件名、数据表名
        :param data: 数据
        :param index: 主键(数据库的唯一标识，可以是数组)
        :return:
        """
        pass

    def read(self, source, filter):
        pass

    def count(self, source, filter) -> int:
        pass