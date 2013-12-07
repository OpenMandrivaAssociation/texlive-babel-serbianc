# revision 30348
# category Package
# catalog-ctan /macros/latex/contrib/babel-contrib/serbianc
# catalog-date 2013-05-04 16:25:22 +0200
# catalog-license lppl1.3
# catalog-version 2.2
Name:		texlive-babel-serbianc
Version:	2.2
Release:	2
Summary:	Babel module to support Serbian Cyrillic
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/serbianc
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-serbianc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-serbianc.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-serbianc.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides support for Serbian documents written in
Cyrillic, in babel.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/babel-serbianc/serbianc.ldf
%{_texmfdistdir}/tex/generic/babel-serbianc/serbianc.sty
%doc %{_texmfdistdir}/doc/generic/babel-serbianc/COPYING
%doc %{_texmfdistdir}/doc/generic/babel-serbianc/ChangeLog
%doc %{_texmfdistdir}/doc/generic/babel-serbianc/Copyright
%doc %{_texmfdistdir}/doc/generic/babel-serbianc/INSTALL
%doc %{_texmfdistdir}/doc/generic/babel-serbianc/README
%doc %{_texmfdistdir}/doc/generic/babel-serbianc/README.Files
%doc %{_texmfdistdir}/doc/generic/babel-serbianc/README.serbianc
%doc %{_texmfdistdir}/doc/generic/babel-serbianc/sample.pdf
%doc %{_texmfdistdir}/doc/generic/babel-serbianc/sample.tex
%doc %{_texmfdistdir}/doc/generic/babel-serbianc/serbianc.patch
#- source
%doc %{_texmfdistdir}/source/generic/babel-serbianc/serbianc.dtx
%doc %{_texmfdistdir}/source/generic/babel-serbianc/serbianc.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
