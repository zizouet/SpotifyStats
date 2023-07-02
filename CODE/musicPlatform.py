
from enum import Enum
import pandas as pd
import findspark

class PlatformSpecs(Enum):
    SPOTIFY = "SPOTIFY"
    DEEZER = "DEEZER"
    YTMUSIC = "YTMUSIC"

class Platform:
    def __init__(self, platform):
        self.platform = platform
        self.useFullCols=[]
        self.cols=[]
        self.data = []
        self.isData = False

        

#load JSON History with paths = [path1, ..., pathN]
    def loadFiles(self,paths):
        findspark.init()
        import pyspark # only run after findspark.init()
        from pyspark.sql import SparkSession
        spark = SparkSession.builder.getOrCreate()
        data = spark.read.option("multiLine", True).json(paths)
        self.data = data.toPandas()
        self.isData=True
