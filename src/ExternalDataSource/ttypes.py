#
# Autogenerated by Thrift Compiler (0.9.1)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import Status.ttypes
import Data.ttypes
import Types.ttypes


from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class TComparisonOp(object):
  LT = 0
  LE = 1
  EQ = 2
  NE = 3
  GE = 4
  GT = 5

  _VALUES_TO_NAMES = {
    0: "LT",
    1: "LE",
    2: "EQ",
    3: "NE",
    4: "GE",
    5: "GT",
  }

  _NAMES_TO_VALUES = {
    "LT": 0,
    "LE": 1,
    "EQ": 2,
    "NE": 3,
    "GE": 4,
    "GT": 5,
  }


class TColumnDesc(object):
  """
  Attributes:
   - name
   - type
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'name', None, None, ), # 1
    (2, TType.STRUCT, 'type', (Types.ttypes.TColumnType, Types.ttypes.TColumnType.thrift_spec), None, ), # 2
  )

  def __init__(self, name=None, type=None,):
    self.name = name
    self.type = type

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.type = Types.ttypes.TColumnType()
          self.type.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TColumnDesc')
    if self.name is not None:
      oprot.writeFieldBegin('name', TType.STRING, 1)
      oprot.writeString(self.name)
      oprot.writeFieldEnd()
    if self.type is not None:
      oprot.writeFieldBegin('type', TType.STRUCT, 2)
      self.type.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TTableSchema(object):
  """
  Attributes:
   - cols
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'cols', (TType.STRUCT,(TColumnDesc, TColumnDesc.thrift_spec)), None, ), # 1
  )

  def __init__(self, cols=None,):
    self.cols = cols

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.LIST:
          self.cols = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = TColumnDesc()
            _elem5.read(iprot)
            self.cols.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TTableSchema')
    if self.cols is not None:
      oprot.writeFieldBegin('cols', TType.LIST, 1)
      oprot.writeListBegin(TType.STRUCT, len(self.cols))
      for iter6 in self.cols:
        iter6.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TRowBatch(object):
  """
  Attributes:
   - cols
   - num_rows
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'cols', (TType.STRUCT,(Data.ttypes.TColumnData, Data.ttypes.TColumnData.thrift_spec)), None, ), # 1
    (2, TType.I64, 'num_rows', None, None, ), # 2
  )

  def __init__(self, cols=None, num_rows=None,):
    self.cols = cols
    self.num_rows = num_rows

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.LIST:
          self.cols = []
          (_etype10, _size7) = iprot.readListBegin()
          for _i11 in xrange(_size7):
            _elem12 = Data.ttypes.TColumnData()
            _elem12.read(iprot)
            self.cols.append(_elem12)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.num_rows = iprot.readI64();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TRowBatch')
    if self.cols is not None:
      oprot.writeFieldBegin('cols', TType.LIST, 1)
      oprot.writeListBegin(TType.STRUCT, len(self.cols))
      for iter13 in self.cols:
        iter13.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.num_rows is not None:
      oprot.writeFieldBegin('num_rows', TType.I64, 2)
      oprot.writeI64(self.num_rows)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TBinaryPredicate(object):
  """
  Attributes:
   - col
   - op
   - value
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'col', (TColumnDesc, TColumnDesc.thrift_spec), None, ), # 1
    (2, TType.I32, 'op', None, None, ), # 2
    (3, TType.STRUCT, 'value', (Data.ttypes.TColumnValue, Data.ttypes.TColumnValue.thrift_spec), None, ), # 3
  )

  def __init__(self, col=None, op=None, value=None,):
    self.col = col
    self.op = op
    self.value = value

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.col = TColumnDesc()
          self.col.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.op = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRUCT:
          self.value = Data.ttypes.TColumnValue()
          self.value.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TBinaryPredicate')
    if self.col is not None:
      oprot.writeFieldBegin('col', TType.STRUCT, 1)
      self.col.write(oprot)
      oprot.writeFieldEnd()
    if self.op is not None:
      oprot.writeFieldBegin('op', TType.I32, 2)
      oprot.writeI32(self.op)
      oprot.writeFieldEnd()
    if self.value is not None:
      oprot.writeFieldBegin('value', TType.STRUCT, 3)
      self.value.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TPrepareParams(object):
  """
  Attributes:
   - table_name
   - init_string
   - predicates
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'table_name', None, None, ), # 1
    (2, TType.STRING, 'init_string', None, None, ), # 2
    (3, TType.LIST, 'predicates', (TType.LIST,(TType.STRUCT,(TBinaryPredicate, TBinaryPredicate.thrift_spec))), None, ), # 3
  )

  def __init__(self, table_name=None, init_string=None, predicates=None,):
    self.table_name = table_name
    self.init_string = init_string
    self.predicates = predicates

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.table_name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.init_string = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.predicates = []
          (_etype17, _size14) = iprot.readListBegin()
          for _i18 in xrange(_size14):
            _elem19 = []
            (_etype23, _size20) = iprot.readListBegin()
            for _i24 in xrange(_size20):
              _elem25 = TBinaryPredicate()
              _elem25.read(iprot)
              _elem19.append(_elem25)
            iprot.readListEnd()
            self.predicates.append(_elem19)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TPrepareParams')
    if self.table_name is not None:
      oprot.writeFieldBegin('table_name', TType.STRING, 1)
      oprot.writeString(self.table_name)
      oprot.writeFieldEnd()
    if self.init_string is not None:
      oprot.writeFieldBegin('init_string', TType.STRING, 2)
      oprot.writeString(self.init_string)
      oprot.writeFieldEnd()
    if self.predicates is not None:
      oprot.writeFieldBegin('predicates', TType.LIST, 3)
      oprot.writeListBegin(TType.LIST, len(self.predicates))
      for iter26 in self.predicates:
        oprot.writeListBegin(TType.STRUCT, len(iter26))
        for iter27 in iter26:
          iter27.write(oprot)
        oprot.writeListEnd()
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TPrepareResult(object):
  """
  Attributes:
   - status
   - num_rows_estimate
   - accepted_conjuncts
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'status', (Status.ttypes.TStatus, Status.ttypes.TStatus.thrift_spec), None, ), # 1
    (2, TType.I64, 'num_rows_estimate', None, None, ), # 2
    (3, TType.LIST, 'accepted_conjuncts', (TType.I32,None), None, ), # 3
  )

  def __init__(self, status=None, num_rows_estimate=None, accepted_conjuncts=None,):
    self.status = status
    self.num_rows_estimate = num_rows_estimate
    self.accepted_conjuncts = accepted_conjuncts

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.status = Status.ttypes.TStatus()
          self.status.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.num_rows_estimate = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.accepted_conjuncts = []
          (_etype31, _size28) = iprot.readListBegin()
          for _i32 in xrange(_size28):
            _elem33 = iprot.readI32();
            self.accepted_conjuncts.append(_elem33)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TPrepareResult')
    if self.status is not None:
      oprot.writeFieldBegin('status', TType.STRUCT, 1)
      self.status.write(oprot)
      oprot.writeFieldEnd()
    if self.num_rows_estimate is not None:
      oprot.writeFieldBegin('num_rows_estimate', TType.I64, 2)
      oprot.writeI64(self.num_rows_estimate)
      oprot.writeFieldEnd()
    if self.accepted_conjuncts is not None:
      oprot.writeFieldBegin('accepted_conjuncts', TType.LIST, 3)
      oprot.writeListBegin(TType.I32, len(self.accepted_conjuncts))
      for iter34 in self.accepted_conjuncts:
        oprot.writeI32(iter34)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.status is None:
      raise TProtocol.TProtocolException(message='Required field status is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TOpenParams(object):
  """
  Attributes:
   - query_id
   - table_name
   - init_string
   - authenticated_user_name
   - row_schema
   - batch_size
   - predicates
   - limit
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'query_id', (Types.ttypes.TUniqueId, Types.ttypes.TUniqueId.thrift_spec), None, ), # 1
    (2, TType.STRING, 'table_name', None, None, ), # 2
    (3, TType.STRING, 'init_string', None, None, ), # 3
    (4, TType.STRING, 'authenticated_user_name', None, None, ), # 4
    (5, TType.STRUCT, 'row_schema', (TTableSchema, TTableSchema.thrift_spec), None, ), # 5
    (6, TType.I32, 'batch_size', None, None, ), # 6
    (7, TType.LIST, 'predicates', (TType.LIST,(TType.STRUCT,(TBinaryPredicate, TBinaryPredicate.thrift_spec))), None, ), # 7
    (8, TType.I64, 'limit', None, None, ), # 8
  )

  def __init__(self, query_id=None, table_name=None, init_string=None, authenticated_user_name=None, row_schema=None, batch_size=None, predicates=None, limit=None,):
    self.query_id = query_id
    self.table_name = table_name
    self.init_string = init_string
    self.authenticated_user_name = authenticated_user_name
    self.row_schema = row_schema
    self.batch_size = batch_size
    self.predicates = predicates
    self.limit = limit

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.query_id = Types.ttypes.TUniqueId()
          self.query_id.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.table_name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.init_string = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.authenticated_user_name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRUCT:
          self.row_schema = TTableSchema()
          self.row_schema.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I32:
          self.batch_size = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.LIST:
          self.predicates = []
          (_etype38, _size35) = iprot.readListBegin()
          for _i39 in xrange(_size35):
            _elem40 = []
            (_etype44, _size41) = iprot.readListBegin()
            for _i45 in xrange(_size41):
              _elem46 = TBinaryPredicate()
              _elem46.read(iprot)
              _elem40.append(_elem46)
            iprot.readListEnd()
            self.predicates.append(_elem40)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.I64:
          self.limit = iprot.readI64();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TOpenParams')
    if self.query_id is not None:
      oprot.writeFieldBegin('query_id', TType.STRUCT, 1)
      self.query_id.write(oprot)
      oprot.writeFieldEnd()
    if self.table_name is not None:
      oprot.writeFieldBegin('table_name', TType.STRING, 2)
      oprot.writeString(self.table_name)
      oprot.writeFieldEnd()
    if self.init_string is not None:
      oprot.writeFieldBegin('init_string', TType.STRING, 3)
      oprot.writeString(self.init_string)
      oprot.writeFieldEnd()
    if self.authenticated_user_name is not None:
      oprot.writeFieldBegin('authenticated_user_name', TType.STRING, 4)
      oprot.writeString(self.authenticated_user_name)
      oprot.writeFieldEnd()
    if self.row_schema is not None:
      oprot.writeFieldBegin('row_schema', TType.STRUCT, 5)
      self.row_schema.write(oprot)
      oprot.writeFieldEnd()
    if self.batch_size is not None:
      oprot.writeFieldBegin('batch_size', TType.I32, 6)
      oprot.writeI32(self.batch_size)
      oprot.writeFieldEnd()
    if self.predicates is not None:
      oprot.writeFieldBegin('predicates', TType.LIST, 7)
      oprot.writeListBegin(TType.LIST, len(self.predicates))
      for iter47 in self.predicates:
        oprot.writeListBegin(TType.STRUCT, len(iter47))
        for iter48 in iter47:
          iter48.write(oprot)
        oprot.writeListEnd()
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.limit is not None:
      oprot.writeFieldBegin('limit', TType.I64, 8)
      oprot.writeI64(self.limit)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TOpenResult(object):
  """
  Attributes:
   - status
   - scan_handle
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'status', (Status.ttypes.TStatus, Status.ttypes.TStatus.thrift_spec), None, ), # 1
    (2, TType.STRING, 'scan_handle', None, None, ), # 2
  )

  def __init__(self, status=None, scan_handle=None,):
    self.status = status
    self.scan_handle = scan_handle

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.status = Status.ttypes.TStatus()
          self.status.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.scan_handle = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TOpenResult')
    if self.status is not None:
      oprot.writeFieldBegin('status', TType.STRUCT, 1)
      self.status.write(oprot)
      oprot.writeFieldEnd()
    if self.scan_handle is not None:
      oprot.writeFieldBegin('scan_handle', TType.STRING, 2)
      oprot.writeString(self.scan_handle)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.status is None:
      raise TProtocol.TProtocolException(message='Required field status is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TGetNextParams(object):
  """
  Attributes:
   - scan_handle
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'scan_handle', None, None, ), # 1
  )

  def __init__(self, scan_handle=None,):
    self.scan_handle = scan_handle

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.scan_handle = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TGetNextParams')
    if self.scan_handle is not None:
      oprot.writeFieldBegin('scan_handle', TType.STRING, 1)
      oprot.writeString(self.scan_handle)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TGetNextResult(object):
  """
  Attributes:
   - status
   - eos
   - rows
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'status', (Status.ttypes.TStatus, Status.ttypes.TStatus.thrift_spec), None, ), # 1
    (2, TType.BOOL, 'eos', None, None, ), # 2
    (3, TType.STRUCT, 'rows', (TRowBatch, TRowBatch.thrift_spec), None, ), # 3
  )

  def __init__(self, status=None, eos=None, rows=None,):
    self.status = status
    self.eos = eos
    self.rows = rows

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.status = Status.ttypes.TStatus()
          self.status.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.BOOL:
          self.eos = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRUCT:
          self.rows = TRowBatch()
          self.rows.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TGetNextResult')
    if self.status is not None:
      oprot.writeFieldBegin('status', TType.STRUCT, 1)
      self.status.write(oprot)
      oprot.writeFieldEnd()
    if self.eos is not None:
      oprot.writeFieldBegin('eos', TType.BOOL, 2)
      oprot.writeBool(self.eos)
      oprot.writeFieldEnd()
    if self.rows is not None:
      oprot.writeFieldBegin('rows', TType.STRUCT, 3)
      self.rows.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.status is None:
      raise TProtocol.TProtocolException(message='Required field status is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TCloseParams(object):
  """
  Attributes:
   - scan_handle
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'scan_handle', None, None, ), # 1
  )

  def __init__(self, scan_handle=None,):
    self.scan_handle = scan_handle

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.scan_handle = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TCloseParams')
    if self.scan_handle is not None:
      oprot.writeFieldBegin('scan_handle', TType.STRING, 1)
      oprot.writeString(self.scan_handle)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TCloseResult(object):
  """
  Attributes:
   - status
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'status', (Status.ttypes.TStatus, Status.ttypes.TStatus.thrift_spec), None, ), # 1
  )

  def __init__(self, status=None,):
    self.status = status

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.status = Status.ttypes.TStatus()
          self.status.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TCloseResult')
    if self.status is not None:
      oprot.writeFieldBegin('status', TType.STRUCT, 1)
      self.status.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.status is None:
      raise TProtocol.TProtocolException(message='Required field status is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
