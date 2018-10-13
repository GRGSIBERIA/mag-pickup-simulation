#-*- encoding: utf-8
import csv
from numpy as np 

class Coil:
    def __init__(self, path: str):
        """
        :param path: コイルのデータ

        .. Note:
        コイルのデータは以下のCSVフォーマットで代入する
        Pはコイルの位置，ZはコイルのZ向き
        時間, Px, Py, Pz, Zx, Zy, Zz
        
        ヘッダ行は必ず挿入し，不要な場合は空行にする
        """
        self.times = []
        self.position = []
        self.direction = []

        rows = []
        with open(path, "r") as f:
            reader = csv.reader(f)
            next(reader)    # ヘッダを読み飛ばす

            for row in reader:
                rows.append(row)
        
        