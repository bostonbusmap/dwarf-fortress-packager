#!/bin/bash
set -e

export PACKAGE=dwarf-fortress
export VERSION=0.34.11

rm -rf staging.deb
mkdir staging.deb

cp df_linux staging.deb -rf

cd staging.deb
tar zcvf ${PACKAGE}_${VERSION}.orig.tar.gz df_linux

cp ../debian df_linux -rf
cp ../dwarf-fortress df_linux

cd df_linux

dpkg-buildpackage -rfakeroot
