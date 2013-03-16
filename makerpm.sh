#!/bin/bash
set -e

export PACKAGE=dwarf-fortress
export VERSION=0.34.11

rm -rf staging.rpm
mkdir -p staging.rpm/buildroot/SOURCES

cp df_linux staging.rpm -rf
cp dwarf-fortress staging.rpm/df_linux
cp *.desktop staging.rpm/df_linux

cd staging.rpm
mv df_linux dwarf-fortress
tar zcvf ${PACKAGE}.tar.gz dwarf-fortress
mv ${PACKAGE}.tar.gz buildroot/SOURCES

cp ../dwarf-fortress.spec .

rpmbuild --define "_topdir $(pwd)/buildroot" -ba dwarf-fortress.spec

cp $(find buildroot/RPMS -type f) .
