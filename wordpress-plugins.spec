Summary:	Plugins for the WordPress personal publishing system
Summary(pl.UTF-8):	Wtyczki dla osobistego systemu publikacji WordPress
Name:		wordpress-plugins
Version:	1.6
Release:	1
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
# WTF? Each time I download this file it has new md5sum? Is it generated "on the fly"?
# Source4:	http://downloads.wordpress.org/plugin/feedwordpress.2010.0127.zip
Source4:	http://execve.pl/PLD/feedwordpress.2010.0127.zip
# Source4-md5:	d84349218f3f067030b5c148bc108ff1
URL:		http://codex.wordpress.org/Plugins
BuildRequires:	rpm-build-macros >= 1.553
Requires:	wordpress = %{version}
Obsoletes:	wordpress-plugin
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		wordpressdir	%{_datadir}/wordpress
%define		pluginssubdir	wp-content/plugins
%define		pluginsdir	%{wordpressdir}/%{pluginssubdir}

%description
WordPress is a state-of-the-art semantic personal publishing platform
with a focus on aesthetics, web standards, and usability.

This package provides additional plugins, which enhace WordPress
functionality. Be ware: this package includes many plugins, which you
may not want to install, and willing to use specific packages
separately instead.

%description -l pl.UTF-8
WordPress jest technologicznie dopracowaną, semantyczną, osobistą
platformą do publikacji kładącą nacisk na standardy WWW oraz
użyteczność.

Ten pakiet dostarcza wtyczki rozszerzające funkcjonalność WordPress.
Uwaga: ten pakiet zawiera w sobie wiele wtyczek, być może takich,
które nie są akurat potrzebne - w takim wypadku można instalować
wtyczki osobno.

%package -n wordpress-plugin-khanhs_content_adder
Summary:	Content Adder plugin for WordPress
Summary(pl.UTF-8):	Wtyczka Content Adder dla WordPress
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

%description -n wordpress-plugin-khanhs_content_adder -l pl.UTF-8
Przy pomocy tej wtyczki można dodawać HTML czy JavaScript wszędzie
tam, gdzie zdefiniowany jest atrybut ID. Konfiguracja jest prosta:
wystarczy skonfigurować plik wtyczki względem posiadanej treści,
uaktywnić ją i używać.

%package -n wordpress-plugin-excerpt_preview
Summary:	Excerpt Preview plugin for WordPress
Summary(pl.UTF-8):	Wtyczka Excerpt Preview dla WordPress
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

%description -n wordpress-plugin-excerpt_preview -l pl.UTF-8
Ta wtyczka pozwala używać podglądu fragment wpisu tuż przed miejscem
gdzie jego zawartość poprzedza funkcję 'zapisz' na stronie
Tworzenie/Edycja panelu administracyjnego. Wtyczka jest przydatna
głównie dla fotoblogów, które używają pola podglądu, aby przechowywać
miniaturki.

%package -n wordpress-plugin-next_to_last
Summary:	Next-to-last plugin for WordPress
Summary(pl.UTF-8):	Wtyczka następny-to-ostatniego dla WordPress
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

%description -n wordpress-plugin-next_to_last -l pl.UTF-8
Ta wtyczka umieszcza odnośniki "<< last post" oraz "next post >>" na
górze i na dole strony Edycji i pozwala w ten sposób użytkownikowi w
łatwy sposób przechodzić do następnej bądź poprzedniej strony z
wpisem. Wtyczka ta używa JavaScript.

%package -n wordpress-plugin-paged_comment_editing
Summary:	Paged Comment Editing plugin for WordPress
Summary(pl.UTF-8):	Wtyczka Stronicowanej Edycji Komentarzy dla WordPress
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
  interface, including arbitrary numbers of posts per page as well as
  paging of comment searching

- viewing invisible comments (e.g. marked as invisible by filters)

%description -n wordpress-plugin-paged_comment_editing -l pl.UTF-8
Ta wtyczka przechwytuje zarządzanie interfejsem magazynującym
edytowane komentarze w celu rozszerzenia go o następujące możliwości:

- przechodzenie poprzez strony komentarzy w interfejsie
  administracyjnym komentarzy, włączając w to ustawianie żądanej liczby
  jednocześnie wyświetlanych na stronie wpisów, czy stronicowanie
  wyszukiwania w komentarzach

- oglądanie niewidocznych komentarzy (np. zaznaczonych jako
  niewidoczne przez filtry)

%package -n wordpress-plugin-feedwordpress
Summary:	Atom/RSS aggregator for the WordPress
Summary(pl.UTF-8):	Agregator Atom/RSS dla WordPress
License:	GPL
Group:		Applications/Publishing
URL:		http://feedwordpress.radgeek.com/
# Requires wordpress with new MagpieRSS
Requires:	wordpress >= 2.9.2-2
Provides:	wordpress-plugin
Obsoletes:	wordpress-plugins

%description -n wordpress-plugin-feedwordpress
FeedWordPress is an Atom/RSS aggregator for the WordPress weblog
software. It syndicates content from feeds that you choose into your
WordPress weblog; if you syndicate several feeds you can use
WordPress's posts database and templating engine as the back-end of an
aggregator (planet) website. It was originally developed because I
needed a more flexible replacement for Planet to use at Feminist
Blogs.

%prep
%setup -q -c -T
cp %{SOURCE0} .
tar xvzf %{SOURCE1}
unzip -qq %{SOURCE2}
unzip -qq %{SOURCE3}
unzip -qq %{SOURCE4}

# don't install these files. They are provided by wordpress package.
rm -rf feedwordpress/MagpieRSS-upgrade

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{wordpressdir} $RPM_BUILD_ROOT%{pluginsdir}

for i in *.phps
do
    mv -f $i $(basename $i .phps).php
done
find . -type f -name '*.php' -o -name '*.txt' -o -name '*.htm*' -o -name '*.js' | xargs %undos
cp -R * $RPM_BUILD_ROOT%{pluginsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(640,http,http) %{pluginsdir}/*

%files -n wordpress-plugin-khanhs_content_adder
%defattr(644,root,root,755)
%attr(640,http,http) %{pluginsdir}/kca.php

%files -n wordpress-plugin-excerpt_preview
%defattr(644,root,root,755)
%attr(640,http,http) %{pluginsdir}/previewexcerpt.php

%files -n wordpress-plugin-next_to_last
%defattr(644,root,root,755)
%attr(640,http,http) %{pluginsdir}/next-to-last.php

%files -n wordpress-plugin-paged_comment_editing
%defattr(644,root,root,755)
%attr(640,http,http) %{pluginsdir}/edit-comments-full.php

%files -n wordpress-plugin-feedwordpress
%defattr(644,root,root,755)
%doc feedwordpress/readme.txt feedwordpress/ChangeLog.text
%dir %attr(750,http,http) %{pluginsdir}/feedwordpress
%attr(640,http,http) %{pluginsdir}/feedwordpress/*.p??
