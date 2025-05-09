#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-PerlIO-eol
Version  : 0.19
Release  : 31
URL      : https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/PerlIO-eol-0.19.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/PerlIO-eol-0.19.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libperlio-eol-perl/libperlio-eol-perl_0.17-1.debian.tar.xz
Summary  : 'PerlIO layer for normalizing line endings'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-PerlIO-eol-license = %{version}-%{release}
Requires: perl-PerlIO-eol-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
normalizing line endings.  It requires Perl version 5.7.3 or later.
* Installation

%package dev
Summary: dev components for the perl-PerlIO-eol package.
Group: Development
Provides: perl-PerlIO-eol-devel = %{version}-%{release}
Requires: perl-PerlIO-eol = %{version}-%{release}

%description dev
dev components for the perl-PerlIO-eol package.


%package license
Summary: license components for the perl-PerlIO-eol package.
Group: Default

%description license
license components for the perl-PerlIO-eol package.


%package perl
Summary: perl components for the perl-PerlIO-eol package.
Group: Default
Requires: perl-PerlIO-eol = %{version}-%{release}

%description perl
perl components for the perl-PerlIO-eol package.


%prep
%setup -q -n PerlIO-eol-0.19
cd %{_builddir}
tar xf %{_sourcedir}/libperlio-eol-perl_0.17-1.debian.tar.xz
cd %{_builddir}/PerlIO-eol-0.19
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/PerlIO-eol-0.19/deblicense/
pushd ..
cp -a PerlIO-eol-0.19 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
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
mkdir -p %{buildroot}/usr/share/package-licenses/perl-PerlIO-eol
cp %{_builddir}/PerlIO-eol-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-PerlIO-eol/3c3208f5914b492d230c6ff1513ae3384889b94a || :
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-PerlIO-eol/4ed81cda73b4be0e220be7d5fb11baf974e9cf8c || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/PerlIO::eol.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-PerlIO-eol/3c3208f5914b492d230c6ff1513ae3384889b94a
/usr/share/package-licenses/perl-PerlIO-eol/4ed81cda73b4be0e220be7d5fb11baf974e9cf8c

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
