%define name libsbml
%define version 3.0.0
%define rel	1
%define release %mkrel %{rel}

Summary:	Systems Biology Markup Language (SBML) library
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source:         http://prdownloads.sourceforge.net/sbml/%{name}-%{version}-prerelease-src.tar.bz2
Patch:		%{name}-%{version}-gcc4.patch
License:	LGPL
Group:		System/Libraries
Url:		http://sbml.org/libsbml.html
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	swig python
BuildRequires:  xerces-c-devel python-devel tetex-latex tetex-dvips
%description
The Systems Biology Markup Language (SBML) is a computer-readable format for 
representing models of biochemical reaction networks. SBML is applicable 
to metabolic networks, cell-signaling pathways, genomic regulatory networks,
and many other areas in systems biology.

LIBSBML is a C application programming interface (API) library for reading, 
writing and manipulating the SBML. Currently, the library supports all of 
SBML Level 1 Version 1 and Version 2, and nearly all of SBML Level 2 Version 1.
(The still-unimplemented parts of Level 2 are support for RDF and support
for MathML's semantics, annotation and annotation-xml elements. 
These will be implemented in the near future.)


%package -n %{name}-devel
Summary:        Header files for development with the Systems Biology Markup Language (SBML)
Group:          Development/C
Requires:       %{name} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{name}-devel
This package provides the necessary development libraries and includes
files to allow you to develop with the Systems Biology Markup Language (SBML)


%package -n %{name}-static-devel
Summary:        Static libraries for the Systems Biology Markup Language (SBML) library
Group:          Development/C
Requires:       %{name}-devel = %{version}-%{release}
Provides:	%{name}-static-devel = %{version}-%{release}

%description -n %{name}-static-devel
This package includes the static libraries necessary for developing programs 
which will use the Systems Biology Markup Language (SBML)


%package doc
Summary:        Documentation for libSBML
Group:          Development/C
Requires:       %{name} = %{version}-%{release}

%description doc
This package contains the developer's documentation



%prep

%setup -q

#%patch -p1

%build

#do not use percent/configure it messes up the compilation
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"
export CPPFLAGS="$RPM_OPT_FLAGS"
export FFLAGS="$RPM_OPT_FLAGS"
./configure i586-mandrake-linux-gnu --prefix=%_prefix --with-xerces --with-swig --with-python #--with-perl #--libdir=%_libdir

#-j1 necessary because of a race problem where the python binding
#would be compiled before libsbml.so
%make -j1

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -n %{name}
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/python%{pyver}/site-packages/*

%files -n %{name}-devel
%defattr(-,root,root)
%doc COPYING.txt
%{_includedir}/sbml/

%files -n %{name}-static-devel
%defattr(-,root,root)
%doc COPYING.txt
%{_libdir}/*.a

%files doc
%defattr(-,root,root)
%{_docdir}

