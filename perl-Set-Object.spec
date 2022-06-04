#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Set-Object
Version  : 1.42
Release  : 25
URL      : https://cpan.metacpan.org/authors/id/R/RU/RURBAN/Set-Object-1.42.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RU/RURBAN/Set-Object-1.42.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libs/libset-object-perl/libset-object-perl_1.39-1.debian.tar.xz
Summary  : 'Unordered collections (sets) of Perl Objects'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-2.0 GPL-1.0
Requires: perl-Set-Object-license = %{version}-%{release}
Requires: perl-Set-Object-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
~~~~~~~~~~~~~~~~~~~~~~
Set::Object provides efficient sets,
unordered collections of Perl objects without duplicates
for scalars and references.

%package dev
Summary: dev components for the perl-Set-Object package.
Group: Development
Provides: perl-Set-Object-devel = %{version}-%{release}
Requires: perl-Set-Object = %{version}-%{release}

%description dev
dev components for the perl-Set-Object package.


%package license
Summary: license components for the perl-Set-Object package.
Group: Default

%description license
license components for the perl-Set-Object package.


%package perl
Summary: perl components for the perl-Set-Object package.
Group: Default
Requires: perl-Set-Object = %{version}-%{release}

%description perl
perl components for the perl-Set-Object package.


%prep
%setup -q -n Set-Object-1.42
cd %{_builddir}
tar xf %{_sourcedir}/libset-object-perl_1.39-1.debian.tar.xz
cd %{_builddir}/Set-Object-1.42
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Set-Object-1.42/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Set-Object
cp %{_builddir}/Set-Object-1.42/LICENSE %{buildroot}/usr/share/package-licenses/perl-Set-Object/555574ecd72fc31417309a60e8c708af93ef4e8c
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Set-Object/5c32525a8d3005cf0cf7f887f11df2067213be92
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Set::Changes.3
/usr/share/man/man3/Set::Object.3
/usr/share/man/man3/Set::Object::Weak.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Set-Object/555574ecd72fc31417309a60e8c708af93ef4e8c
/usr/share/package-licenses/perl-Set-Object/5c32525a8d3005cf0cf7f887f11df2067213be92

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
