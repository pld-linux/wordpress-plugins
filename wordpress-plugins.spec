Summary:	Plugins for the WordPress personal publishing system
Summary(pl):	Wtyczki dla osobistego systemu publikacji WordPress
Name:		wordpress-plugins
Version:	1.5
Release:	2
License:	GPL or MIT or Free
Group:		Applications/Publishing
Source0:	http://ink.bur.st/wp-content/downloads/kca.phps
# Source0-md5:	a6aecdf5eeee244f1537825921773625
Source1:	http://pericat.ca/downloads/previewexcerpt.tar.gz
# Source1-md5:	41e6c2f87dec2225ac33a4eef74fab39
Source2:	http://thunkgeek.com/files/next-to-last.zip
# Source2-md5:	6c6812e81adc1cc7320a8d5674b7dfb4
Source3:	http://www.coldforged.org/paged_comment_editing.zip
# Source3-md5:	86452bfd4369877f3faea8639e457326
URL:		http://codex.wordpress.org/Plugins
BuildRequires:	dos2unix
Requires:	wordpress = %{version}
Obsoletes:	wordpress-plugin
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
License:	MIT
Group:		Applications/Publishing
URL:		http://www.thoughtmechanics.com/
Requires:	wordpress
Provides:	wordpress-plugin
Obsoletes:	wordpress-plugins

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
License:	Free
Group:		Applications/Publishing
URL:		http://pericat.ca/unlock/
Requires:	wordpress
Provides:	wordpress-plugin
Obsoletes:	wordpress-plugins

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

%package -n wordpress-plugin-next_to_last
Summary:	Next-to-last plugin for WordPress
Summary(pl):	Wtyczka nastêpny-to-ostatniego dla WordPress
License:	GPL
Group:		Applications/Publishing
URL:		http://thunkgeek.com/wordpress-plugins.php
Requires:	wordpress
Provides:	wordpress-plugin
Obsoletes:	wordpress-plugins

%description -n wordpress-plugin-next_to_last
This plugin places "<< last post" and "next post >>" links at the top
and bottom of the Edit page in Wordpress to allow the user to easily
get back and forth between their posts. This plugin uses JavaScript.

%description -n wordpress-plugin-next_to_last -l pl
Ta wtyczka umieszcza odno¶niki "<< last post" oraz "next post >>" na
górze i na dole strony Edycji i pozwala w ten sposób u¿ytkownikowi w
³atwy sposób przechodziæ do nastêpnej b±d¼ poprzedniej strony z
wpisem. Wtyczka ta u¿ywa JavaScript.

%package -n wordpress-plugin-paged_comment_editing
Summary:	Paged Comment Editing plugin for WordPress
Summary(pl):	Wtyczka Stronicowanej Edycji Komentarzy dla WordPress
License:	GPL
Group:		Applications/Publishing
URL:		http://www.coldforged.org/paged-comment-editing-plugin/
Requires:	wordpress
Provides:	wordpress-plugin
Obsoletes:	wordpress-plugins

%description -n wordpress-plugin-paged_comment_editing
This plugin overhauls the stock comment editing interface to provide
the following capabilities:

- paging through all of comments in the comment administration
  interface, including arbitrary numbers of posts per page as well
  as paging of comment searching

- viewing invisible comments (e.g. marked as invisible by filters)

%description -n wordpress-plugin-paged_comment_editing -l pl
Ta wtyczka przechwytuje zarz±dzanie interfejsem magazynuj±cym
edytowane komentarze w celu rozszerzenia go o nastêpuj±ce mo¿liwo¶ci:

- przechodzenie poprzez strony komentarzy w interfejsie
  administracyjnym komentarzy, w³±czaj±c w to ustawianie ¿±danej liczby
  jednocze¶nie wy¶wietlanych na stronie wpisów, czy stronicowanie
  wyszukiwania w komentarzach

- ogl±danie niewidocznych komentarzy (np. zaznaczonych jako
  niewidoczne przez filtry)

%prep
%setup -q -c -T
cp %{SOURCE0} .
tar xvzf %{SOURCE1}
unzip -qq %{SOURCE2}
unzip -qq %{SOURCE3}

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
%defattr(644,root,http,755)
%dir %{pluginsdir}
%verify(not md5 mtime size) %{pluginsdir}/*

%files -n wordpress-plugin-khanhs_content_adder
%defattr(644,root,http,755)
%dir %{pluginsdir}
%verify(not md5 mtime size) %{pluginsdir}/kca.php

%files -n wordpress-plugin-excerpt_preview
%defattr(644,root,http,755)
%dir %{pluginsdir}
%verify(not md5 mtime size) %{pluginsdir}/previewexcerpt.php

%files -n wordpress-plugin-next_to_last
%defattr(644,root,http,755)
%dir %{pluginsdir}
%verify(not md5 mtime size) %{pluginsdir}/next-to-last.php

%files -n wordpress-plugin-paged_comment_editing
%defattr(644,root,http,755)
%dir %{pluginsdir}
%verify(not md5 mtime size) %{pluginsdir}/edit-comments-full.php
