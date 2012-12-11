%define oname trollop

Name:       rubygem-%{oname}
Version:    1.16.2
Release:    %mkrel 1
Summary:    Trollop is a commandline option parser for Ruby that just gets out of your way
Group:      Development/Ruby
License:    Ruby or GPLv2
URL:        http://trollop.rubyforge.org
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}
Requires:   rubygems
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
Trollop is a commandline option parser for Ruby that just
gets out of your way. One line of code per option is all you need to write.
For that, you get a nice automatically-generated help page, robust option
parsing, command subcompletion, and sensible defaults for everything you don't
specify.


%prep

%build

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}

%clean
rm -rf %buildroot

%files
%defattr(-, root, root, -)
%{ruby_gemdir}/gems/%{oname}-%{version}/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec


%changelog
* Sat Oct 09 2010 Rémy Clouard <shikamaru@mandriva.org> 1.16.2-1mdv2011.0
+ Revision: 584371
- import rubygem-trollop

