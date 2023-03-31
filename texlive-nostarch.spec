Name:		texlive-nostarch
Version:	15878
Release:	2
Summary:	LaTeX class for No Starch Press
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nostarch
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nostarch.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nostarch.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nostarch.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the "official" LaTeX style for No Starch
Press. Provided are a a class, a package for interfacing to
hyperref and an index style file. The style serves both for
printed and for electronic books.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bib/nostarch/nostarch.bib
%{_texmfdistdir}/makeindex/nostarch/nostarch.ist
%{_texmfdistdir}/tex/latex/nostarch/nostarch.cls
%{_texmfdistdir}/tex/latex/nostarch/nshyper.sty
%doc %{_texmfdistdir}/doc/latex/nostarch/100euroie.png
%doc %{_texmfdistdir}/doc/latex/nostarch/100euroit.png
%doc %{_texmfdistdir}/doc/latex/nostarch/1eurogr.jpg
%doc %{_texmfdistdir}/doc/latex/nostarch/README
%doc %{_texmfdistdir}/doc/latex/nostarch/nostarch.pdf
%doc %{_texmfdistdir}/doc/latex/nostarch/nssample.pdf
%doc %{_texmfdistdir}/doc/latex/nostarch/nssample.tex
%doc %{_texmfdistdir}/doc/latex/nostarch/recycled.png
%doc %{_texmfdistdir}/doc/latex/nostarch/vitruvian.jpg
#- source
%doc %{_texmfdistdir}/source/latex/nostarch/Makefile
%doc %{_texmfdistdir}/source/latex/nostarch/nostarch.dtx
%doc %{_texmfdistdir}/source/latex/nostarch/nostarch.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex makeindex tex doc source %{buildroot}%{_texmfdistdir}
