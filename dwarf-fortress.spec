Name:           dwarf-fortress
Version:        0.34.11
Release:        1
Summary:        Dwarf Fortress
Group:          Games
License:        Proprietary
URL:            http://www.bay12games.com/dwarves/
Source0:        http://fakeurl/dwarf-fortress.tar.gz

%description
Dwarf Fortress

%prep
%setup -qn %{name}

%files
%{_bindir}/dwarf-fortress

/usr/share/dwarf-fortress

/usr/share/applications

%install
mkdir -p %{buildroot}%{_bindir}
install -m0755 dwarf-fortress %{buildroot}%{_bindir}

export DIR=%{buildroot}/usr/share/dwarf-fortress

mkdir -p $DIR
cp -r command?line.txt $DIR
cp -r data $DIR
cp -r df $DIR
cp -r file?changes.txt $DIR
cp -r gamelog.txt $DIR
cp -r g_src $DIR
cp -r libs $DIR
cp -r raw $DIR
cp -r README.linux $DIR
cp -r readme.txt $DIR
cp -r release?notes.txt $DIR
cp -r sdl $DIR

mkdir -p %{buildroot}/usr/share/applications
cp *.desktop %{buildroot}/usr/share/applications
