# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/nostarch
# catalog-date 2008-08-22 17:15:44 +0200
# catalog-license lppl
# catalog-version 1.3
Name:		texlive-nostarch
Version:	1.3
Release:	1
Summary:	LaTeX class for No Starch Press
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nostarch
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nostarch.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nostarch.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nostarch.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides the "official" LaTeX style for No Starch
Press. Provided are a a class, a package for interfacing to
hyperref and an index style file. The style serves both for
printed and for electronic books.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex makeindex tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
