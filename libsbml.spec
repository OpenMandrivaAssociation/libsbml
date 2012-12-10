Summary:	Systems Biology Markup Language (SBML) library
Name:		libsbml
Version:	3.4.1
Release:	3
Source:         http://prdownloads.sourceforge.net/sbml/%{name}-%{version}-src.tar.bz2
License:	LGPL
Group:		System/Libraries
Url:		http://sbml.org/libsbml.html
Requires:	swig python
BuildRequires:  swig xerces-c-devel python-devel tetex-latex tetex-dvips zlib-devel bzip2-devel

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

%build

%configure --with-xerces --with-swig --with-python
%make -j1

%install
%makeinstall_std

%files -n %{name}
%defattr(-,root,root)
%{_libdir}/*.so
%doc COPYING.txt
%py_platsitedir/*

%files -n %{name}-devel
%defattr(-,root,root)
%{_includedir}/sbml/

%files -n %{name}-static-devel
%defattr(-,root,root)
%{_libdir}/*.a
%{_libdir}/pkgconfig/libsbml.pc

#%files doc
#%defattr(-,root,root)
#%{_docdir}



%changelog
* Mon Mar 15 2010 Eric Fernandez <zeb@mandriva.org> 3.4.1-2mdv2010.1
+ Revision: 519943
- rebuild

* Mon Aug 17 2009 Eric Fernandez <zeb@mandriva.org> 3.4.1-1mdv2010.0
+ Revision: 417176
- new version 3.4.1

* Wed May 06 2009 Eric Fernandez <zeb@mandriva.org> 3.3.2-2mdv2010.0
+ Revision: 372403
- rebuild

* Fri Apr 03 2009 Eric Fernandez <zeb@mandriva.org> 3.3.2-1mdv2009.1
+ Revision: 363690
- fix build requires
- new version 3.3.2
- new version 3.3.2

* Sun Dec 28 2008 Funda Wang <fwang@mandriva.org> 3.2.0-2mdv2009.1
+ Revision: 320164
- rebuild for new python

* Mon Oct 13 2008 Eric Fernandez <zeb@mandriva.org> 3.2.0-1mdv2009.1
+ Revision: 293296
- correct build-requires
- add zlib in build requires for x86_64
- cleanup
- version 3.2.0

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Aug 04 2007 Funda Wang <fwang@mandriva.org> 3.0.0-1mdv2008.0
+ Revision: 58831
- Add patch to fix python binding installation
- fix building
- Remove unused patch
- New version


* Fri Aug 18 2006 Eric Fernandez <zeb@zebulon.org.uk> 2.3.4-2mdv2007.0
- rebuild using mkrel
- patch for gcc-4
- spec file cleanup

* Fri Nov 04 2005 Eric Fernandez <zeb@zebulon.org.uk> 2.3.4-1mdk
- New version 2.3.4

* Tue Jun 07 2005 Eric Fernandez <zeb@zebulon.org.uk> 2.3.2-1mdk
- New version 2.3.2
- Removed install and doc hacks (thanks to correct Makefiles)
- Clean up Buildrequires (lib devel requirements)

* Sun Jan 02 2005 Eric Fernandez <zeb@zebulon.org.uk> 2.2.0-3mdk
- Rebuild

* Mon Dec 13 2004 Eric Fernandez <zeb@zebulon.org.uk> 2.2.0-2mdk
- Rebuild for new libxerces-c26, replaces libxerces-c25

* Thu Dec 09 2004 Eric Fernandez <zeb@zebulon.org.uk> 2.2.0-1mdk
- New version 2.2.0
- removed fix for python modules, now correctly handled by the Makefile
- split doc
- added url for source ( Michael Scherer )

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 2.1.0-5mdk
- Rebuild for new python

* Thu Oct 21 2004 Michael Scherer <misc@mandrake.org> 2.1.0-4mdk 
- BuildRequires

* Thu Oct 14 2004 Michael Scherer <misc@mandrake.org> 2.1.0-3mdk
- BuildRequires

* Fri Oct 01 2004 Michael Scherer <misc@mandrake.org> 2.1.0-2mdk 
- BuildRequires

* Sun Sep 19 2004 Michael Scherer <misc@mandrake.org> 2.1.0-1mdk 
- some fix
- from Eric Fernandez <zeb@zebulon.org.uk> 
  - First mdk release

