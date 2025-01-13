
    'object': types.String(length=None),
    'UUID()': types.UUID(),
    'VARCHAR(length=400)': types.String(length=400),
    'VARCHAR(length=250)': types.String(length=250),
    'VARCHAR(length=100)': types.String(length=100)
    'TEXT': types.Text(),



PD_TO_POSTGRES_DTYPES = {
    'bool': types.Boolean(),
    'int8': types.SmallInteger(),
    'int16': types.Integer(),
    'int32': types.BigInteger(),
    'int64': types.BigInteger(),
    'float16': types.Float(precision=3),
    'float32': types.Float(precision=6),
    'float64': types.Float(precision=15),
    'datetime64[ns]': types.DateTime(),
    'datetime64[ms]': types.DateTime(timezone=True),
    'timedelta64[ns]': types.Interval(),
    'timedelta64[ms]': types.Interval(type_='MICROSECOND'),
    'category': types.Enum(*[], create_constraint=False, name=None),
    'timestamp': types.DateTime(timezone=True),
    'bool': types.Boolean(),
}