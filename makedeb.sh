#!/bin/bash
set -e

export PACKAGE=dwarf-fortress
export VERSION=0.34.11

rm -rf staging.deb
mkdir staging.deb

cp df_linux staging.deb -rf
cp dwarf-fortress staging.deb/df_linux
cp *.desktop staging.deb/df_linux

cd staging.deb
tar zcvf ${PACKAGE}_${VERSION}.orig.tar.gz df_linux

cp ../debian df_linux -rf

cd df_linux

dpkg-buildpackage -rfakeroot
