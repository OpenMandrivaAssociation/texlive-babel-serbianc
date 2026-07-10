%global tl_name babel-serbianc
%global tl_revision 64588

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.2a
Release:	%{tl_revision}.1
Summary:	Babel module to support Serbian Cyrillic
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/serbianc
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-serbianc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-serbianc.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-serbianc.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides support for Serbian documents written in Cyrillic,
in babel.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/generic
%dir %{_datadir}/texmf-dist/source/generic
%dir %{_datadir}/texmf-dist/tex/generic
%dir %{_datadir}/texmf-dist/doc/generic/babel-serbianc
%dir %{_datadir}/texmf-dist/source/generic/babel-serbianc
%dir %{_datadir}/texmf-dist/tex/generic/babel-serbianc
%doc %{_datadir}/texmf-dist/doc/generic/babel-serbianc/README.md
%doc %{_datadir}/texmf-dist/doc/generic/babel-serbianc/serbianc.pdf
%doc %{_datadir}/texmf-dist/source/generic/babel-serbianc/serbianc.dtx
%doc %{_datadir}/texmf-dist/source/generic/babel-serbianc/serbianc.ins
%{_datadir}/texmf-dist/tex/generic/babel-serbianc/serbianc.ldf
