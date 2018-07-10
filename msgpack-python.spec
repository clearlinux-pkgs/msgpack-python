#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : msgpack-python
Version  : 0.5.6
Release  : 41
URL      : https://pypi.python.org/packages/8a/20/6eca772d1a5830336f84aca1d8198e5a3f4715cd1c7fc36d3cc7f7185091/msgpack-python-0.5.6.tar.gz
Source0  : https://pypi.python.org/packages/8a/20/6eca772d1a5830336f84aca1d8198e5a3f4715cd1c7fc36d3cc7f7185091/msgpack-python-0.5.6.tar.gz
Summary  : MessagePack (de)serializer.
Group    : Development/Tools
License  : Apache-2.0
Requires: msgpack-python-python3
Requires: msgpack-python-python
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools

%description
======================
MessagePack for Python
======================
.. image:: https://travis-ci.org/msgpack/msgpack-python.svg?branch=master
:target: https://travis-ci.org/msgpack/msgpack-python
:alt: Build Status

%package python
Summary: python components for the msgpack-python package.
Group: Default
Requires: msgpack-python-python3

%description python
python components for the msgpack-python package.


%package python3
Summary: python3 components for the msgpack-python package.
Group: Default
Requires: python3-core

%description python3
python3 components for the msgpack-python package.


%prep
%setup -q -n msgpack-python-0.5.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1520780343
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages py.test-2.7 --verbose || :
%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
