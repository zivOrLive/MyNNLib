from DAL.Mongo.CollectionExecuter import _CollectionExectuer

class _Getter(_CollectionExectuer):
    def __init__(self, collection):
        super().__init__(collection)

    def getLocalReceptiveFieldSize(self, layerId):
        json = self.getScalarByLayerIdAndType(layerId, "local_receptive_field_size")
        return [json.H, json.W]