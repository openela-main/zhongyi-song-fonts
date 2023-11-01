%global fontname zhongyi-song
%global fontconf 65-0-%{fontname}.conf


Name:           zhongyi-song-fonts
Version:        0.1.20020329.1
Release:        18%{?dist}
Summary:        Zhong Yi Song -- GB18030 Standard Ming Face Chinese Font

License:        Commercial
URL:            http://www.china-e.com.cn/en/fonts/Font-Main.htm
Source0:        zysong.ttf.tar.bz2
Source1:        %{fontname}-fontconfig.conf
Source2:        zhongyi-license.txt

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
GB18030-2000 TrueType Chinese Character Song Font was appraised by China
authorized department and tested by National Center for Quality Supervision and
Inspection of Chinese Information Processing Products, which was designed and
manufactured by Beijing Zhong Yi Electronics Co. and up to China National
Standard.

%prep
%setup -q -c
install -m 0644 -p %{SOURCE2} .

%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}


%_font_pkg -f %{fontconf} *.ttf

%license zhongyi-license.txt

%changelog
* Mon Apr 18 2022 Peng Wu <pwu@redhat.com> - 0.1.20020329.1-18
- Rebuild the package
- Resolves: #2075544

* Fri Oct 12 2018 Peng Wu <pwu@redhat.com> - 0.1.20020329.1-17
- Drop ghostscript sub-package.

* Mon Mar  3 2014 Peng Wu <pwu@redhat.com> - 0.1.20020329.1-16.el7
- Resolves: rhbz#1067491
- Import this package for RHEL7.
- Re-write the spec for RHEL7.

* Wed May 19 2010  Peng Wu <pwu@redhat.com> - 0.1.20020329.1-15.el6
- Fixes a typo in change log.

* Wed May 19 2010  Peng Wu <pwu@redhat.com> - 0.1.20020329.1-14.el6
- Remove cjkuni-fonts-ghostscript requirement from zhongyi-song-fonts.

* Wed May 19 2010  Peng Wu <pwu@redhat.com> - 0.1.20020329.1-13.el6
- Split a separate ghostscript sub-packages,
  Resolves: rhbz#591217: zhongyi-song-fonts depends on package cjkuni-fonts-ghostscript.

* Wed Apr 28 2010  Peng Wu <pwu@redhat.com> - 0.1.20020329.1-12.el6
- Fixes rpm postun scriptlet.
- And drop basefontdir from files, as it belongs to fontpackages-filesystem.

* Thu Apr 15 2010  Peng Wu <pwu@redhat.com> - 0.1.20020329.1-11.el6
- Fixes rpm post and postun scriptlets, and fontconfig file attributes.

* Mon Apr 12 2010  Peng Wu <pwu@redhat.com> - 0.1.20020329.1-10.el6
- Fixes some typo.

* Mon Apr 12 2010  Peng Wu <pwu@redhat.com> - 0.1.20020329.1-9.el6
- Add fontconfig conf file based on l10n-font-template.conf template.

* Mon Apr 12 2010  Peng Wu <pwu@redhat.com> - 0.1.20020329.1-8.el6
- Merge zhongyi-song-fonts and -common sub-package into single packages.
- Remove chmod from scripts.

* Fri Mar 26 2010  Peng Wu <pwu@redhat.com> - 0.1-7.el6
- Fixes zhongyi song font install path, and fixes the font path in ghostscript conf.

* Tue Mar 16 2010  Peng Wu <pwu@redhat.com> - 0.1-6.el6
- Resolves: rhbz#538245 (RHEL6 Supplementary: [zh_CN] need GB18030 font for Chinese Gov certification)
  Rename the package from fonts-chinese-zysong to zhongyi-song-fonts for RHEL6.
  And make the zhongyi-song-fonts to adopt the Packaging:FontsPolicy.

* Tue Aug 14 2007 Caius CHANCE <cchance@redhat.com> - 0.1-5.el5
- Resolves: rhbz#247729 (zysong font needs to be removed from fonts-chinese.)
  ^^^ Moved zysong.ttf to new directory.

* Wed Aug  8 2007 Akira TAGOH <tagoh@redhat.com> - 0.1-4.el5
- Resolves: rhbz#247729 (zysong font needs to be removed from fonts-chinese.)
            rhbz#248505 (Review Request: fonts-chinese-zysong.)
- ^^^ Add %%triggerin and %%triggerpostun, also modify %%post and %%postun
  to update cidfmap.zh_CN and CIDFnmap.zh_CN.

* Wed Aug 08 2007 Caius Chance <cchance@redhat.com> - 0.1-3.el5
- Resolves: rhbz#247729 (zysong font needs to be removed from fonts-chinese.)
            rhbz#248505 (Review Request: fonts-chinese-zysong.)
- Migrated from devel to el5 branch.

* Fri Aug  3 2007 Jens Petersen <petersen@redhat.com> - 0.1-2.el5
- Resolves: rhbz#247577 (Add fonts-chinese-zysong package for zysong font from 
  fonts-chinese.)
- Resolves: rhbz#248505 (Review Request: fonts-chinese-zysong - Zhong Yi, Ming 
  Face GB18030 Chinese True Type Font.)

* Tue Jul 17 2007 Caius Chance <cchance@redhat.com> - 0.1-1.el5
- new package separated from fonts-chinese (#247577)
