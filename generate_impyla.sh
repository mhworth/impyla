#! /usr/bin/env bash

IMPYLA_REPO=`pwd`
OUTPUT=$IMPYLA_REPO/impala/thrift

# generate the python code
thrift -gen py:new_style -out $OUTPUT $IMPYLA_REPO/thrift/Data.thrift
thrift -gen py:new_style -out $OUTPUT $IMPYLA_REPO/thrift/DataSinks.thrift
thrift -gen py:new_style -out $OUTPUT $IMPYLA_REPO/thrift/Descriptors.thrift
thrift -gen py:new_style -out $OUTPUT $IMPYLA_REPO/thrift/Exprs.thrift
thrift -gen py:new_style -out $OUTPUT $IMPYLA_REPO/thrift/Frontend.thrift
thrift -gen py:new_style -out $OUTPUT $IMPYLA_REPO/thrift/ImpalaInternalService.thrift
thrift -gen py:new_style -out $OUTPUT $IMPYLA_REPO/thrift/ImpalaService.thrift
thrift -gen py:new_style -out $OUTPUT $IMPYLA_REPO/thrift/NetworkTest.thrift
thrift -gen py:new_style -out $OUTPUT $IMPYLA_REPO/thrift/Partitions.thrift
thrift -gen py:new_style -out $OUTPUT $IMPYLA_REPO/thrift/PlanNodes.thrift
thrift -gen py:new_style -out $OUTPUT $IMPYLA_REPO/thrift/Planner.thrift
thrift -gen py:new_style -out $OUTPUT $IMPYLA_REPO/thrift/RuntimeProfile.thrift
thrift -gen py:new_style -out $OUTPUT $IMPYLA_REPO/thrift/StateStoreService.thrift
thrift -gen py:new_style -out $OUTPUT $IMPYLA_REPO/thrift/Status.thrift
thrift -gen py:new_style -out $OUTPUT $IMPYLA_REPO/thrift/Types.thrift
thrift -gen py:new_style -out $OUTPUT $IMPYLA_REPO/thrift/beeswax.thrift
thrift -gen py:new_style -out $OUTPUT $IMPYLA_REPO/thrift/cli_service.thrift
thrift -gen py:new_style -out $OUTPUT $IMPYLA_REPO/thrift/parquet.thrift
