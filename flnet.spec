#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : flnet
Version  : 7.3.2
Release  : 4
URL      : https://sourceforge.net/projects/fldigi/files/flnet/flnet-7.3.2.tar.gz
Source0  : https://sourceforge.net/projects/fldigi/files/flnet/flnet-7.3.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: flnet-bin = %{version}-%{release}
Requires: flnet-data = %{version}-%{release}
Requires: flnet-license = %{version}-%{release}
BuildRequires : fltk-dev
BuildRequires : fontconfig-dev
BuildRequires : libXcursor-dev
BuildRequires : libXft-dev
BuildRequires : libXinerama-dev
BuildRequires : libXrender-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libpng-dev
BuildRequires : pkgconfig(xext)

%description
Flnet provides the Amateur Radio Net Control Station operator with a real
time tool to assist him or her in managing the net activities.  A single
screen with multiple windows is used to allow rapid entry, search, pick
and display of all stations calling in to the net.  All operations on
the main screen are accomplished with keyboard entries only.  No mouse
action is required to perform the net control functions.  Experience
has shown that most net control operators prefer this method of operation
to improve the speed of entry and selection

%package bin
Summary: bin components for the flnet package.
Group: Binaries
Requires: flnet-data = %{version}-%{release}
Requires: flnet-license = %{version}-%{release}

%description bin
bin components for the flnet package.


%package data
Summary: data components for the flnet package.
Group: Data

%description data
data components for the flnet package.


%package license
Summary: license components for the flnet package.
Group: Default

%description license
license components for the flnet package.


%prep
%setup -q -n flnet-7.3.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545266213
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1545266213
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/flnet
cp COPYING %{buildroot}/usr/share/package-licenses/flnet/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/flnet

%files data
%defattr(-,root,root,-)
/usr/share/applications/flnet.desktop
/usr/share/pixmaps/flnet.xpm

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/flnet/COPYING
