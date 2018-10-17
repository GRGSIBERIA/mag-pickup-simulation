#-*- encoding: utf-8
import csv
import numpy as np 
from typing import Dict

class DataSheet:
    """
    データシートの基底クラス
    パスを読み込んで行列に直すだけ
    """
    def __init__(self, **kwargs:dict):
        if kwargs.has_key("path"):
            path = kwargs["path"]
            has_header = True
            if kwargs.has_key("has_header"):
                has_header = kwargs["has_header"]
            self._rows = []
            with open(path, "r") as f:
                reader = csv.reader(f)

                if has_header:
                    next(reader)    # ヘッダを読み飛ばす

                for row in reader:
                    data = []
                    for datum in row:
                        data.append(float(datum))   # float型変換を忘れずに
                    self._rows.append(data)

class TimePosition(DataSheet):
    """
    時間と座標値に対応したデータシートの抽象基底クラス
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.times = []
        self.positions = []

        if kwargs.has_key("path"):
            for row in self._rows:
                self.times.append(row[0])
                ws = []
                columns = int((len(row)-1) / 3)
                for n in range(columns):
                    # 先頭行が時間なので1スタート
                    num = n*3+1
                    ws.append(np.array(row[num:num+3]))
                self.positions.append(ws)
            self.times = np.array(self.times)
            self._rows = None
        else:
            self.times = kwargs["times"]
            self.positions = kwargs["positions"]

class Coil(TimePosition):
    """
    コイルのデータシート
    """
    def __init__(self, **kwargs):
        """
        引数は以下の値を取り得る
        Coil(path=str, has_header=bool(optional)) の場合 ::
            :param path: CSVファイルのパス
            :param has_header: ヘッダ行を読み込む，デフォルトはTrue
        Coil(times=list[numpy.array], positions=list[numpy.array])
            :param times: 時間
            :param positions: 座標値

        .. Note:
        コイルのデータは以下のCSVフォーマットで代入する
        ``t, Px, Py, Pz``
        tは時間，Pはコイルの位置，ZはコイルのZ向き
        """
        super().__init__(**kwargs)

class Wire(TimePosition):
    """
    ワイヤーのデータシート
    """
    def __init__(self, **kwargs):
        """
        引数は以下の値を取り得る
        Wire(path=str, has_header=bool(optional)) の場合 ::
            :param path: CSVファイルのパス
            :param has_header: ヘッダ行を読み込む，デフォルトはTrue
        Wire(times=list[numpy.array], positions=list[list[numpy.array]]) の場合 ::
            :param times: 時間
            :param positions: 質点数に対応した座標値の2次元配列

        .. Note:
        ワイヤーのデータは以下のCSVフォーマットで代入する
        ``t, P0x, P0y, P0z, P1x, P1y, P1z, ..., Pnx, Pny, Pnz``
        tは時間，Pnは質点位置，nは質点番号
        ランダムな質点だと非常に不揃いなデータになるので連続性を持たせること
        """
        super().__init__(**kwargs)
        