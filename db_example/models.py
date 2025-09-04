from django.db import models


class StructureInventory(models.Model):
    # lot_ext_id = models.IntegerField()
    # lot_desc = models.IntegerField()
    # de_ext_id = models.IntegerField()
    # de_desc = models.IntegerField()
    # de_type = models.CharField()
    # f_type = models.CharField()
    # c_type = models.CharField()
    # a_type = models.CharField()
    # struct_min = models.DecimalField(max_digits=15, decimal_places=5)
    # struct_ml = models.DecimalField(max_digits=15, decimal_places=5)
    # struct_max = models.DecimalField(max_digits=15, decimal_places=5)
    # content_min = models.DecimalField(max_digits=15, decimal_places=5)
    # content_ml = models.DecimalField(max_digits=15, decimal_places=5)
    # content_max = models.DecimalField(max_digits=15, decimal_places=5)
    # de_width = models.FloatField()
    # de_length = models.FloatField()
    # ffe_min = models.FloatField()
    # ffe_ml = models.FloatField()
    # ffe_max = models.FloatField()
    # num_of_floor = models.IntegerField()
    # t_build_min = models.IntegerField()
    # t_build_ml = models.IntegerField()
    # t_build_max = models.IntegerField()
    # build_num = models.IntegerField()
    # de_active = models.BooleanField()
    # rep_pt_n = models.FloatField()
    # rep_pt_e = models.FloatField()

    # TODO: Check if the column names have to be the same for an import

    LotExtID = models.IntegerField()
    LotDesc = models.IntegerField()
    DEExtID = models.IntegerField(primary_key=True)
    DEDesc = models.IntegerField()
    DEType = models.CharField()
    Ftype = models.CharField()
    Ctype = models.CharField()
    Atype = models.CharField()
    StructMin = models.DecimalField(max_digits=15, decimal_places=5)
    StructML = models.DecimalField(max_digits=15, decimal_places=5)
    StructMax = models.DecimalField(max_digits=15, decimal_places=5)
    ContentMin = models.DecimalField(max_digits=15, decimal_places=5)
    ContentML = models.DecimalField(max_digits=15, decimal_places=5)
    ContentMax = models.DecimalField(max_digits=15, decimal_places=5)
    DEWidth = models.FloatField()
    DELength = models.FloatField()
    FFEMin = models.FloatField()
    FFEML = models.FloatField()
    FFEMax = models.FloatField()
    NumOfFloor = models.IntegerField()
    TBuildMin = models.IntegerField()
    TBuildML = models.IntegerField()
    TBuildMax = models.IntegerField()
    BuildNum = models.IntegerField()
    DEActive = models.IntegerField()
    RepPtN = models.FloatField()
    RepPtE = models.FloatField()








