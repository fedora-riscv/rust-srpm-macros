Name:           rust-srpm-macros
Version:        5
Release:        1%{?dist}
Summary:        RPM macros for building Rust source packages

License:        MIT
URL:            https://pagure.io/fedora-rust/rust2rpm
Source0:        https://releases.pagure.org/fedora-rust/rust2rpm/rust2rpm-%{version}.tar.xz

BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup -n rust2rpm-%{version}

%install
install -D -p -m 0644 -t %{buildroot}%{_rpmmacrodir} data/macros.rust-srpm

%files
%license LICENSE
%{_rpmmacrodir}/macros.rust-srpm

%changelog
* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5-1
- Update to 5

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 08 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4-2
- Include license

* Fri Jul 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4-1
- Update to 4

* Tue Jun 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3-1
- Initial package
