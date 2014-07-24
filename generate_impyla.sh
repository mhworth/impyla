#! /usr/bin/env bash

IMPYLA_REPO=`pwd`
OUTPUT=$IMPYLA_REPO/impala/thrift
ARGS="-gen py:new_style -out $OUTPUT"
ARGS="-gen py:new_style"

# generate the python code
thrift $ARGS $IMPYLA_REPO/thrift/Data.thrift
thrift $ARGS $IMPYLA_REPO/thrift/DataSinks.thrift
thrift $ARGS $IMPYLA_REPO/thrift/Descriptors.thrift
thrift $ARGS $IMPYLA_REPO/thrift/Exprs.thrift
thrift $ARGS $IMPYLA_REPO/thrift/Frontend.thrift
thrift $ARGS $IMPYLA_REPO/thrift/ImpalaInternalService.thrift
thrift $ARGS $IMPYLA_REPO/thrift/ImpalaService.thrift
thrift $ARGS $IMPYLA_REPO/thrift/NetworkTest.thrift
thrift $ARGS $IMPYLA_REPO/thrift/Partitions.thrift
thrift $ARGS $IMPYLA_REPO/thrift/PlanNodes.thrift
thrift $ARGS $IMPYLA_REPO/thrift/Planner.thrift
thrift $ARGS $IMPYLA_REPO/thrift/RuntimeProfile.thrift
thrift $ARGS $IMPYLA_REPO/thrift/StateStoreService.thrift
thrift $ARGS $IMPYLA_REPO/thrift/Status.thrift
thrift $ARGS $IMPYLA_REPO/thrift/Types.thrift
thrift $ARGS $IMPYLA_REPO/thrift/beeswax.thrift
thrift $ARGS $IMPYLA_REPO/thrift/cli_service.thrift
thrift $ARGS $IMPYLA_REPO/thrift/parquet.thrift
