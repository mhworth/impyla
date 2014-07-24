#
# Autogenerated by Thrift Compiler (0.9.1)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import Types.ttypes
import CatalogObjects.ttypes


from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class TRowBatch(object):
  """
  Attributes:
   - num_rows
   - row_tuples
   - tuple_offsets
   - tuple_data
   - compression_type
   - uncompressed_size
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'num_rows', None, None, ), # 1
    (2, TType.LIST, 'row_tuples', (TType.I32,None), None, ), # 2
    (3, TType.LIST, 'tuple_offsets', (TType.I32,None), None, ), # 3
    (4, TType.STRING, 'tuple_data', None, None, ), # 4
    (5, TType.I32, 'compression_type', None, None, ), # 5
    (6, TType.I32, 'uncompressed_size', None, None, ), # 6
  )

  def __init__(self, num_rows=None, row_tuples=None, tuple_offsets=None, tuple_data=None, compression_type=None, uncompressed_size=None,):
    self.num_rows = num_rows
    self.row_tuples = row_tuples
    self.tuple_offsets = tuple_offsets
    self.tuple_data = tuple_data
    self.compression_type = compression_type
    self.uncompressed_size = uncompressed_size

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
        if ftype == TType.I32:
          self.num_rows = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.row_tuples = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = iprot.readI32();
            self.row_tuples.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.tuple_offsets = []
          (_etype9, _size6) = iprot.readListBegin()
          for _i10 in xrange(_size6):
            _elem11 = iprot.readI32();
            self.tuple_offsets.append(_elem11)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.tuple_data = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I32:
          self.compression_type = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I32:
          self.uncompressed_size = iprot.readI32();
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
    if self.num_rows is not None:
      oprot.writeFieldBegin('num_rows', TType.I32, 1)
      oprot.writeI32(self.num_rows)
      oprot.writeFieldEnd()
    if self.row_tuples is not None:
      oprot.writeFieldBegin('row_tuples', TType.LIST, 2)
      oprot.writeListBegin(TType.I32, len(self.row_tuples))
      for iter12 in self.row_tuples:
        oprot.writeI32(iter12)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.tuple_offsets is not None:
      oprot.writeFieldBegin('tuple_offsets', TType.LIST, 3)
      oprot.writeListBegin(TType.I32, len(self.tuple_offsets))
      for iter13 in self.tuple_offsets:
        oprot.writeI32(iter13)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.tuple_data is not None:
      oprot.writeFieldBegin('tuple_data', TType.STRING, 4)
      oprot.writeString(self.tuple_data)
      oprot.writeFieldEnd()
    if self.compression_type is not None:
      oprot.writeFieldBegin('compression_type', TType.I32, 5)
      oprot.writeI32(self.compression_type)
      oprot.writeFieldEnd()
    if self.uncompressed_size is not None:
      oprot.writeFieldBegin('uncompressed_size', TType.I32, 6)
      oprot.writeI32(self.uncompressed_size)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.num_rows is None:
      raise TProtocol.TProtocolException(message='Required field num_rows is unset!')
    if self.row_tuples is None:
      raise TProtocol.TProtocolException(message='Required field row_tuples is unset!')
    if self.compression_type is None:
      raise TProtocol.TProtocolException(message='Required field compression_type is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TColumnValue(object):
  """
  Attributes:
   - bool_val
   - byte_val
   - short_val
   - int_val
   - long_val
   - double_val
   - string_val
   - binary_val
  """

  thrift_spec = (
    None, # 0
    (1, TType.BOOL, 'bool_val', None, None, ), # 1
    (2, TType.I32, 'int_val', None, None, ), # 2
    (3, TType.I64, 'long_val', None, None, ), # 3
    (4, TType.DOUBLE, 'double_val', None, None, ), # 4
    (5, TType.STRING, 'string_val', None, None, ), # 5
    (6, TType.BYTE, 'byte_val', None, None, ), # 6
    (7, TType.I16, 'short_val', None, None, ), # 7
    (8, TType.STRING, 'binary_val', None, None, ), # 8
  )

  def __init__(self, bool_val=None, byte_val=None, short_val=None, int_val=None, long_val=None, double_val=None, string_val=None, binary_val=None,):
    self.bool_val = bool_val
    self.byte_val = byte_val
    self.short_val = short_val
    self.int_val = int_val
    self.long_val = long_val
    self.double_val = double_val
    self.string_val = string_val
    self.binary_val = binary_val

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
        if ftype == TType.BOOL:
          self.bool_val = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.BYTE:
          self.byte_val = iprot.readByte();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I16:
          self.short_val = iprot.readI16();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.int_val = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.long_val = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.DOUBLE:
          self.double_val = iprot.readDouble();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.string_val = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.STRING:
          self.binary_val = iprot.readString();
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
    oprot.writeStructBegin('TColumnValue')
    if self.bool_val is not None:
      oprot.writeFieldBegin('bool_val', TType.BOOL, 1)
      oprot.writeBool(self.bool_val)
      oprot.writeFieldEnd()
    if self.int_val is not None:
      oprot.writeFieldBegin('int_val', TType.I32, 2)
      oprot.writeI32(self.int_val)
      oprot.writeFieldEnd()
    if self.long_val is not None:
      oprot.writeFieldBegin('long_val', TType.I64, 3)
      oprot.writeI64(self.long_val)
      oprot.writeFieldEnd()
    if self.double_val is not None:
      oprot.writeFieldBegin('double_val', TType.DOUBLE, 4)
      oprot.writeDouble(self.double_val)
      oprot.writeFieldEnd()
    if self.string_val is not None:
      oprot.writeFieldBegin('string_val', TType.STRING, 5)
      oprot.writeString(self.string_val)
      oprot.writeFieldEnd()
    if self.byte_val is not None:
      oprot.writeFieldBegin('byte_val', TType.BYTE, 6)
      oprot.writeByte(self.byte_val)
      oprot.writeFieldEnd()
    if self.short_val is not None:
      oprot.writeFieldBegin('short_val', TType.I16, 7)
      oprot.writeI16(self.short_val)
      oprot.writeFieldEnd()
    if self.binary_val is not None:
      oprot.writeFieldBegin('binary_val', TType.STRING, 8)
      oprot.writeString(self.binary_val)
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

class TResultRow(object):
  """
  Attributes:
   - colVals
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'colVals', (TType.STRUCT,(TColumnValue, TColumnValue.thrift_spec)), None, ), # 1
  )

  def __init__(self, colVals=None,):
    self.colVals = colVals

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
          self.colVals = []
          (_etype17, _size14) = iprot.readListBegin()
          for _i18 in xrange(_size14):
            _elem19 = TColumnValue()
            _elem19.read(iprot)
            self.colVals.append(_elem19)
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
    oprot.writeStructBegin('TResultRow')
    if self.colVals is not None:
      oprot.writeFieldBegin('colVals', TType.LIST, 1)
      oprot.writeListBegin(TType.STRUCT, len(self.colVals))
      for iter20 in self.colVals:
        iter20.write(oprot)
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

class TColumnData(object):
  """
  Attributes:
   - is_null
   - bool_vals
   - byte_vals
   - short_vals
   - int_vals
   - long_vals
   - double_vals
   - string_vals
   - binary_vals
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'is_null', (TType.BOOL,None), None, ), # 1
    (2, TType.LIST, 'bool_vals', (TType.BOOL,None), None, ), # 2
    (3, TType.LIST, 'byte_vals', (TType.BYTE,None), None, ), # 3
    (4, TType.LIST, 'short_vals', (TType.I16,None), None, ), # 4
    (5, TType.LIST, 'int_vals', (TType.I32,None), None, ), # 5
    (6, TType.LIST, 'long_vals', (TType.I64,None), None, ), # 6
    (7, TType.LIST, 'double_vals', (TType.DOUBLE,None), None, ), # 7
    (8, TType.LIST, 'string_vals', (TType.STRING,None), None, ), # 8
    (9, TType.LIST, 'binary_vals', (TType.STRING,None), None, ), # 9
  )

  def __init__(self, is_null=None, bool_vals=None, byte_vals=None, short_vals=None, int_vals=None, long_vals=None, double_vals=None, string_vals=None, binary_vals=None,):
    self.is_null = is_null
    self.bool_vals = bool_vals
    self.byte_vals = byte_vals
    self.short_vals = short_vals
    self.int_vals = int_vals
    self.long_vals = long_vals
    self.double_vals = double_vals
    self.string_vals = string_vals
    self.binary_vals = binary_vals

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
          self.is_null = []
          (_etype24, _size21) = iprot.readListBegin()
          for _i25 in xrange(_size21):
            _elem26 = iprot.readBool();
            self.is_null.append(_elem26)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.bool_vals = []
          (_etype30, _size27) = iprot.readListBegin()
          for _i31 in xrange(_size27):
            _elem32 = iprot.readBool();
            self.bool_vals.append(_elem32)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.byte_vals = []
          (_etype36, _size33) = iprot.readListBegin()
          for _i37 in xrange(_size33):
            _elem38 = iprot.readByte();
            self.byte_vals.append(_elem38)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.LIST:
          self.short_vals = []
          (_etype42, _size39) = iprot.readListBegin()
          for _i43 in xrange(_size39):
            _elem44 = iprot.readI16();
            self.short_vals.append(_elem44)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.LIST:
          self.int_vals = []
          (_etype48, _size45) = iprot.readListBegin()
          for _i49 in xrange(_size45):
            _elem50 = iprot.readI32();
            self.int_vals.append(_elem50)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.LIST:
          self.long_vals = []
          (_etype54, _size51) = iprot.readListBegin()
          for _i55 in xrange(_size51):
            _elem56 = iprot.readI64();
            self.long_vals.append(_elem56)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.LIST:
          self.double_vals = []
          (_etype60, _size57) = iprot.readListBegin()
          for _i61 in xrange(_size57):
            _elem62 = iprot.readDouble();
            self.double_vals.append(_elem62)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.LIST:
          self.string_vals = []
          (_etype66, _size63) = iprot.readListBegin()
          for _i67 in xrange(_size63):
            _elem68 = iprot.readString();
            self.string_vals.append(_elem68)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.LIST:
          self.binary_vals = []
          (_etype72, _size69) = iprot.readListBegin()
          for _i73 in xrange(_size69):
            _elem74 = iprot.readString();
            self.binary_vals.append(_elem74)
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
    oprot.writeStructBegin('TColumnData')
    if self.is_null is not None:
      oprot.writeFieldBegin('is_null', TType.LIST, 1)
      oprot.writeListBegin(TType.BOOL, len(self.is_null))
      for iter75 in self.is_null:
        oprot.writeBool(iter75)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.bool_vals is not None:
      oprot.writeFieldBegin('bool_vals', TType.LIST, 2)
      oprot.writeListBegin(TType.BOOL, len(self.bool_vals))
      for iter76 in self.bool_vals:
        oprot.writeBool(iter76)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.byte_vals is not None:
      oprot.writeFieldBegin('byte_vals', TType.LIST, 3)
      oprot.writeListBegin(TType.BYTE, len(self.byte_vals))
      for iter77 in self.byte_vals:
        oprot.writeByte(iter77)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.short_vals is not None:
      oprot.writeFieldBegin('short_vals', TType.LIST, 4)
      oprot.writeListBegin(TType.I16, len(self.short_vals))
      for iter78 in self.short_vals:
        oprot.writeI16(iter78)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.int_vals is not None:
      oprot.writeFieldBegin('int_vals', TType.LIST, 5)
      oprot.writeListBegin(TType.I32, len(self.int_vals))
      for iter79 in self.int_vals:
        oprot.writeI32(iter79)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.long_vals is not None:
      oprot.writeFieldBegin('long_vals', TType.LIST, 6)
      oprot.writeListBegin(TType.I64, len(self.long_vals))
      for iter80 in self.long_vals:
        oprot.writeI64(iter80)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.double_vals is not None:
      oprot.writeFieldBegin('double_vals', TType.LIST, 7)
      oprot.writeListBegin(TType.DOUBLE, len(self.double_vals))
      for iter81 in self.double_vals:
        oprot.writeDouble(iter81)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.string_vals is not None:
      oprot.writeFieldBegin('string_vals', TType.LIST, 8)
      oprot.writeListBegin(TType.STRING, len(self.string_vals))
      for iter82 in self.string_vals:
        oprot.writeString(iter82)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.binary_vals is not None:
      oprot.writeFieldBegin('binary_vals', TType.LIST, 9)
      oprot.writeListBegin(TType.STRING, len(self.binary_vals))
      for iter83 in self.binary_vals:
        oprot.writeString(iter83)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.is_null is None:
      raise TProtocol.TProtocolException(message='Required field is_null is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TResultSetMetadata(object):
  """
  Attributes:
   - columns
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'columns', (TType.STRUCT,(CatalogObjects.ttypes.TColumn, CatalogObjects.ttypes.TColumn.thrift_spec)), None, ), # 1
  )

  def __init__(self, columns=None,):
    self.columns = columns

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
          self.columns = []
          (_etype87, _size84) = iprot.readListBegin()
          for _i88 in xrange(_size84):
            _elem89 = CatalogObjects.ttypes.TColumn()
            _elem89.read(iprot)
            self.columns.append(_elem89)
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
    oprot.writeStructBegin('TResultSetMetadata')
    if self.columns is not None:
      oprot.writeFieldBegin('columns', TType.LIST, 1)
      oprot.writeListBegin(TType.STRUCT, len(self.columns))
      for iter90 in self.columns:
        iter90.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.columns is None:
      raise TProtocol.TProtocolException(message='Required field columns is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TResultSet(object):
  """
  Attributes:
   - rows
   - schema
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'rows', (TType.STRUCT,(TResultRow, TResultRow.thrift_spec)), None, ), # 1
    (2, TType.STRUCT, 'schema', (TResultSetMetadata, TResultSetMetadata.thrift_spec), None, ), # 2
  )

  def __init__(self, rows=None, schema=None,):
    self.rows = rows
    self.schema = schema

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
          self.rows = []
          (_etype94, _size91) = iprot.readListBegin()
          for _i95 in xrange(_size91):
            _elem96 = TResultRow()
            _elem96.read(iprot)
            self.rows.append(_elem96)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.schema = TResultSetMetadata()
          self.schema.read(iprot)
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
    oprot.writeStructBegin('TResultSet')
    if self.rows is not None:
      oprot.writeFieldBegin('rows', TType.LIST, 1)
      oprot.writeListBegin(TType.STRUCT, len(self.rows))
      for iter97 in self.rows:
        iter97.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.schema is not None:
      oprot.writeFieldBegin('schema', TType.STRUCT, 2)
      self.schema.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.rows is None:
      raise TProtocol.TProtocolException(message='Required field rows is unset!')
    if self.schema is None:
      raise TProtocol.TProtocolException(message='Required field schema is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
