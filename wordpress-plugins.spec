Summary:	Plugins for the WordPress personal publishing system
Summary(pl):	Wtyczki dla osobistego systemu publikacji WordPress
Name:		wordpress-plugins
Version:	1.5
Release:	2
License:	GPL
Group:		Applications/Publishing
Source0:	http://ink.bur.st/wp-content/downloads/kca.phps
# Source0-md5:	a6aecdf5eeee244f1537825921773625
Source1:	http://pericat.ca/downloads/previewexcerpt.tar.gz
# Source1-md5:	41e6c2f87dec2225ac33a4eef74fab39
URL:		http://codex.wordpress.org/Plugins
BuildRequires:	dos2unix
Requires:	wordpress = %{version}
Provides:	wordpress-plugin-khanhs_content_adder
Provides:	wordpress-plugin-previewexcerpt
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		wordpressdir	/home/services/httpd/html/wordpress
%define		pluginssubdir	wp-content/plugins
%define		pluginsdir	%{wordpressdir}/%{pluginssubdir}

%description
WordPress is a state-of-the-art semantic personal publishing platform
with a focus on aesthetics, web standards, and usability.

This package provides additional plugins, which enhace WordPress
functionality. Be ware: this package includes many plugins, which you
may not want to install, and willing to use specific packages
separately instead.

%description -l pl
WordPress jest technologicznie dopracowan±, semantyczn±, osobist±
platform± do publikacji k³ad±c± nacisk na standardy WWW oraz
u¿yteczno¶æ.

Ten pakiet dostarcza wtyczki rozszerzaj±ce funkcjonalno¶æ WordPress.
Uwaga: ten pakiet zawiera w sobie wiele wtyczek, byæ mo¿e takich,
które nie s± akurat potrzebne - w takim wypadku mo¿na instalowaæ
wtyczki osobno.

%package -n wordpress-plugin-khanhs_content_adder
Summary:	Content Adder plugin for WordPress
Summary(pl):	Wtyczka Content Adder dla WordPress
Group:		Applications/Publishing
URL:		http://www.thoughtmechanics.com/
Requires:	wordpress
Provides:	wordpress-plugin

%description -n wordpress-plugin-khanhs_content_adder
With KCA you can add HTML or JavaScript anywhere there's an ID
attribute defined. Configuration is easy: configure the plugin file
with the content you want, activate the plugin and you're done.

%description -n wordpress-plugin-khanhs_content_adder -l pl
Przy pomocy tej wtyczki mo¿na dodawaæ HTML czy JavaScript wszêdzie
tam, gdzie zdefiniowany jest atrybut ID. Konfiguracja jest prosta:
wystarczy skonfigurowaæ plik wtyczki wzglêdem posiadanej tre¶ci,
uaktywniæ j± i u¿ywaæ.

%package -n wordpress-plugin-excerpt_preview
Summary:	Excerpt Preview plugin for WordPress
Summary(pl):	Wtyczka Excerpt Preview dla WordPress
Group:		Applications/Publishing
URL:		http://pericat.ca/unlock/
Requires:	wordpress
Provides:	wordpress-plugin

%description -n wordpress-plugin-excerpt_preview
This plugin adds a preview of the post's excerpt below that of its
content following a 'save' in the admin panel's Write/Edit page.
Mostly useful for photologs that use the excerpt field to store
thumbnails.

%description -n wordpress-plugin-excerpt_preview -l pl
Ta wtyczka pozwala u¿ywaæ podgl±du fragment wpisu tu¿ przed miejscem
gdzie jego zawarto¶æ poprzedza funkcjê 'zapisz' na stronie
Tworzenie/Edycja panelu administracyjnego. Wtyczka jest przydatna
g³ównie dla fotoblogów, które u¿ywaj± pola podgl±du, aby przechowywaæ
miniaturki.

%prep
%setup -q -c -T
cp %{SOURCE0} .
tar xvzf %{SOURCE1}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{wordpressdir} $RPM_BUILD_ROOT%{pluginsdir}

for i in *.phps
do
    mv -f $i $(basename $i .phps).php
done
find . -type f -name '*.php' -o -name '*.txt' -o -name '*.htm*' -o -name '*.js' | xargs dos2unix
cp -R * $RPM_BUILD_ROOT%{pluginsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{pluginsdir}
%verify(not md5 size mtime) %{pluginsdir}/*

%files -n wordpress-plugin-khanhs_content_adder
%defattr(644,root,root,755)
%dir %{pluginsdir}
%verify(not md5 size mtime) %{pluginsdir}/kca.php

%files -n wordpress-plugin-excerpt_preview
%defattr(644,root,root,755)
%dir %{pluginsdir}
%{pluginsdir}/kca.php
