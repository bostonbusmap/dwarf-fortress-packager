Name:           dwarf-fortress
Version:        0.34.11
Release:        1
Summary:        Dwarf Fortress
Group:          Games
License:        Freely redistributable without restriction
URL:            http://www.tkl.iis.u-tokyo.ac.jp/~toyoda/index_e.html
Source0:        http://fakeurl/dwarf-fortress.tar.gz

%description
Dwarf Fortress

%prep
%setup -qn %{name}

%files
%{_bindir}/dwarf-fortress

%install
mkdir -p %{buildroot}%{_bindir}
install -m0755 dwarf-fortress %{buildroot}%{_bindir}
