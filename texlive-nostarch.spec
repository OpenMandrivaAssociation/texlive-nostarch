%global tl_name nostarch
%global tl_revision 67683

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.4
Release:	%{tl_revision}.1
Summary:	LaTeX class for No Starch Press
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/nostarch
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nostarch.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nostarch.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nostarch.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the "official" LaTeX style for No Starch Press.
Provided are a class, a package for interfacing to hyperref and an index
style file. The style serves both for printed and for electronic books.

