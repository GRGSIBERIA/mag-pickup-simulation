#-*- encoding: utf-8
import csv
import numpy as np 

class DataSheet:
    """
    データシートの基底クラス
    パスを読み込んで行列に直すだけ
    """
    def __init__(self, path: str, hasHeader=True):
        """
        :param path: データのパス
        :param hasHeader: ヘッダの有無
        """
        self._rows = []
        with open(path, "r") as f:
            reader = csv.reader(f)

            if hasHeader:
                next(reader)    # ヘッダを読み飛ばす

            for row in reader:
                data = []
                for datum in row:
                    data.append(float(datum))   # float型変換を忘れずに
                self._rows.append(data)

class Coil(DataSheet):
    """
    コイルのデータシート
    """
    def __init__(self, path: str, hasHeader=True):
        """
        :param path: コイルのデータパス
        :param hasHeader: ヘッダの有無

        .. Note:
        コイルのデータは以下のCSVフォーマットで代入する
        Pはコイルの位置，ZはコイルのZ向き
        時間, Px, Py, Pz, Zx, Zy, Zz
        """
        super().__init__(path, hasHeader)
        self.times = []
        self.position = []
        self.direction = []
        
        for row in self._rows:
            self.times.append(row[0])
            self.position.append(np.array(row[1:4]))
            self.direction.append(np.array(row[4:7]))
        self.times = np.array(self.times)
        self._rows = None

class Wire(DataSheet):
    """
    ワイヤーのデータシート
    """
    def __init__(self, path: str, hasHeader=True):
        """
        :param path: ワイヤーのデータパス
        :param hasHeader: ヘッダの有無

        .. Note:
        ワイヤーのデータは以下のCSVフォーマットで代入する
        Pnは質点位置，nは質点番号（ランダムな質点だと非常に不揃いなデータになる）
        時間, P0x, P0y, P0z, P1x, P1y, P1z, ..., Pnx, Pny, Pnz
        """
        super().__init__(path, hasHeader)
        self.times = []
        self.wires = []

        for row in self._rows:
            self.times.append(row[0])
            ws = []
            for n in range((len(row)-1) / 3):
                ws.append(np.array([row[n*3+1], row[n*3+2], row[n*3+3]))    # 先頭行が時間なので1スタート
            self.wires.append(ws)
        self.times = np.array(self.times)
        self._rows = None