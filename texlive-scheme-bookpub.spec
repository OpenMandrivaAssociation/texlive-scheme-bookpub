%global tl_name scheme-bookpub
%global tl_revision 63547

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	book publishing scheme (core LaTeX and add-ons)
Group:		Publishing
URL:		https://www.ctan.org/pkg/scheme-bookpub
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/scheme-bookpub.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(barcodes)
Requires:	texlive(biber)
Requires:	texlive(biblatex)
Requires:	texlive(bookcover)
Requires:	texlive(caption)
Requires:	texlive(collection-basic)
Requires:	texlive(collection-latex)
Requires:	texlive(enumitem)
Requires:	texlive(fontspec)
Requires:	texlive(latexmk)
Requires:	texlive(lipsum)
Requires:	texlive(listings)
Requires:	texlive(markdown)
Requires:	texlive(memoir)
Requires:	texlive(microtype)
Requires:	texlive(minted)
Requires:	texlive(novel)
Requires:	texlive(octavo)
Requires:	texlive(pdfpages)
Requires:	texlive(pgf)
Requires:	texlive(qrcode)
Requires:	texlive(shapes)
Requires:	texlive(titlesec)
Requires:	texlive(tocloft)
Requires:	texlive(tufte-latex)
Requires:	texlive(willowtreebook)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a book publishing scheme, containing core (Lua)LaTeX and
selected additional packages likely to be useful for non-technical book
publication. It does not contain additional fonts (different books need
different fonts, and the packages are large), nor does it contain
additional mathematical or other technical packages.

