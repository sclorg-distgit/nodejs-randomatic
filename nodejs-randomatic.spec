%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}
%global npm_name randomatic

Summary:       Generate randomized strings of a specified length, fast
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       1.1.5
Release:       5%{?dist}
License:       MIT
URL:           https://github.com/jonschlinkert/randomatic
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}nodejs-devel
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch

%description
Generate randomized strings of a specified length, fast. 
Only the length is necessary, but you can optionally generate 
patterns using any combination of numeric, alpha-numeric, 
alphabetical, special or custom characters.

%prep
%setup -q -n package
chmod 644 *

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{npm_name}

%changelog
* Mon Jul 03 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.1.5-5
- rh-nodejs8 rebuild

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.1.5-4
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.1.5-3
- Rebuilt with updated metapackage

* Thu Jan 14 2016 Tomas Hrcka <thrcka@redhat.com> - 1.1.5-2
- Enable scl macros

* Wed Dec 16 2015 Troy Dawson <tdawson@redhat.com> - 1.1.5-1
- Initial package
