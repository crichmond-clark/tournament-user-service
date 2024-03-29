# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user_service.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12user_service.proto\x12\x04user\"3\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08username\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\"t\n\x07Profile\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07user_id\x18\x02 \x01(\x05\x12\x12\n\nfirst_name\x18\x03 \x01(\t\x12\x11\n\tlast_name\x18\x04 \x01(\t\x12\x14\n\x0cphone_number\x18\x05 \x01(\t\x12\x0f\n\x07\x63ountrt\x18\x06 \x01(\t\"1\n\x12GetAllUsersRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\r\n\x05limit\x18\x02 \x01(\x05\"?\n\x13GetAllUsersResponse\x12\x19\n\x05users\x18\x01 \x03(\x0b\x32\n.user.User\x12\r\n\x05total\x18\x02 \x01(\x05\" \n\x12GetUserByIdRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"/\n\x13GetUserByIdResponse\x12\x18\n\x04user\x18\x01 \x01(\x0b\x32\n.user.User\"4\n\x11\x43reateUserRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\".\n\x12\x43reateUserResponse\x12\x18\n\x04user\x18\x01 \x01(\x0b\x32\n.user.User\"@\n\x11UpdateUserRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08username\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\".\n\x12UpdateUserResponse\x12\x18\n\x04user\x18\x01 \x01(\x0b\x32\n.user.User\"\x1f\n\x11\x44\x65leteUserRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"%\n\x12\x44\x65leteUserResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\xe2\x02\n\x0bUserService\x12\x44\n\x0bGetAllUsers\x12\x18.user.GetAllUsersRequest\x1a\x19.user.GetAllUsersResponse\"\x00\x12\x44\n\x0bGetUserById\x12\x18.user.GetUserByIdRequest\x1a\x19.user.GetUserByIdResponse\"\x00\x12\x41\n\nCreateUser\x12\x17.user.CreateUserRequest\x1a\x18.user.CreateUserResponse\"\x00\x12\x41\n\nUpdateUser\x12\x17.user.UpdateUserRequest\x1a\x18.user.UpdateUserResponse\"\x00\x12\x41\n\nDeleteUser\x12\x17.user.DeleteUserRequest\x1a\x18.user.DeleteUserResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_USER']._serialized_start=28
  _globals['_USER']._serialized_end=79
  _globals['_PROFILE']._serialized_start=81
  _globals['_PROFILE']._serialized_end=197
  _globals['_GETALLUSERSREQUEST']._serialized_start=199
  _globals['_GETALLUSERSREQUEST']._serialized_end=248
  _globals['_GETALLUSERSRESPONSE']._serialized_start=250
  _globals['_GETALLUSERSRESPONSE']._serialized_end=313
  _globals['_GETUSERBYIDREQUEST']._serialized_start=315
  _globals['_GETUSERBYIDREQUEST']._serialized_end=347
  _globals['_GETUSERBYIDRESPONSE']._serialized_start=349
  _globals['_GETUSERBYIDRESPONSE']._serialized_end=396
  _globals['_CREATEUSERREQUEST']._serialized_start=398
  _globals['_CREATEUSERREQUEST']._serialized_end=450
  _globals['_CREATEUSERRESPONSE']._serialized_start=452
  _globals['_CREATEUSERRESPONSE']._serialized_end=498
  _globals['_UPDATEUSERREQUEST']._serialized_start=500
  _globals['_UPDATEUSERREQUEST']._serialized_end=564
  _globals['_UPDATEUSERRESPONSE']._serialized_start=566
  _globals['_UPDATEUSERRESPONSE']._serialized_end=612
  _globals['_DELETEUSERREQUEST']._serialized_start=614
  _globals['_DELETEUSERREQUEST']._serialized_end=645
  _globals['_DELETEUSERRESPONSE']._serialized_start=647
  _globals['_DELETEUSERRESPONSE']._serialized_end=684
  _globals['_USERSERVICE']._serialized_start=687
  _globals['_USERSERVICE']._serialized_end=1041
# @@protoc_insertion_point(module_scope)
